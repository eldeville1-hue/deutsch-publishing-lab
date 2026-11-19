# Deutsch Publishing Lab — Positioning & Market Validation v1

**Status:** research-ready; **not a paid product launch**  
**Date:** 2026-11-19  
**Existing live free beta:** https://eldeville1-hue.github.io/deutsch-publishing-lab/

## Product principle — preserve the learning logic

Keep the five-step learning journey:

1. **Stellenanzeigen verstehen** — read a job posting and distinguish requirements and benefits
2. **Bewerbungen schreiben** — explain motivation and present true, concrete experiences
3. **Vorstellungsgespräche führen** — answer, explain and ask follow-up questions
4. **Im Ausbildungsbetrieb kommunizieren** — clarify tasks, report issues, ask for feedback
5. **In der Berufsschule arbeiten** — understand tasks, compare, argue and summarize

Every lesson should preserve the existing progression: objectives → realistic source text/dialogue → comprehension → grammar/language training → strategy → authentic writing/transfer task → self-assessment. Preserve the existing browser storage key, exercise-answer mapping, navigation, five chapters, and user drafts. Any future refactor requires data-persistence tests.

**Core market:** newcomers preparing for Ausbildung in German-speaking Germany, ideally approximately B1 German. **Current content limitation:** many example scenarios focus on IT (particularly Anwendungsentwicklung). Market the *current* edition accurately as an IT-oriented pilot; generalize gradually rather than claiming it already covers all professions.

### Universality roadmap (do not implement without content QA)

- Keep existing IT scenarios as an optional **IT track**, never silently delete them.
- Add alternative authentic examples across **Einzelhandel**, **Büro/Verwaltung**, **Logistik**, **Handwerk**, and **Gesundheitswesen** only after ensuring terminology and workplace practices are sound.
- Organize the product around **transferable communication skills**, not a single occupation.
- Distinguish generic, cross-professional language from technical or regulated-profession specifics.
- Preserve a single coherent visual learning environment instead of cloning apps.

## Honest market hypothesis

> People preparing for an Ausbildung may value an interactive, mobile-first B1 workbook that focuses on practical language tasks rather than isolated vocabulary quizzes.

**Hypothesis not verified.** A free site visit or an expression of interest is not a sale. A purchase from an unfamiliar person is stronger evidence, subject to law and a clear paid value proposition.

## Phase A — 7-day discovery test (no payment collected)

Recruit 5–10 willing testers from relevant online groups or community networks, respecting group advertising rules. Do not collect unnecessary personal data; avoid public lists of learners.

Ask testers to use the **existing free beta** and answer four questions:
1. What are you preparing for (Ausbildung, Berufsschule, interview, or something else)?
2. Which chapter did you try, and where did you get stuck?
3. Would you use this again next week? Why or why not?
4. If a reviewed offline edition with additional exercises were available for **€6.90**, would you **consider** buying it? (No / Maybe / Yes). Make clear this is hypothetical and not an order.

Keep an evidence table, without names or emails: date, channel, profession/goal, chapter completed, major friction, hypothetical purchase interest, improvements requested. Count unique participants, not impressions or repeated responses.

**Do not claim:** 'X buyers', 'certified B1' or 'perfect for all professions'.

## Phase B — sales test, only after readiness gates

Do not take money until:
- independent DaF/DaZ review of the relevant material;
- verified **paid offer** meaningfully distinct from the freely available full beta (for example, reviewed offline pack with genuinely additional original exercises, printable study sheets, correction rubric and changelog);
- reviewed commercial-use rights and clear license for all content;
- checked German tax, self-employment classification and relevant online business/consumer information obligations with qualified local advice;
- verified payment/delivery, refunds and customer support approach.

**Suggested experimental price:** €6.90; this is an assumption for testing, not validated willingness to pay.

Payhip and similar services can host an eventual paid file, but they do **not** supply an audience by themselves.

## German promotional text — unpaid research post

**Titel:** Kostenloses B1-Arbeitsbuch für den Ausbildungsstart – Feedback gesucht

> Ich entwickle ein interaktives Deutsch-Arbeitsbuch für Menschen, die sich auf eine Ausbildung in Deutschland vorbereiten. Die aktuelle Web-Beta enthält fünf Kapitel zu Stellenanzeigen, Bewerbung, Vorstellungsgespräch, Kommunikation im Betrieb und Berufsschule. Viele Beispiele stammen derzeit aus dem IT-Bereich.
>
> Ich suche einige freiwillige Testpersonen, die ein Kapitel auf dem Handy ausprobieren und mir ehrlich sagen, was verständlich ist und was noch fehlt. Das Angebot ist kostenlos, keine Anmeldung und kein Kauf erforderlich. Es handelt sich um ein Lernprojekt, nicht um ein offizielles B1-Zertifikat.
>
> Kostenlos testen: https://eldeville1-hue.github.io/deutsch-publishing-lab/
>
> Falls Feedback in dieser Gruppe erlaubt ist, freue ich mich über kurze Rückmeldungen direkt hier.

Only publish where permitted. Do not add contact email addresses, checkout links, analytics, forms or trackers without explicit owner decision and adequate privacy/legal setup.

## Evaluation after 7 days

- Less than 5 meaningful test users: **insufficient distribution**, not proof of poor demand.
- Users start but cannot finish: focus on product usability and pedagogy before selling.
- Users finish and request more, but decline €6.90: investigate value differentiation.
- Multiple **independent** positive responses: consider a small, legally compliant paid experiment once a differentiated paid artifact exists.

## Technical release record

The most recent verified baseline as of 2026-11-19 was commit `732f4e94c2f85a9eea3696ad6c38e1fc603b6668`, with successful GitHub Pages deployment and successful Chromium-based Browser QA. This does not replace physical Safari testing or pedagogical review.
