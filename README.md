# Community CRM

A browser-based community CRM coursework project. It links contacts, households, memberships and paid periods, donations, staff tasks, reports, CSV import/export, file activity history, and separate-copy backup restore.

## How to run this app

- **Browser-only option:** Open `index.html` from the project folder (in Edge, right-click and choose **Open with → Microsoft Edge**). Screens and existing data remain viewable, but donation/task changes are disabled because server authorization requires `start-crm.bat`.
- **Server-validation option (Windows):** Install Python 3, then double-click `start-crm.bat`. It starts `server.py` and opens `http://127.0.0.1:8765` in your browser. Contact and household name values are trimmed and blank/space-only names are rejected by the local server before the existing browser storage save happens.
- **Files:** `index.html` remains available on GitHub and can still be opened directly. `server.py` and `start-crm.bat` are optional additions; no npm packages are required.
- **Storage:** Both options continue to use the same browser `localStorage` data for this browser profile. The local server validates names; it does not add a central database or server-side user authorization.
- **Test accounts:** Choose Admin, Staff, or Viewer on the sign-in screen. All demo roles use the fake passcode `demo123`.

## Load the classroom practice data

The app's explicit **Reset sample data** action loads the supplied, fake classroom baseline into the current browser. It is a separate, confirmed action; normal startup loads saved `communityCRM.v2` data and does not reseed over existing work. Export a JSON backup before resetting data you need to keep.

The `data/` folder includes the original classroom practice filenames and values:

- `crm-classroom-test-data.json` — 30 contacts, 5 households, 20 memberships, 20 donations, and 15 manual tasks.
- `contacts-clean.csv`, `contacts-messy.csv`, `contacts-corrected.csv`, and `contacts-existing.csv` — CSV import cases.
- `README.txt` — practice-data notes.

## CRM 6 integrated workflow

Use **October 15, 2026** in the Memberships and Reports date controls. Sign in as Staff, then:

1. In Contacts, add ID `C900`, first name `Test`, last name `Builder`, email `test900@example.com`, no household, and email permission **Allowed**.
2. In Memberships, add ID `M900`, select C900, choose **One person ($35)**, set start date to `2026-10-15`, payment status **Paid**, and payment code `FINAL-M900`. The end date is calculated as `2027-10-15`.
3. Use Renew on M900. Enter payment code `FINAL-R900`, amount `35`, status **Paid**, and payment date `2026-10-15`. The second paid period is `2027-10-15` through `2028-10-15`; the first period and its payment remain in membership history.
4. In Donations, add ID `D900`, donor C900, amount `12`, date `2026-10-15`, campaign `Campaign B`, payment method Cash, and payment code `FINAL-D900`.
5. The donation creates a Thank-you task due `2026-10-22`. In Tasks, mark that task Complete.
6. In Donations, set Campaign to `Campaign B` and leave the date range covering 2026. Export the visible donations CSV. It should include 11 rows totaling **$212**.

After the workflow, the baseline donation total is **$367** ($155 Campaign A and $212 Campaign B), with 13 active memberships and 15 people covered. Reusing `FINAL-M900`, `FINAL-R900`, or `FINAL-D900` is rejected as a duplicate payment code. Closing and reopening the same browser preserves the saved records.

## Import and exports

Open Contacts → Import contacts from CSV. Choose a file, select Preview, review each row, and select Import only when there are no Error rows. Cancel clears the preview without saving. The CSV headers can be reordered but must contain exactly: `contact_id,name,email,phone,household,tags,notes,email_opt_in`.

The parser supports quoted commas and doubled quotes. Existing IDs are classified as Duplicate before validating the other columns; duplicate new IDs in the same file are errors on every matching row. Emails are valid and unique without case sensitivity. Blank email permission is false. If any row is an error, the whole file is blocked. Contacts and new households are staged together and saved in one localStorage operation. Replaying a corrected file adds zero contacts and records another import event.

Reports recalculate from saved records using their selected date and inclusive donation date-range controls. The October 15, 2026 classroom baseline is **$355 donations** ($155 Campaign A and $200 Campaign B), **12 active memberships**, **14 covered people**, and **6 overdue jobs**. Voided and archived donations are excluded.

CSV export buttons sit beside each corresponding on-screen table and export the rows and visible values for its current filters. The email permission list contains only active contacts with an email address and permission set to Yes. Admins can enable or disable Viewer CSV export. Viewer imports are always blocked. Import and download history records the user, time, filename, and row count.

## Backups and roles

- **Admin:** Can manage records and settings, change plan prices, control Viewer CSV export, and download/restore JSON backups. Price changes apply to new sales and renewals; earlier payment amounts remain in history.
- **Staff:** Can manage records, import contacts, and export CSV files.
- **Viewer:** Read-only. CSV export works only when an Admin enables it. Viewers cannot import.

The JSON backup includes contacts, households, memberships and all stored periods, membership payments/history, donations, tasks, audit history, file history, and settings. Restore writes the full data into a separate `communityCRM.restoreCopy.v1` localStorage copy and does not replace the original. The Admin can download that restored copy separately.

## Data storage and security limitation

The app stores records in the current browser's `localStorage` under `communityCRM.v2`; records do not sync across devices. When run through `start-crm.bat`, the local server issues an HttpOnly role session and checks donation/task create, edit, void, complete, archive, and restore requests before the browser writes those changes. Admin and Staff are allowed; Viewer and signed-out requests are rejected. The shared `demo123` passcode is intentionally a coursework shortcut. This is not production authentication or a central server database; someone with direct access to the browser profile can still alter localStorage. Do not use real personal, donor, or payment information.
