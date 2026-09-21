# Child detail tabs

Child detail splits one child's day into Today, Standing, and Activity so the mock phone ends instead of stacking every section.

## Sub-features

- `tab-today` shows today's plan tasks.
- `tab-standing` shows the three-pillar standing view.
- `tab-activity` shows the timed activity list.

## How to get to it (user POV)

- Scroll to the Child detail slot.
- Choose **Today**, **Standing**, or **Activity** on that phone's tab list.

## Driving it with verify-goji-docs

Preconditions:

- Doctor reports both page titles.
- Zoom is closed.

- **Open Child detail.** Load the studio and find `.slot[data-title="Child detail"]`. Run `scripts/verify drive studio-child-tabs`.
- **Today default.** The Today tab has `aria-selected="true"` and the phone shows `Today's plan · 3 of 5 done`.
- **Standing.** Choose **Standing**. The driver clicks `button[data-pane="p-standing"]`. That tab has `aria-selected="true"`, `#p-standing` is visible, and the phone shows `Where Eli stands`.
- **Activity.** Choose **Activity**. The driver clicks `button[data-pane="p-activity"]`. That tab has `aria-selected="true"` and the phone shows `Looked up 4 words`.
- **Proof.** `before.png` is Today. `after.png` is Standing with `Where Eli stands` visible. `state.txt` records each `aria-selected` value.

## Gotchas

- Other phones also have buttons. Scope queries to `.slot[data-title="Child detail"]`.
- Tab panels share the phone. Assert the selected tab and the panel heading together.
- The slot note talks about the live Flutter screen. That note is design rationale, not the mock's current tab state.
