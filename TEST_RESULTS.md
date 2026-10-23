# Community CRM — Manual Test Log

Run these tests in a browser. Record actual outcomes and mark Pass/Fail only after performing each test.

| # | Test | Expected result | Actual result | Pass/Fail |
|---:|---|---|---|---|
| 1 | Login success | Admin / Staff / Viewer signs in with `demo123` |  |  |
| 2 | Login failure | Incorrect passcode shows error |  |  |
| 3 | Eight-page navigation | Dashboard, Contacts, Contact Details, Memberships, Donations, Tasks, Reports, and Login / Settings each open as separate pages |  |  |
| 4 | Dashboard summary | Contact, household, membership, donation, and task totals appear |  |  |
| 5 | Add contact | Valid contact saves and appears in directory |  |  |
| 6 | Required contact fields | Missing first or last name is rejected |  |  |
| 7 | Invalid email | Malformed email is rejected |  |  |
| 8 | Duplicate email | Existing email cannot be added to another contact |  |  |
| 9 | Contact search/filter | Search and Active/Archived/All filter show matching records |  |  |
| 10 | Contact details page | Select contact and see profile plus related memberships, donations, tasks |  |  |
| 11 | Edit from contact profile | Edit contact button opens contact editor |  |  |
| 12 | Household display | Assigned household appears in contact details |  |  |
| 13 | Membership create/edit | Membership saves and appears in Memberships page |  |  |
| 14 | Membership date validation | Renewal date earlier than start date is rejected |  |  |
| 15 | Donations | Valid donation saves; donation values display as currency |  |  |
| 16 | Reports page | Totals, donations by fund, and membership status breakdown appear |  |  |
| 17 | CSV report export | Reports export downloads a CSV |  |  |
| 18 | Task management | Task saves and status can be updated to Complete |  |  |
| 19 | Archive and restore | Archived record disappears from Active and can be restored |  |  |
| 20 | Change history | Create/edit/archive/restore actions appear in local audit history |  |  |
| 21 | JSON backup | JSON backup downloads and contains the app's data arrays |  |  |
| 22 | Section CSV export | CSV files download for contacts, memberships, donations, and tasks |  |  |
| 23 | Settings logout | Sign out returns to the login screen |  |  |
| 24 | Viewer role | Viewer sees read-only controls |  |  |
| 25 | Admin reset | Admin can confirm reset and sample records return |  |  |
| 26 | Browser persistence | Refreshing the page keeps saved records in the same browser profile |  |  |
| 27 | Keyboard accessibility | Tab navigation reaches controls and focus is visible |  |  |
| 28 | Narrow viewport | Pages remain usable on a narrow browser window |  |  |

## Security and storage caveats
- Demo login and roles are client-side only, not secure authentication or server-enforced authorization.
- Data lives in browser localStorage, not a shared database.
- The audit log is local and not tamper-proof.
