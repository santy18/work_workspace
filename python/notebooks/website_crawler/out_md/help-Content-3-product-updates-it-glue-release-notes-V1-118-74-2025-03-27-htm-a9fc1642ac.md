---
title: "IT Glue V1.118.74: March 27, 2025"
source: "https://help.itglue.kaseya.com/help/Content/3-product-updates/it-glue-release-notes/V1.118.74-2025-03-27.htm"
crawled_at: "2025-08-18T21:15:14.568011Z"
---

v1.118.88

# IT Glue V1.118.74: March 27, 2025

## New features

This release introduces the following features:

### Microsoft Entra ID groups auto-documentation

For details, refer to [Microsoft Integration: Entra ID groups auto-documentation](../../1-admin/microsoft/microsoft-entra-id-groups-auto-documentation.html).

### Kaseya MDM Integration

For details, refer to [Integrating with Kaseya MDM](../../1-admin/rmm-integrations/integrating-with-kaseya-mdm.html).

## Enhancement

### VSA 10 API

The VSA 10 API has been migrated from v2 to v3.

### MyGlue Chrome extension 1

Extension pages are now persistent so users don't have to search multiple times for password when needing username and one time password (OTP).

## Bug fixes

This release fixed the following issues:

* When editing a document, the page no longer turns blank, interrupting the editing process.
* Attempting to replace the published version of a document with an older revision no longer produces a 500 error.
* An issue that caused an error message to appear when editing configurations has been fixed.
* Newly created Meraki organizations now appear as expected on the matching page.
* An issue that caused a 500 error to appear when a user with the role of Manager, Editor, or Creator attempted to create a new organization has been fixed.
* When a user receives an error within their sync logs, the user is now able to locate the reported asset within Auvik.
* Exported documents are no longer missing inline image folders.
* When searching for a password using content in the notes section, an issue that caused some entries to not appear in search results has been fixed.
* Flexible assets now appear as expected in Autotask ticket insights.
* MyGlue:
  + Login to MyGlue via extension now redirects when SSO is enabledDeployed.
  + MyGlue extension now fills in the password and the username.
  + Fixed My Glue login redirecting in a loop, repeatedly asking for an email address on the updated version of Edge (133.0.3065.59)

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
