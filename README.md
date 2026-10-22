# Community CRM — Classroom Project

## Start the app
1. Extract the ZIP file.
2. Open `index.html` in a modern browser (Chrome, Edge, Firefox, or Safari).
3. Sign in with the demo credentials:
   - Username: `admin`
   - Password: `community123`
4. Navigate with the left menu. Sample records are preloaded so every page has something to demonstrate.

No install or build step is required. The app is a single-page HTML/CSS/JavaScript project.

## Included rubric areas
- **CRM 1 — Contact Starter:** create, read, update, delete, search, archive, status filter, required fields, email format and duplicate-email checks.
- **CRM 2 — Contacts and Login:** demo sign-in, contact search, household records and assignments, contact history, keyboard labels and focus indicators.
- **CRM 3 — Memberships and Renewals:** plans, start/renewal dates, one-year date default, renewal-date validation, due-soon and overdue indicators.
- **CRM 4 — Donations and Tasks:** donations, methods/funds/receipts, donation summaries, task priorities/due dates/status and complete action.
- **CRM 5 — Import and Reports:** CSV import, header validation, required names, email validation, duplicate-email skipping, CSV export, JSON backup and summary reports.
- **CRM 6 — Finish and Test:** responsive layout, empty states, activity log, confirmation before deletion/reset, input validation, data persistence, comments and test plan.

## Data storage and code map
- `seedDB()` creates sample data in a JavaScript object.
- `loadDB()` reads saved JSON from browser `localStorage` at key `communityCRM.v1`.
- `db` is the in-memory state object with `contacts`, `households`, `memberships`, `donations`, `tasks`, and `activity` arrays.
- `saveDB()` writes the state back to localStorage.
- `render()` and the `*Page()` functions display current data.
- `openForm()` builds forms from schemas in `fieldsFor()`.
- The record form submit handler validates and updates the correct array.
- `logActivity()` records major changes; contact history is stored on each contact.
- Memberships, donations and tasks refer to contacts through `contactId`.

## Important limitations
This is a front-end teaching demo. The demo login is hard-coded and is **not secure authentication**. localStorage is local to one browser profile/device, is not encrypted or shared across users, and can be cleared. Do not enter real sensitive personal, donor, or payment data. A production CRM would need a secure backend, password hashing, authorization, server-side validation, audit controls and backups.

## Manual test plan — record your actual results
1. **Login:** enter wrong credentials; verify a helpful error. Sign in with the demo credentials.
2. **Required fields:** create a contact without first or last name; verify the browser blocks the save.
3. **Email validation:** enter an invalid email; verify it is rejected.
4. **Duplicate contact:** save two contacts with the same email; verify the second is rejected.
5. **CRUD and persistence:** add a contact, edit it, refresh the browser and search for it.
6. **Archive:** archive a contact, filter to Archived, then restore it if desired.
7. **Household:** assign contacts to a household and verify the household contact count changes.
8. **Membership date:** create a membership and confirm the renewal date defaults to one year after the selected start date; test renewal earlier than start.
9. **Donation totals:** add a donation and verify the dashboard/report total increases by the donation amount.
10. **Task:** create a task, mark it complete, and filter to Complete.
11. **CSV import:** import a CSV with one new contact, one duplicate email, and one row missing a name. Verify import counts.
12. **CSV export and backup:** export contacts and download a JSON backup.
13. **Empty search:** search for a string with no matches and verify the empty-state message.
14. **Responsive view:** resize the browser to a narrow/mobile width and verify navigation/tables remain usable.
15. **Reset:** export a backup first, reset sample data, and verify sample records return.

Record pass/fail and any issues you discover. Do not claim tests passed until you run them yourself.

## Suggested AI assistance statement
Personalize this so it truthfully reflects what you did:
“I used AI to help plan the CRM pages, draft code comments explaining JavaScript state and browser storage, and create a manual test plan. I reviewed and tested the app and made these changes myself: [describe your actual changes].”
