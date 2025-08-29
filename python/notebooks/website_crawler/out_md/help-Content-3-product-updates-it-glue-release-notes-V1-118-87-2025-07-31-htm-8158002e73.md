---
title: "IT Glue V1.118.87: July 31, 2025"
source: "https://help.itglue.kaseya.com/help/Content/3-product-updates/it-glue-release-notes/V1.118.87-2025-07-31.htm"
crawled_at: "2025-08-18T21:14:12.518974Z"
---

v1.118.88

# IT Glue V1.118.87: July 31, 2025

## Enhancement

### IT Glue Chrome extension

A new version of the IT Glue Chrome Extension has been released, featuring support for autofilling one-time passcodes (OTP). Additionally, users can now exclude specific webpages from autofill, providing greater control and customization of the extension’s behavior.

## Fixes

* Resolved an issue where icons for related items appeared inconsistently in the dropdown search compared to the left sidebar. Icons now accurately reflect their asset types.
* Fixed a bug that caused the Password List View to freeze after returning from a password’s revision view. Navigation is now smooth and responsive.
* Addressed a security issue where asset names containing embedded script tags (e.g., <script>alert("hello");</script>) triggered a 403 error. This issue has been resolved across both the Flexible Asset and Groups pages.
* Corrected misleading Auvik UID-related error messages in sync logs. Logs now accurately reflect the true sync status.
* Fixed an issue where IT Glue organization data wasn’t syncing with myITprocess despite KaseyaOne SSO being enabled. Data now syncs as expected.
* Resolved an error that prevented network data from being retrieved and displayed. Network Glue now successfully collects and shows network information.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
