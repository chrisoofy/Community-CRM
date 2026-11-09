# Community CRM

A browser-based community CRM coursework project with contacts, households, memberships, donations, tasks, reports, CSV import/export, and file activity history.

## How to run this app

- **Tools needed:** Microsoft Edge, Google Chrome, Firefox, or another modern browser.
- **Install command:** None. This project has no package manager or external runtime dependency.
- **Start command:** Open `index.html` from the project folder. In Edge on Windows, right-click `index.html` and choose **Open with → Microsoft Edge**.
- **Browser address:** The local file address will look like `file:///.../Community-CRM/index.html`.
- **Demo sign-in:** Select Admin, Staff, or Viewer. The demo passcode for each is `demo123`.

## Practice data

The `data/` folder contains the supplied classroom practice files with their original filenames and sample IDs:

- `crm-classroom-test-data.json` — 30 contacts, 5 households, 20 memberships, 20 donations, and 15 manual tasks.
- `contacts-clean.csv`, `contacts-messy.csv`, `contacts-corrected.csv`, and `contacts-existing.csv` — the four contact import test files.
- `README.txt` — practice-data notes.

A new browser profile starts with the classroom dataset mapped into the CRM's internal fields. On first use, the app stores this initial dataset in that browser's `localStorage`. Normal startup does not replace existing saved browser data. **Reset sample data** replaces the current browser's data with the supplied classroom baseline; export a backup first if you need to keep changes.

## Contact CSV import

Open **Contacts → Import contacts from CSV**. Choose a CSV, select **Preview**, review each row as **New**, **Duplicate**, or **Error**, then select **Import**. Cancel clears the preview without saving. Headers can be reordered but must contain exactly: `contact_id,name,email,phone,household,tags,notes,email_opt_in`.

The parser handles quoted commas and doubled quotes. Saved IDs are skipped before other row validation, IDs are case-sensitive, duplicate new IDs in a file are errors on every matching row, and emails are checked for validity and uniqueness without case sensitivity. Blank email permission is treated as false. If any row is an error, the whole file is blocked. The app stages new contacts and households together and writes them in one localStorage operation. A repeated corrected file adds zero contacts and records the import attempt.

## Reports and downloads

The Reports page calculates totals from saved records. Its default practice date is **October 15, 2026**. With the supplied practice data, the expected starting values are:

- Donations: **$355 total**, **$155 Campaign A**, **$200 Campaign B**
- Active memberships: **12**
- People covered: **14**
- Overdue manual tasks: **6**

Change the report date or donation date range to recalculate. Donation start and end boundaries are inclusive; voided and archived donations are excluded. Overdue tasks must still be open and have a due date earlier than the selected date.

CSV export buttons are beside the matching contact, membership, donation, and task lists and export the records and displayed columns for the current table filters. The email permission list contains only active contacts with an email address and permission set to Yes. Admins can enable or disable Viewer CSV exports in Login / Settings. Viewer imports are always blocked. Imports and downloads are listed with the signed-in demo role, time, filename, and row count.

## Roles and data storage

- **Admin:** Can manage records, change the Viewer CSV export permission, and use JSON backup/restore.
- **Staff:** Can manage records, import contacts, and export CSV data.
- **Viewer:** Read-only. CSV exports work only when an Admin enables them. Viewers cannot import or change settings.

The app stores records in the current browser's `localStorage` under `communityCRM.v2`. Data does not sync across browsers or devices.

## Important limitation

This repository is a **single-file, browser-only demonstration**. Sign-in and role checks run in client-side JavaScript; there is no server, server-side request authorization, central database, or secure authentication. A person with browser developer tools can bypass client-side restrictions or edit local data. Do not store real personal, donor, payment, or other sensitive information in this demo.
