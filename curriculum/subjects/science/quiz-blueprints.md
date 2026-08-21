# Science — quiz blueprints (K–2 first objective)

Format per [`../../QUIZZES.md`](../../QUIZZES.md) §4. For interactive lesson packages the check is **built into the package** and its score is posted via `lesson.check` / `lesson.complete` (see [`../../LESSON_PACKAGES.md`](../../LESSON_PACKAGES.md) §4). Until the player ships, deliver the same items as a **parent quiz**.

---

## `quiz.science.k2.living.01` — Living or not living?

```yaml
quiz.science.k2.living.01:
  objectives: [obj.science.k2.living.01]
  skill: "classify living vs nonliving; name the sign of life used"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at K
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one moving nonliving thing, one still living thing, one once-alive object, one "which sign?" item]
    distractors: movement-as-life, stillness-as-nonlife, once-alive-as-alive
```

**Gold items (v1):** (each distractor names its misconception)

1. A **wolf** runs through the woods. Living or not living? → **living** / not living *(baseline)*
2. A **river** rushes downhill all day. Living or not living? → living *(movement-as-life)* / **not living**
3. An **oak tree** stands still all winter. Living or not living? → **living** / not living *(stillness-as-nonlife)*
4. A **log** on the ground. Living or not living? → living *(once-alive-as-alive)* / **not living**
5. A **fox** has three kits in spring. Which sign of life is that? → grows / needs food / **makes more of its kind** / moves

Retakes swap the animal for the current fable animal (ant, crow, lion, hare…) — the misconceptions stay fixed.
