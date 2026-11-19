"""Exercise the published textbook in Chromium, including mobile emulation."""
import os
import re
import shutil

from playwright.sync_api import expect, sync_playwright

URL = os.getenv("TEXTBOOK_URL", "http://127.0.0.1:8765/deutsch-publishing-lab/")
CHAPTERS = {
    "anzeigen": ([0, 1, 2], [0, 1, 0]),
    "anschreiben": ([1, 0, 2], [0, 1, 1]),
    "gespraech": ([1, 0, 2], [0, 0, 0]),
    "betrieb": ([1, 2, 0], [0, 1, 2]),
    "schule": ([1, 0, 2], [1, 0, 2]),
}


def check_width(page, width):
    sizes = page.evaluate("""() => {
      const elements = [document.documentElement,
        ...document.querySelectorAll('.library-shell,.study-dialog,.final-dialog,.is-writing-focus')];
      return elements.filter(el => el.clientWidth).map(el =>
        [el.id || el.className || 'document', el.clientWidth, el.scrollWidth]);
    }""")
    assert sizes[0][1] == width, sizes
    assert all(scroll <= client + 1 for _, client, scroll in sizes), sizes


def test_viewport(browser, width, height, mobile):
    context = browser.new_context(viewport={"width": width, "height": height},
                                  is_mobile=mobile, has_touch=mobile, reduced_motion="reduce")
    page = context.new_page()
    page.set_default_timeout(7000)
    page.add_init_script("""(() => {
      window.qaClicks = [];
      document.addEventListener('click', event => {
        const target = event.target.closest('button,input,select');
        window.qaClicks.push([location.pathname, target?.outerHTML.slice(0, 180) || event.target.tagName,
          event.clientX, event.clientY, window.scrollY]);
      }, true);
    })();""")
    errors = []
    def activate(control):
        if mobile:
            control.tap()
        else:
            control.click()
    page.on("pageerror", lambda error: errors.append(str(error)))
    try:
        assert page.goto(URL).ok
        library = page.locator("#learning-library")
        expect(library).to_be_visible()
        check_width(page, width)

        for chapter, (reading, language) in CHAPTERS.items():
            page.locator(f'[data-open-lesson="{chapter}"]').click()
            lesson = page.locator(f"#lesson-{chapter}")
            expect(lesson).to_be_visible()
            expect(lesson.locator("h1")).to_be_focused()
            check_width(page, width)
            page.locator(f'[data-scroll-step="{chapter}-step-2"]').click()

            def choose(index, value):
                lesson.locator(f'[name="{chapter}-q{index}"][value="{value}"]').check()

            grade = lesson.locator('[onclick^="grade("]')
            for index, value in enumerate(reading):
                choose(index, (value + 1) % 3 if index == 0 else value)
            grade.scroll_into_view_if_needed()
            activate(grade)
            assert not errors, errors
            expect(page.locator(f"#score-{chapter}")).to_contain_text("2 von 3")
            choose(0, reading[0])
            expect(page.locator(f"#score-{chapter}")).to_contain_text("erneut prüfen")
            activate(grade)
            assert not errors, errors
            expect(page.locator(f"#score-{chapter}")).to_contain_text("3 von 3")

            check_language = lesson.locator("[data-check-practice]")
            for index, value in enumerate(language):
                page.select_option(f"#cloze-{chapter}-{index}", str((value + 1) % 3 if index == 0 else value))
            activate(check_language)
            expect(page.locator(f"#cloze-score-{chapter}")).to_contain_text("2 / 3")
            page.select_option(f"#cloze-{chapter}-0", str(language[0]))
            expect(page.locator(f"#cloze-score-{chapter}")).to_contain_text("erneut prüfen")
            activate(check_language)
            expect(page.locator(f"#cloze-score-{chapter}")).to_contain_text("3 / 3")

            toggle = lesson.locator(f'[aria-controls="write-{chapter}"]')
            activate(toggle)
            draft = page.locator(f"#write-{chapter}")
            expect(draft).to_be_focused()
            check_width(page, width)
            draft.fill("Mein erster Entwurf.")
            draft.fill("Das ist mein überarbeiteter Entwurf.")
            expect(page.locator(f"#count-{chapter}")).to_contain_text("5 Wörter")
            page.keyboard.press("Escape")
            expect(toggle).to_be_focused()
            expect(toggle).to_have_attribute("aria-pressed", "false")
            page.locator("#reader-back-library").click()
            expect(library.locator("h1")).to_be_focused()

        # Editorial writing workshops in chapters 1 and 2 must preserve drafts.
        page.locator('[data-open-lesson="anzeigen"]').click()
        page.locator("#evidence-write-anzeigen").fill("In der Anzeige finde ich konkrete Informationen.")
        page.locator("#reader-back-library").click()
        page.locator('[data-open-lesson="anschreiben"]').click()
        page.locator("#motivation-write-anschreiben").fill("Mein kleines Projekt zeigt, wie ich lerne.")
        page.locator("#reader-back-library").click()
        page.locator('[data-open-lesson="gespraech"]').click()
        page.locator("#interview-write-gespraech").fill("Ich habe die Aufgabe sorgfältig gelöst.")
        page.locator("#interview-followup-gespraech").fill("Beim zweiten Versuch habe ich nachgefragt.")
        page.locator("#reader-back-library").click()
        page.locator("#library-start").click()
        if width <= 840:
            page.locator("#next").click()
            expect(page.locator("#quick-chapter")).to_have_value("anschreiben")
            page.locator("#prev").click()
            expect(page.locator("#quick-chapter")).to_have_value("anzeigen")
        else:
            page.locator('.chapter-link[data-lesson="anschreiben"]').click()
            expect(page.locator("#quick-chapter")).to_have_value("anschreiben")
        page.select_option("#quick-chapter", "schule")
        page.locator("#reader-back-library").click()
        page.locator("#library-continue").click()
        expect(page.locator("#quick-chapter")).to_have_value("schule")
        page.locator("#theme").click()
        expect(page.locator("body")).to_have_class(re.compile("night"))
        page.locator("#reader-larger").click()
        page.locator("#reader-smaller").click()
        page.locator("#reader-larger").click()
        assert page.locator("body").evaluate("el => el.style.getPropertyValue('--reader-scale')") == "1.1"

        page.locator("#open-study-top").click()
        expect(page.locator("#study-stats")).to_contain_text("30/30")
        check_width(page, width)
        for key in ("Shift+Tab", "Tab", "Tab"):
            page.keyboard.press(key)
            assert page.evaluate("!!document.activeElement.closest('.study-dialog')")
        page.keyboard.press("Escape")
        expect(page.locator("#open-study-top")).to_be_focused()
        page.reload()
        expect(library).to_be_visible()
        expect(library).to_have_css("background-color", "rgb(24, 35, 29)")
        page.locator("#library-continue").click()
        expect(page.locator("#quick-chapter")).to_have_value("schule")
        expect(page.locator("#write-schule")).to_have_value("Das ist mein überarbeiteter Entwurf.")
        expect(page.locator('[name="schule-q0"][value="1"]')).to_be_checked()
        expect(page.locator("#cloze-schule-0")).to_have_value("1")
        expect(page.locator("body")).to_have_class(re.compile("night"))
        assert page.locator("body").evaluate("el => el.style.getPropertyValue('--reader-scale')") == "1.1"

        page.locator("#reader-back-library").click()
        page.locator('[data-open-lesson="anzeigen"]').click()
        expect(page.locator("#evidence-write-anzeigen")).to_have_value("In der Anzeige finde ich konkrete Informationen.")
        page.locator("#reader-back-library").click()
        page.locator('[data-open-lesson="anschreiben"]').click()
        expect(page.locator("#motivation-write-anschreiben")).to_have_value("Mein kleines Projekt zeigt, wie ich lerne.")
        page.locator("#reader-back-library").click()
        page.locator('[data-open-lesson="gespraech"]').click()
        expect(page.locator("#interview-write-gespraech")).to_have_value("Ich habe die Aufgabe sorgfältig gelöst.")
        expect(page.locator("#interview-followup-gespraech")).to_have_value("Beim zweiten Versuch habe ich nachgefragt.")
        page.locator("#reader-back-library").click()

        page.locator("#library-continue").click()
        page.locator("#final-open").click()
        expect(page.locator(".final-dialog")).to_be_visible()
        check_width(page, width)
        page.locator('[aria-controls="final-writing"]').click()
        page.locator("#final-writing").fill("Mein Abschlusstext.")
        page.keyboard.press("Escape")
        expect(page.locator(".final-dialog")).to_be_visible()
        page.keyboard.press("Escape")
        expect(page.locator(".final-dialog")).to_be_hidden()
        assert not errors, errors
        print(f"PASS {width} × {height}, {'mobile emulation' if mobile else 'desktop browser viewport'}", flush=True)
    except Exception:
        print(f"Failed at {width} × {height}: {page.title()}, errors={errors}", flush=True)
        print(page.evaluate("window.qaClicks?.slice(-12)"), flush=True)
        raise
    finally:
        context.close()


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(executable_path=shutil.which("google-chrome"))
    for width, height, mobile in [(320, 700, True), (375, 812, True), (390, 844, True),
                                  (430, 932, True), (768, 1024, True), (1440, 900, False)]:
        test_viewport(browser, width, height, mobile)
