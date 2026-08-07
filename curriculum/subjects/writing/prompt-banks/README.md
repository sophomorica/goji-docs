# Writing prompt banks — manual-mode fuel for the writing loop

Status: **authored 2026-08-07** · one file per band: [`k2.md`](./k2.md) · [`35.md`](./35.md) · [`68.md`](./68.md) · [`912.md`](./912.md)

**What these are.** The composition strand's prompt supply, twice over:

1. **Manual mode, today** (WRITING_LOOP_SPEC §3): no Grok, no key — the parent picks a prompt from the band file, assigns it as a journal/writing task with the min-words floor, and judges the result against the rubric line. Parent-judged, never auto-scored (PARENT_STANDING.md §2).
2. **Grok fuel, later** (WRITING_LOOP_SPEC §1–2): each entry already carries what the generated `writing_prompt` payload carries — objectives, book id, prompt text, per-skill `look_for` rubric lines, min words. Generation learns the house style from these; analysis grades against the same finite skill list.

**Entry format** (mirrors SPEC §2b):

- **book / topic** — an anchor book by on-device id (INTEGRATION.md §1) or a germane Kiwix topic (INTEGRATION.md §4). Nothing on the Goji is random; a prompt tied to neither is a defect.
- **mode** — recount · narrative · informative · opinion · analytical.
- **skills** — the `obj.writing.*` IDs the prompt exercises (compose + the grammar/mechanics riding along; reading co-tags where one submission credits both pillars, SPEC §4).
- **rubric** — `skill` → "look_for" lines, exactly what the parent (today) or Grok (later) checks.
- **min words** — floor enforced via the journal/writing app's synced word count.

Rotation note: prompts name specific anchors; when the band's anchor rotates (curriculum lead's call), prefer the current anchor's prompts and save the rest for review weeks — old anchors stay legal, they're just not the spine that week.
