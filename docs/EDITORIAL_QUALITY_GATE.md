# Editorial Quality Gate — Deutsch für den Ausbildungsstart

Status: **open / not approved for commercial release**  
Review date: 2026-11-19  
Scope: current `main/index.html`, five chapters, automated answer keys and self-assessed writing.

## Evidence and limits

- The repository includes an automated Playwright workflow with Chromium/mobile emulation (320, 375, 390, 430, 768 and 1440 px).
- A successful CI job is **not** a test on a physical iPhone or Safari.
- The course uses auto-graded multiple-choice and selection questions plus independent writing tasks. A score on closed questions must not be advertised as a verified CEFR B1 qualification.
- Independent review by a qualified DaF/DaZ educator is still outstanding.

## Chapter-by-chapter editorial action list

| Chapter | Current core exercise | Next editorial check |
| --- | --- | --- |
| 01 Stellenanzeigen | Find responsibilities, requirements and missing details | Verify answers against the exact fictional vacancy; add one task requiring evidence quotation and one polite clarification question |
| 02 Anschreiben | Recognize motivation, subject line and closing phrase | Distinguish *acceptable* from *best for this stated purpose*; require an original paragraph with criteria and annotated model |
| 03 Vorstellungsgespräch | Choose project examples and appropriate questions | Add a branching follow-up that requires the learner to explain a project, not just identify a model answer |
| 04 Ausbildungsbetrieb | Clarifying task instructions and reporting errors | Verify dialogue/answer consistency; add an authentic repair sequence (problem → consequence → proposed next step) |
| 05 Berufsschule | Compare backup approaches and interpret deadlines | Add a structured comparison task and a transparent writing rubric; distinguish language evaluation from technical claims |

## Non-negotiable acceptance criteria

1. Each chapter states observable learning goals and includes a clear self-check tied to those goals.
2. Each closed question has one defensible keyed answer **given the exact instruction and reading text**. Distractors are plausible without being misleading.
3. Each grammar example and explanation is correct, with examples reviewed in their original sentence context.
4. Open writing tasks have sample responses **and** a rubric for content, politeness/register, organization and language; they are never automatically marked linguistically correct.
5. Word-count guidance is not misrepresented as grammar or CEFR assessment.
6. All educational examples using fictional companies and vacancies are marked as fictional. No trademarked employer identity should imply endorsement.
7. Responsive UI and keyboard interactions pass automated regression; a **real iOS Safari run remains mandatory** before claiming iPhone compatibility.
8. Existing `localStorage` keys and stored learner responses must survive any redesign. Run a data-migration regression before altering state format.
9. Verify screen reader semantics, focus order, zoom to 200%, reduced motion and color contrast.
10. Final release needs independent DaF/DaZ editorial sign-off, content corrections, privacy disclosure and an accessibility review.

## Release blockers and priorities

**P0 before public non-beta release:** independent DaF/DaZ language/pedagogy review; mobile Safari verification; accurate claims about scoring and data persistence.

**P1 for the next iteration:** strengthen authentic skill-transfer writing tasks; conduct full item-by-item review of all key mappings and messages; check mobile layouts at 200% browser text zoom.

**P2 after validated learning outcomes:** add new chapters, print layout, payments and commercial distribution.

## Test execution record

2026-11-19: GitHub Actions "Browser QA" on commit `25eb471f58a9bc4c03eda24676097f1d7f4f1199` concluded **success**; GitHub Pages build on the same commit concluded **success**. The live HTTPS page and physical Safari behavior were **not directly exercised in this review**.

This is a planning and source-code audit, **not** an independent certification or completed linguistic review.
