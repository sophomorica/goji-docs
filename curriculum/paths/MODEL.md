# Skill path records

Status: target model for the framework build. 2026-09-23.

This is the data the parent app, the cloud, and the computer share when a parent assigns a skill. Field names match records this repo already uses. Where a live schema was not in the workspace, the field is marked ASSUMED and the source note says which doc it came from.

Why these records, and not a new platform, is in [SURVEY.md](./SURVEY.md). The build order is in [PLAN.md](./PLAN.md).

## Records

Five records. A skill is a catalog row. A path is the ordered template for one skill. A node is one step on that template. An assignment gives one path to one child on one school day. Progress is derived from events the device already uploads. It is not a second log.

### Skill

A skill is what the parent assigns. If an objective id exists, the skill id is that `obj.*` id. Objectives already carry a statement, a success criterion, prerequisites, a practice tool, a quiz, a Virginia code, and a status. See `subjects/math/OBJECTIVES.md` and `assets/templates/objective.md`.

If no objective exists yet, the skill id is the Virginia code already in `skills/`. Kindergarten `K.MG.2` is in that state. `skills/math-k.md` marks it as a gap. The framework does not invent an `obj.*` row and does not write the skill statement again.

| Field | Meaning |
| --- | --- |
| `id` | `obj.*` when one exists. Otherwise the Virginia code, such as `K.MG.2`. |
| `pillar` | `reading`, `writing`, or `math`. |
| `va_sol` | Zero or more Virginia codes. Empty only for a non-standards objective that already says so. |
| `prereq_ids` | Skill ids that precede this one. Copied from the objective prerequisite column when that column exists. |
| `obj_id` | The `obj.*` id, or null when the row is still only a coverage gap. |
| `path_id` | The path template, or null when nobody has ordered the nodes. A gap with a null path is a legal catalog row. |

The fixture skill is `K.MG.2`. `obj_id` is null. `path_id` is `path.K.MG.2`. No statement field is stored on this record. The words stay in `skills/math-k.md` until a curriculum lead authors an objective.

### Path

One path template per skill. The template is an ordered list of node ids plus one fail edge. It is not a course, and it is not generated from a standards list.

| Field | Meaning |
| --- | --- |
| `id` | `path.` plus the skill id. The fixture id is `path.K.MG.2`. |
| `skill_id` | The skill this path expands. |
| `version` | Integer. A pack update bumps the version. An open assignment keeps the version it started with. |
| `node_ids` | Ordered. The fixture order is teach, practice, check. |
| `on_check_fail` | The node id to reopen when the check gate fails. The fixture points at the teach node. |

### Node

A node is one school-day row. The role is the pedagogy. The task kind is an existing school-day type from [PARENT_APP_PRODUCT.md](../../PARENT_APP_PRODUCT.md) section 5. The node does not contain lesson sentences, items, or media.

| Field | Meaning |
| --- | --- |
| `id` | Stable. Fixture ids are `node.K.MG.2.teach`, `node.K.MG.2.practice`, and `node.K.MG.2.check`. |
| `path_id` | Parent path. |
| `role` | `teach`, `practice`, or `check`. |
| `task_kind` | An existing plan task kind. ASSUMED from [MATH_MODULE_TASKS_PLAN.md](../../MATH_MODULE_TASKS_PLAN.md). Math drills stay `app_time`. Exact `CHECK` values are copied from `SYNC_API.md` at implementation time, not invented here. |
| `content_ref` | An existing id (`lesson.*`, `quiz.*`, `anim.*`, a math module id, a book id, a deck id), or null. |
| `move_on` | `completed` or `passed`. Teach and practice use `completed`. Check uses `passed`. There is no implicit default of done. |
| `gate` | For `passed` only. `min_score` and `out_of`, or the objective's existing drill rule. Null while `content_ref` is null. |

`task_kind: "lesson"` from [LESSON_PACKAGES.md](../LESSON_PACKAGES.md) is a proposal, not a kind this model requires. A teach node may later point at a lesson id. Until that player exists, the node stays a slot with `content_ref` null.

### Assignment

An assignment is the parent's confirm action. It binds a skill, a path version, a child, and a school-day plan.

| Field | Meaning |
| --- | --- |
| `id` | New id per confirm. |
| `child_id` | The child the wizard already scopes. |
| `skill_id` | The skill the parent picked. |
| `path_id` | Copied from the skill. |
| `path_version` | The version at confirm time. |
| `plan_id` | The school-day plan, or null when the path has any null `content_ref`. |
| `task_ids` | The `plan_tasks` rows created by expansion. Empty when `plan_id` is null. |

Confirming the same child, skill, and local day again updates that assignment in place. It does not append a second copy. A crash halfway through expansion leaves either no plan or the same task ids on retry.

A path with any null `content_ref` does not create a plan and does not call start. [SYNC_AUDIT_2026-07-25.md](../../SYNC_AUDIT_2026-07-25.md) records that a zero-task plan is rejected by `start_school_day`. The K.MG.2 fixture is in that state on purpose.

### Progress

