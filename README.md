# Community CRM

A single-file browser demo CRM for community contacts, households, memberships, donations, tasks, reporting, archive/restore, and change history.

## Run the app
1. Open [index.html](index.html) in Edge, Chrome, Firefox, or Safari.
2. Sign in with one of the demo roles and passcode `demo123`.
3. Try adding/editing a contact, searching, archiving/restoring, exporting a CSV/JSON backup, and importing a CSV.

## Demo accounts
- **Admin demo** — full demo UI access, including reset sample data.
- **Staff demo** — create, edit, archive, restore and import records.
- **Viewer demo** — read-only interface.

These role controls are deliberately a **coursework simulation only**. Because this app runs entirely in the browser, a user can bypass them using developer tools. It has no server-side authentication, server authorization, shared database, or secure audit trail. Never enter real sensitive personal, donor, or payment data.

## Implemented features
- Dashboard totals for contacts, households, active memberships, donations, and open tasks.
- Contact records with required first/last name, email format/uniqueness validation, phone, tags, notes, email permission, and optional household assignment.
- Household records and household relationship display.
- Membership records, date validation, one-year renewal action, and status.
- Donation records and totals grouped by fund.
- Task records and status.
- Search across record fields, active/archived/all filters, and clear no-results feedback.
- Archive/restore instead of hard-delete, plus a capped local change-history log with timestamp, demo user, action, record type and ID.
- CSV contact import with header validation, malformed/invalid-row rejection, and duplicate skipping; CSV export for the current section and JSON backup export.
- Resettable sample data: 20 contacts and 5 households, plus example membership, donations and task.
- Responsive layout, visible labels, keyboard focus outlines, skip link, status messages, and confirmation prompts for archive/reset.
- Comments/documentation describing data storage and the code paths that modify it.

## Where data is stored and changed
- `db` is the in-memory JavaScript object containing arrays for contacts, households, memberships, donations, tasks, and audit entries.
- `loadDB()` reads JSON from this browser's `localStorage` using key `communityCRM.v2`. It can migrate basic records from the earlier `communityCRM.v1` key.
- `submitForm()` validates fields and updates or inserts records; duplicate emails, invalid emails, invalid dates, and invalid donation amounts are rejected before saving.
- `persist()` writes the current state to `localStorage` and re-renders the interface. A browser storage failure shows a message.
- `log()` records local audit entries for create/edit/archive/restore/import/login/reset events.
- `render()`, `renderForm()`, and `visibleRows()` display the dashboard, form, and filtered records.
- Browser-local storage is scoped to a browser profile/device. Clearing browser data may remove it; export a backup before resetting or clearing data.

## Testing
Use [TEST_RESULTS.md](TEST_RESULTS.md) as a test log. Run each test in your browser and enter actual results; do not claim tests passed unless you have personally verified them. Some rubric requirements such as real secure multi-user login, server-enforced permissions, and database transactions cannot be genuinely satisfied by a static browser-only app; these limitations are documented honestly.

## Rubric checklist
- [x] Multiple CRM sections, visible navigation, data persistence, sample data, documentation.
- [x] Contact validation and duplicate prevention; household assignment; tags and email permission.
- [x] Search, active/archive filters, archive/restore, local audit history.
- [x] Membership renewal, donation report, tasks, CSV import/export and JSON backup.
- [x] Keyboard focus indicators, labels, status messages, responsive layout.
- [!] Login and roles are a client-side demonstration, not production security.
- [ ] Manual browser testing and actual results still need to be completed.

## AI assistance
If your assignment requires an AI assistance statement, personalize it to truthfully describe the help you used and the changes you personally made.
