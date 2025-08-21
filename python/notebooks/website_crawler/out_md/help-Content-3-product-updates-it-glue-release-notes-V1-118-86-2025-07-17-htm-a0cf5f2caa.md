---
title: "IT Glue V1.118.86: July 17, 2025"
source: "https://help.itglue.kaseya.com/help/Content/3-product-updates/it-glue-release-notes/V1.118.86-2025-07-17.htm"
crawled_at: "2025-08-18T21:14:09.482328Z"
---

v1.118.88

# IT Glue V1.118.86: July 17, 2025

## Enhancements

### Cooper insight for Password SafeShare

A Cooper insight named **Password SafeShare** is now available in KaseyaOne for the IT Glue Password Safeshare feature.

This insight is displayed if your IT Glue account does not have this setting enabled for any passwords. This insight is considered completed when at least one password has been shared out of your account or when the setting is enabled for your account or for selected passwords.

Refer to [Password SafeShare](../../2-using/documentation-guide/password-safeshare.htm) in this Help system and [Cooper Intelligence Engine](https://help.one.kaseya.com/help/Default_CSH.htm#1004) in the KaseyaOne Help system.

### SNMP status handling improved

To provide clearer diagnostics and simplify troubleshooting, logic has been added to distinguish between cases in which SNMP is detected but not functioning and cases in which SNMP is not found at all.

### @relate functionality in documents improved

The option to filter assets globally or by the current organization when using the @relate functionality in document text boxes is now available. Refer to [@relate links](../../2-using/documents/quick-guide-for-documents.html#@relate-links) in [Quick guide for documents](../../2-using/documents/quick-guide-for-documents.html).

### Option to share vaulted passwords removed

The **Share Password** option, part of the Password SafeShare feature, has been removed from the editing page for vaulted passwords, which inherently cannot be shared.

## Fixes

* An issue that caused users to have to click **Add Section** twice to add a new section to a document has been fixed. The menu now consistently opens on the first click, ensuring a smoother editing experience.
* When logging into Kaseya Helpdesk, selecting **IT Glue** as a login option now works as intended for a seamless process.
* Password history is now accessible as expected when accessing previous password values through the **Revisions** option.
* **Configuration Types** in the left navigation menu are now correctly hidden for MyGlue users who do not have access to view these items based on their user permissions.
* **Quick Notes** can now be created as expected in sub-organizations when the parent is also a sub-organization, allowing for nested structures.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