Progress is a function of `activity_events` and task completion, grouped by skill id. The public words match [PARENT_STANDING.md](../PARENT_STANDING.md).

| State | Rule |
| --- | --- |
| `not_started` | No event and no completed node for this skill. |
| `in_progress` | Any node completed, or any qualifying event, and the objective's mastery rule is not met. |
| `mastered` | The objective's existing success criterion is met. Where that criterion says two sessions on different days, one check is not enough. |

There is no fourth public word and no point total. A failed check leaves the skill `in_progress` and reopens `on_check_fail`. A later failed check can move `mastered` back to `in_progress`. Node-level done flags stay inside the day. The standing card reads the skill state only.

## Fixture

The only Goji School pack in this model is `K.MG.2`. It is a catalog fixture. It is not a lesson.

```json
{
	"pack_id": "pack.goji-school.K.MG.2",
	"version": 1,
	"skill": {
		"id": "K.MG.2",
		"pillar": "math",
		"va_sol": ["K.MG.2"],
		"prereq_ids": [],
		"obj_id": null,
		"path_id": "path.K.MG.2"
	},
	"path": {
		"id": "path.K.MG.2",
		"skill_id": "K.MG.2",
		"version": 1,
		"node_ids": [
			"node.K.MG.2.teach",
			"node.K.MG.2.practice",
			"node.K.MG.2.check"
		],
		"on_check_fail": "node.K.MG.2.teach"
	},
	"nodes": [
		{
			"id": "node.K.MG.2.teach",
			"path_id": "path.K.MG.2",
			"role": "teach",
			"task_kind": null,
			"content_ref": null,
			"move_on": "completed",
			"gate": null
		},
		{
			"id": "node.K.MG.2.practice",
			"path_id": "path.K.MG.2",
			"role": "practice",
			"task_kind": null,
			"content_ref": null,
			"move_on": "completed",
			"gate": null
		},
		{
			"id": "node.K.MG.2.check",
			"path_id": "path.K.MG.2",
			"role": "check",
			"task_kind": null,
			"content_ref": null,
			"move_on": "passed",
			"gate": null
		}
	]
}
```

`task_kind` stays null on the fixture until a content pass names an existing kind. The framework tests use a separate fixture whose refs point at task types the school day already accepts. That test fixture is not Goji School and it is not shown to families.

## Parent flow

1. The parent opens the child and the Standing tab. Pillar tiles are the ones in [PARENT_STANDING.md](../PARENT_STANDING.md).
2. The parent picks one skill in one pillar. The fixture demo picks `K.MG.2`.
3. The app shows that skill's path as the node list, in order, with the role of each node. It does not draft lesson text.
4. If any `content_ref` is null, confirm stores the assignment with `plan_id` null. The screen says the pieces are not on the device yet. Start stays disabled.
5. If every `content_ref` is set, confirm expands the nodes into `plan_tasks` on that child's plan, using the existing wizard and the existing kinds. The parent then uses the existing Start school day action.

The parent does not reorder nodes, add a fourth role, or turn one skill into a custom course.

## Child flow

1. When `plan_id` is null, the child has no new school-day rows from this assignment.
2. When a plan exists, Today shows the expanded tasks in `node_ids` order. Tapping a row uses the existing `navigateTo(appId, intent)` deep link described in [MATH_MODULE_TASKS_PLAN.md](../../MATH_MODULE_TASKS_PLAN.md).
3. A `completed` node marks its task done when the existing completion rule for that kind says so. Minutes, a saved journal, or a submitted quiz stay as they are.
4. A `passed` node marks its task done only when the score meets `gate`. Otherwise the task stays open and `on_check_fail` is open again.
5. Release and the household PIN still end the day. A failed gate does not lock the profile.

## Pack and update

A curriculum pack is a set of skill, path, and node records, plus the files those `content_ref` values name once content exists. The K.MG.2 pack at version 1 has the JSON above and no media files.

The device already downloads an image and checks SHA-256 with Ed25519 over the 32-byte digest. Install does not run yet. Both facts are in [TODO.md](../../TODO.md) and [GOJI_COMPUTER_AUDIT_2026-08-19.md](../../GOJI_COMPUTER_AUDIT_2026-08-19.md). The pack uses that verifier. It does not add a second signature scheme.

| Rule | Behavior |
| --- | --- |
| Identity | `pack_id` plus `version`. |
| Verify | The digest of the pack bytes matches the signed digest, or the device rejects the pack. |
| Apply | Not in this model. The existing OTA apply item stays the owner of install. |
| Demo load | Until apply exists, the parent app can read the same JSON as a bundled asset. The bytes are the bytes a later pack will hash. |
| Replace | A higher version replaces catalog rows by id. An assignment stores `path_version` and keeps walking that version. |
| Idempotent | Verifying the same pack twice leaves one copy of each id. A bad signature leaves the previous copy in place. |

Content files, when a later pack has them, ship inside that signed pack. They are not fetched from a third party by the device. That is the offline rule in [CLAUDE.md](../../CLAUDE.md).
