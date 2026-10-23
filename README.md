# Community CRM

A single-file browser CRM coursework demo. The main navigation now has eight distinct pages: **Dashboard, Contacts, Contact Details, Memberships, Donations, Tasks, Reports, and Login / Settings**.

## Run it
1. Open [index.html](index.html) in Edge, Chrome, Firefox, or Safari.
2. Sign in with Admin, Staff, or Viewer. All demo roles use passcode `demo123`.
3. Use the eight navigation pages to explore the application.

## Page guide
- **Dashboard:** summary metrics, recent activity, open tasks, and a shortcut to Contacts.
- **Contacts:** add/edit contacts, validate required names and email format, prevent duplicate email addresses, search/filter, archive/restore.
- **Contact Details:** select a contact to view their profile, household, tags, email permission, related memberships, donations, and tasks; open the contact editor from the profile.
- **Memberships:** create/edit/search/archive membership records, validate renewal dates, and review plan/status.
- **Donations:** create/edit/search/archive donations and view donation entries.
- **Tasks:** create/edit/search/archive tasks and track due dates, assignees, related contacts, and status.
- **Reports:** summary metrics, donation totals by fund, membership status breakdown, and CSV/JSON export.
- **Login / Settings:** demo login roles, sign out, export a JSON backup, reset sample data, and view local change history.

## Sample data
The app initializes 20 sample contacts, 5 households, one membership, two donations, and one task. These are fictional records.

## Data storage and code notes
- `db` is the in-memory JavaScript data model with `contacts`, `households`, `memberships`, `donations`, `tasks`, and `audit` arrays.
- `load()` reads the `communityCRM.v2` JSON key from browser `localStorage`.
- `submitRecord()` validates and creates/updates contact, membership, donation, and task records.
- `persist()` writes changes and re-renders the app.
- `log()` appends local change-history entries.
- `renderDashboard()`, `renderContactProfile()`, `renderReports()`, and `renderSettings()` power the distinct pages.
- `archive()` marks records archived rather than permanently deleting them.
- `exportCSV()` and `exportJSON()` create local download files.

## Important limitations
This is a browser-only demonstration, not a production CRM. The login and role controls are client-side UI simulations, not secure authentication or server-enforced permissions. Data is stored in the current browser's localStorage and does not sync across devices. The audit log can be edited by someone with browser developer tools. Do not enter real sensitive personal, donor, or payment information.

## Testing
Use [TEST_RESULTS.md](TEST_RESULTS.md) to manually verify page navigation and core workflows. Record actual results after running the tests; don't mark tests passed without checking them.
