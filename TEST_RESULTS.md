# Community CRM — Manual Test Log

Run these tests in the browser using `index.html`. Enter the actual result and Pass/Fail only after performing each test. Do not submit the template with invented results.

| # | Test | Steps | Expected result | Actual result | Pass/Fail |
|---:|---|---|---|---|---|
| 1 | Login success | Sign in with Admin demo / `demo123` | CRM dashboard opens and role is shown |  |  |
| 2 | Login failure | Enter a wrong passcode | Helpful error; app remains signed out |  |  |
| 3 | Logout | Sign in, then select Log out | CRM is hidden and login form returns |  |  |
| 4 | Read-only role | Sign in as Viewer demo | Editing controls are not offered |  |  |
| 5 | Required contact fields | As Staff/Admin, submit a contact with blank first or last name | Save blocked with validation message |  |  |
| 6 | Email validation | Try malformed email such as `abc` | Save blocked |  |  |
| 7 | Duplicate email | Add an email already on another contact | Duplicate rejected; no second record |  |  |
| 8 | Contact create/edit | Create a contact, edit phone, save | Only selected record changes |  |  |
| 9 | Persistence | Refresh browser after adding a test contact | Contact remains in this browser profile |  |  |
| 10 | Household validation | Create household, assign contact; try nonexistent household via UI | Valid household assignment saves; invalid value cannot be selected |  |  |
| 11 | Search match | Search for a known name or email | Matching record appears |  |  |
| 12 | Search no match | Search for a unique nonexistent phrase | Helpful empty state appears |  |  |
| 13 | Clear search | Select Clear search | Query clears and active view returns |  |  |
| 14 | Archive contact | Archive a test contact and confirm | Contact disappears from active view but remains in archived view |  |  |
| 15 | Restore contact | Open archived view and restore the test contact | Contact returns to active view |  |  |
| 16 | Audit history | Create, edit, archive or restore a record, then open Change history | Local action, user, time, type and ID are listed |  |  |
| 17 | Membership date validation | Set renewal date before start date | Save is rejected |  |  |
| 18 | Membership renewal | Use Renew +1 year on a membership | Renewal date advances one year and status is Active |  |  |
| 19 | Donation total/report | Add a donation with a known amount/fund | Dashboard total and fund report update |  |  |
| 20 | Invalid donation | Enter zero or negative donation amount | Save rejected |  |  |
| 21 | Task completion | Edit a task and set status Complete | Task shows Complete; open task count decreases |  |  |
| 22 | CSV import valid rows | Import a CSV with firstName,lastName,email and a valid contact | New contact is added |  |  |
| 23 | CSV duplicate | Import a contact whose email already exists | Duplicate is skipped and count is reported |  |  |
| 24 | CSV invalid row | Import a row missing name or with malformed email | Invalid row rejected and counted |  |  |
| 25 | CSV bad header | Import a CSV without required headers | Import fails with a clear message |  |  |
| 26 | CSV export | Select Export current section CSV | A CSV file downloads with header row |  |  |
| 27 | JSON backup | Select Export JSON backup | JSON backup downloads and contains CRM arrays |  |  |
| 28 | Reset confirmation | As Admin, select Reset demo data and cancel | Existing records remain unchanged |  |  |
| 29 | Reset sample data | As Admin, export backup, confirm reset | 20 sample contacts and 5 households return |  |  |
| 30 | Keyboard access | Use Tab/Shift+Tab and Enter through login and CRM controls | Focus is visible; controls can be reached and activated |  |  |
| 31 | Narrow viewport | Resize browser to phone width | Tables can scroll horizontally; form and buttons remain usable |  |  |
| 32 | Storage failure | If practical, simulate browser storage being unavailable/full | App shows save failure message; no false success is reported |  |  |

## Important limitations to record
- Demo sign-in and role restrictions are client-side only and are not secure authentication or server-enforced authorization.
- Data is saved to the current browser's localStorage, not a shared database. Clearing browser data may remove it.
- The local audit log is editable by anyone with browser developer tools and is not a tamper-proof compliance log.
- Record which browser/device you tested and any failures before submission.
