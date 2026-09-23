# How other systems turn a skill into a path

Status: research note. Each source link was fetched on 2026-09-23.

A parent on Goji should pick one skill and get an ordered path the child can walk. The path is teach, then practice, then check, which is already the rule in [VISION.md](../VISION.md) and [PRACTICES.md](../PRACTICES.md). This note records ten systems that already do a piece of that job, what to copy, and what to leave behind.

The slice worth copying is small. Keep a stable skill id, a prerequisite edge, an ordered path of three roles, one fail edge back to teach, a parent assignment that expands into the school day the app already runs, and a signed pack the device can verify. Leave the rest.

Wire names below are the ones this repo already documents. An implementer re-reads `goji_cloud/SYNC_API.md` before changing the wire.

## Kolibri lessons and channels

Kolibri is an offline learning server. A coach builds a lesson by picking resources out of channels that are already on the device, then assigns that lesson to a class or a group. Learners open the lesson from their class list. Channels import and update as packs. The coach docs warn that updating a channel can move a resource and break a lesson that points at it.

[Coach lessons](https://kolibri.readthedocs.io/en/latest/coach/lessons.html). [Channels and resources](https://kolibri.readthedocs.io/en/latest/manage/resources.html). [Learn](https://kolibri.readthedocs.io/en/latest/learn.html).

**What to borrow.** Assignment points at content the device already holds. A path is an ordered list of those pointers, not a download at the moment the parent taps assign. Pack updates must not silently retarget a pointer. Pin each node to a content id and a version.

**What to skip.** Kolibri Studio, channel tokens, facilities, classes, and groups. Goji is one family and one computer. A parent is not a facility coach.

## Moodle competencies and learning plans

Moodle splits a competency framework from a learning plan. The framework is the tree of competencies, with a rule that can mark a parent complete when its children are complete. A learning plan template is a chosen set of those competencies. Assigning the template to a learner creates that learner's plan. Evidence of prior learning is a separate record from the plan.

[Competency frameworks](https://docs.moodle.org/500/en/Competency_frameworks). [Learning plans](https://docs.moodle.org/39/en/Learning_plans).

**What to borrow.** Three records that do not collapse into one. The catalog (what skills exist), the path template (the ordered nodes for one skill), and the assignment (this child, this day). Completing every node can mark the skill checked. The skill is not itself a node.

**What to skip.** Moodle scales, CSV taxonomy import, cohorts, and course-activity linking. Goji already has objective ids and a Virginia coverage table. A second competency product on top of `obj.*` would split the catalog.

## 1EdTech CASE associations

CASE is a way to exchange a standards document as data. A `CFItem` is one competency. A `CFAssociation` links two items. The type `isChildOf` builds the tree. The type `precedes` says the origin comes before the destination in order. A package can carry items and associations without carrying the teaching material.

[CASE 1.1 specification](https://www.imsglobal.org/spec/case/v1p1). [Information model](https://standards.1edtech.org/case/specifications/standards/v1p1/im).

**What to borrow.** Two edge types are enough. `isChildOf` is the strand and pillar tree already implied by `skills/` and `subjects/`. `precedes` is the prerequisite column already on objectives, plus the order of nodes inside one path. Give every skill and every node a stable id so a later pack can refer to it.

**What to skip.** A CASE server, GUIDs for their own sake, rubrics, and certification. Goji ids stay `obj.*`, `lesson.*`, `quiz.*`, and `K.MG.2` style Virginia codes. The association idea is the data. The REST service is not.

## Khan Academy mastery levels

Khan tracks each skill as Not started, Attempted, Familiar, Proficient, or Mastered. An exercise score moves the level. A later mixed quiz can move it up or down. Course and unit mastery are rollups of those skill levels. Teachers can assign a unit and filter reports to assigned skills. Khan's own write-up says a session is better spent taking two skills to proficient than grazing more skills at familiar.

[How mastery levels work](https://support.khanacademy.org/hc/en-us/articles/5548760867853--How-do-Khan-Academy-s-Mastery-levels-work). [Course and unit mastery](https://support.khanacademy.org/hc/en-us/articles/115002552631-What-are-Course-and-Unit-Mastery). [Skills to proficient](https://blog.khanacademy.org/why-khan-academy-will-be-using-skills-to-proficient-to-measure-learning-outcomes/).

**What to borrow.** The parent assigns a skill, and the report can be limited to that assignment. A later check can lower a skill that looked finished. Goji already has this instinct in [PRACTICES.md](../PRACTICES.md). A quiz gate is not the same as a later mastery test.

**What to skip.** Five public levels and mastery points. [PARENT_STANDING.md](../PARENT_STANDING.md) already shows mastered, in progress, and not started. Those three words stay. Khan's exercise generator and course-challenge machinery stay out.

## ALEKS knowledge checks and Ready to Learn

ALEKS starts with a knowledge check, then shows a pie of topics in three piles. Learned means the student practiced the topic. Mastered means a later knowledge check proved it with no help. Ready to Learn means the prerequisites are in place, so the topic is a legal next step. The student path is that ready set, not the whole course at once.

[Knowledge checks overview (PDF)](https://www.aleks.com/resources/ALEKS_Knowledge_Checks_Overview_for_Students.pdf). [Student module guide (PDF)](https://www.aleks.com/manual/pdf/student-account-independent-use.pdf).

**What to borrow.** A skill is offered when its prerequisites are met, or when the parent assigns it anyway. Learned and mastered stay distinct, which matches a lesson check versus the two-session gate already written on Goji objectives. Placement quizzes in [ASSESSMENT.md](../ASSESSMENT.md) are the knowledge check. They pick a starting skill. They do not rebuild the path every night.

**What to skip.** The pie chart, the adaptive item selector, and a knowledge-state model over every subset of topics. The prerequisite column is a list of ids. The ready set is "every prerequisite is mastered, or the parent overrode that."

## Canvas Mastery Paths

In Canvas, a graded source item releases the next items by score band. A high score can release harder work. A low score can release a review. Conditional items stay hidden until the source is graded. The path is authored by a person as a few ranges, not inferred by a model.

[What are Mastery Paths?](https://community.instructure.com/en/kb/articles/662760-what-are-mastery-paths)

**What to borrow.** One branch, on the check node only. Pass moves to the next node, or marks the skill checked if this was the last node. Fail returns to the teach node named on the path. [PRACTICES.md](../PRACTICES.md) already requires a specific re-teach, not a vague retry.

**What to skip.** Three score ranges, student choice among conditional items, and a general rules engine. Goji has one fail edge. Release and the household PIN still end the day, as [PARENT_APP_PRODUCT.md](../../PARENT_APP_PRODUCT.md) already requires. A gate never traps the child.

## cmi5 assignable units

cmi5 packages a course as blocks and assignable units. Each unit has a `moveOn` value that tells the host when the unit is satisfied. The useful values here are Passed, Completed, and CompletedAndPassed. If `moveOn` is missing, it defaults to NotApplicable, and the unit is satisfied at registration, before the learner opens it. The unit reports completion. The host decides whether that is enough to move on.

[cmi5 specification](https://github.com/AICC/CMI-5_Spec_Current/blob/quartz/cmi5_spec.md). [Best practices](https://aicc.github.io/CMI-5_Spec_Current/best_practices/).

**What to borrow.** Every node names its move-on rule in data, and the default is not "done." A teach node moves on when the child finishes it. A check node moves on only when the score meets the gate. The lesson package posts a result. The school-day task decides whether the row is done. That split is already sketched for lessons in [LESSON_PACKAGES.md](../LESSON_PACKAGES.md).

**What to skip.** xAPI learning-record stores, launch state documents, and cmi5 course XML. Goji already has `activity_events`. A new statement log would duplicate them.

## IXL skill plans and suggested skills

IXL publishes skill plans aligned to textbooks and to state standards. A teacher pins a plan. Students see the pinned plan and can be sent specific suggested skills. A SmartScore goal of 80, 90, or 100 can sit on those suggested skills. The SmartScore is a proprietary running score, not a percent correct.

[Skill plans](https://www.ixl.com/skill-plans). [Teacher's user guide (PDF)](https://www.ixl.com/userguides/us/IXLUserGuide.pdf). [SmartScore goals](https://blog.ixl.com/2025/04/28/set-smartscore-goals-for-your-suggested-skills/).

**What to borrow.** The parent verb is "assign this skill," and the child sees that assignment rather than the whole catalog. Virginia rows in `skills/` are the standards list. A path hangs off one row. The parent does not browse a thousand loose drills to build a day.

**What to skip.** SmartScore, medals, and an endless generated question stream. Goji checks stay countable gates already written on objectives, such as 8 of 10 or 90 percent on 20 problems across two days.

## Oppia skills

An Oppia skill has a description, a concept card (review material the learner can open when stuck), misconceptions with feedback, and rubrics by difficulty. Lesson planning tells authors to list prerequisite skills, including skills from earlier lessons, and to use them for a short review before the new lesson. A skill can exist unpublished, and a published skill can still be unused until a topic includes it.

[Creating a skill](https://oppia-user-guide.readthedocs.io/en/latest/admins/skills.html). [Planning a lesson](https://oppia-user-guide.readthedocs.io/en/latest/admins/guide.html).

**What to borrow.** Prerequisites are ids, and a review of those ids is allowed as the first node when the path author puts it there. Misconceptions already belong on the strand, in [PRACTICES.md](../PRACTICES.md). The check's wrong answers should name those misconceptions. A skill with no path is a legal catalog row. `skills/math-k.md` already has gap rows in that state.

**What to skip.** The exploration editor, concept-card publishing workflow, and difficulty rubrics for question writers. Goji lesson bodies stay in the curriculum lead's files. This build does not add an authoring studio.

## Open edX course outline

Open edX stores a course as a tree. A chapter holds sequentials. A sequential holds verticals. A vertical holds components such as HTML or a problem. The outline is structure. The component files are the material. Studio's hierarchy is fixed even though the raw format is more flexible.

[OLX course building blocks](https://docs.openedx.org/en/latest/educators/olx/organizing-course/course-structure-overview.html). [Courseware structure](https://docs.openedx.org/en/latest/educators/olx/organizing-course/course-xml-file.html).

**What to borrow.** The path file lists node ids in order. Each node points at a component id (`lesson.*`, `quiz.*`, a math module id, a book id). The path file does not contain the component. Replacing a component does not require rewriting the path if the id is stable.

**What to skip.** Chapters, courses, XBlocks, and Studio. One skill expands to one short path. It does not expand to a semester course.

## What this means for Goji

The ten systems agree on a split that Goji is close to already. A catalog names skills. A template orders the work for one skill. An assignment gives that template to one child. Progress is evidence against a gate. Updates arrive as a pack of ids, and old pointers keep their version.

Goji's catalog is `skills/` plus `obj.*` in `subjects/`. Goji's assignment channel is the school day in [PARENT_APP_PRODUCT.md](../../PARENT_APP_PRODUCT.md). Goji's evidence is `activity_events`. Goji's pack verifier already checks a SHA-256 digest with Ed25519, and install is still open in [TODO.md](../../TODO.md). The engineering plan in [PLAN.md](./PLAN.md) fills the missing template, the expansion into `plan_tasks`, and the pack manifest. It does not fill lesson text. Shapes are in [MODEL.md](./MODEL.md).
