# Writing loop — curriculum + Grok-powered prompt/feedback cycle (spec)

Status: **spec v1 (proposal)** · 2026-08-07 · owner-directed  
Position: the writing pillar's engine. Reading feeds writing: *you've read Black Beauty — now write.*  
**Wire rule:** every payload here is a **proposal** — nothing ships until it lands in `goji_cloud/SYNC_API.md`. Product rules honored: the **Pi never calls third-party AI**; generation and analysis are cloud-side (the `content-generate` edge-function path + Grok/xAI key, parent-side billing, ~v1.2 paywall per product TODO).

---

## 1. The loop (one cycle)

```
 profile + progress + anchor book          child writes                  analysis
        │                                        │                           │
        ▼                                        ▼                           ▼
 ┌──────────────┐   prompt    ┌──────────┐  submission  ┌──────────┐  feedback  ┌────────────┐
 │ cloud: Grok  │──────sync──►│  Goji:   │──────sync───►│ cloud:   │────sync───►│ parent app │
 │ prompt gen   │             │ writing  │              │ Grok     │            │ + Goji     │
 └──────────────┘             │ app      │              │ analysis │            │ (encourage)│
                              └──────────┘              └──────────┘            └────────────┘
```

1. **Generate** (cloud, on parent action or suggested-day): Grok gets the child's profile and produces a grade-appropriate prompt tied to the anchor book and the grammar skills in progress.
2. **Write** (device, offline): the prompt arrives as synced content (same `synced_content_cache` mechanism as quizzes); child writes in the writing app; submission uploads through existing activity/content sync.
3. **Analyze** (cloud): Grok scores against the *finite* skill list — not vibes — and returns structured feedback.
4. **Display**: parent app shows strengths/struggles mapped to skill IDs (feeds the standing heat map — `PARENT_STANDING_UX.md`); the device shows only child-appropriate encouragement + one gentle next step. Parent can **read the actual writing** (journal-read parity).

## 2. Payload proposals (for SYNC_API)

### 2a. Prompt generation request (parent app / suggested-day → edge function)

```json
{
  "child_cloud_id": "…",
  "grade_band": "k2",
  "anchor_book_id": "black-beauty",
  "recent_reading": [{"book_id": "black-beauty", "chapters": [12, 13]}],
  "skills_in_progress": ["obj.writing.k2.grammar.01", "obj.reading.k2.comp.01"],
  "mode": "response_to_text | narrative | informative | opinion",
  "constraints": {"min_words": 30, "encourage": ["complete sentences", "one feeling word"]}
}
```

### 2b. Generated prompt (edge function → synced content, kind: `writing_prompt`)

```json
{
  "prompt_id": "wp_…",
  "objectives": ["obj.writing.k2.grammar.01"],
  "book_id": "black-beauty",
  "prompt_text": "Beauty just met Ginger. Write 3 sentences about a time you met someone new. Use a feeling word.",
  "child_display": {"title": "Writing time!", "min_words": 30},
  "rubric": [
    {"skill": "obj.writing.k2.grammar.01", "look_for": "complete sentences (naming + telling part)"},
    {"skill": "obj.writing.k2.mechanics.01", "look_for": "capitals + end marks"}
  ]
}
```

The **rubric rides with the prompt** so analysis is deterministic about what to grade — same blueprint-not-vague-prompt rule as quiz generation (QUIZZES.md §4).

### 2c. Submission (device → cloud, via existing content/activity push)

```json
{
  "prompt_id": "wp_…",
  "child_cloud_id": "…",
  "text": "…the child's writing…",
  "word_count": 47,
  "duration_s": 610,
  "written_at": "ISO"
}
```

### 2d. Analysis result (edge function → parent app + device ack)

```json
{
  "prompt_id": "wp_…",
  "skill_results": [
    {"skill": "obj.writing.k2.grammar.01", "level": "strong | developing | struggling", "evidence": "3 of 4 sentences complete; 'ran fast to the' is a fragment"},
    {"skill": "obj.writing.k2.mechanics.01", "level": "strong", "evidence": "all capitals and end marks correct"}
  ],
  "strengths_note": "Great feeling word: 'nervous'.",
  "parent_note": "Fragments appear when sentences get long — practice quiz.writing.k2.grammar.01.",
  "child_note": "You used a super feeling word! One sentence lost its ending — can you find it?",
  "suggested_next": ["quiz.writing.k2.grammar.01", "lesson.writing.k2.grammar.01"]
}
```

**Consumption map:** parent app renders `skill_results` (heat-map fuel) + `parent_note` + full text; device shows only `child_note`; `skill_results` also append to the child's objective history so standing updates without a human in the loop. `evidence` strings keep the parent's trust — never a bare score.

## 3. Trust & safety rails

- Parent **reviews before the child sees feedback** (toggleable later; default on) — same review-before-push stance as generated quizzes.
- Analysis levels map to the standing model's three states; **no 0–100 scores** (PARENT_STANDING.md rule).
- The child's raw text syncs only within the family's Supabase scope; never used beyond the API call. Flag in the privacy one-pager (product TODO).
- Grok unavailable / no key → the loop degrades to **manual mode**: parent-authored prompt from a curriculum prompt bank + parent sign-off (v1 path that exists today via journal).

## 4. Integration duties (the point)

- **Reading → writing:** prompts default to the anchor book (INTEGRATION.md §1) — comprehension objectives are co-tagged so one submission can credit both pillars.
- **Typing:** typing drills seed from **anchor-book quotes** (same lines the child read; TOOLS.md note) — typing practice is writing-fluency practice.
- **Flashcards:** analysis struggles spawn deck suggestions (fragment trouble → sentence-parts deck; new words used → vocab deck credit).
- **Quizzes:** `suggested_next` points at existing grammar quiz blueprints — the loop closes into teach → practice → check, never a dead-end grade.

## 5. Build order (route via SYNC_API first)

1. SYNC_API: `writing_prompt` content kind + submission/analysis tables + edge functions (`writing-prompt-generate`, `writing-analyze`).
2. Device: writing app consumes `writing_prompt`, submits (offline queue like plan status).
3. Parent app: prompt trigger in wizard + feedback surfaces (`PARENT_STANDING_UX.md` §4).
4. Curriculum: prompt banks per band for manual mode (subjects/writing — composition strand).
5. Paywall wiring (~v1.2 per product TODO).
