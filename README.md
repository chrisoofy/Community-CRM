# Community CRM

A single-file browser demo for managing basic community records. No installation or build step is needed.

## Run it
1. Open [index.html](index.html) in a current browser (Chrome, Edge, Firefox, or Safari).
2. Use the tabs to manage Contacts, Memberships, Donations, and Tasks.
3. Use **Export backup** to download a JSON copy of the browser's current data.

## Features currently implemented
- Add, edit, search, and delete contacts, memberships, donations, and tasks.
- Basic required-field validation and browser email-format validation.
- Prevent duplicate contact email addresses.
- Validate that a membership renewal date is not earlier than its start date.
- Dashboard counts and donation total.
- JSON backup export.
- Responsive layout and code comments explaining browser storage.

## Where data is stored
- `db` is the in-memory JavaScript state object with `contacts`, `memberships`, `donations`, and `tasks` arrays.
- `loadDB()` reads JSON from browser `localStorage` using the key `communityCRM.v1`.
- `saveDB()` writes updated state back to localStorage after a successful change.
- `render()` updates the dashboard and current record table.
- `renderForm()` creates the form for the selected section, and `submitForm()` validates and saves records.

Data is local to the browser profile and device. Clearing browser data can remove it. This is a coursework demo, not a production CRM; it has no secure user authentication, server-side storage, or access control. Do not store real sensitive personal, donor, or payment information.

## Manual test checklist
See [TEST_RESULTS.md](TEST_RESULTS.md). Run each test yourself and fill in actual results; do not mark tests as passed before verifying them.

## Rubric note
This is a basic starter implementation, not a guarantee of full rubric completion. Compare the current features against your instructor's CRM 1–6 rubric and add/test any missing requirements before submitting.

## AI assistance
If your assignment requires an AI assistance statement, personalize it so it truthfully describes the help you used and the changes you personally made.
