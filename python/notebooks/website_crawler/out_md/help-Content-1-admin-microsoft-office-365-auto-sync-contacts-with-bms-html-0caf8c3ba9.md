---
title: "Microsoft Integration: Syncing contacts with BMS"
source: "https://help.itglue.kaseya.com/help/Content/1-admin/microsoft/office-365-auto-sync-contacts-with-bms.html"
crawled_at: "2025-08-18T21:14:28.495499Z"
---

v1.118.88

# Microsoft Integration: Syncing contacts with BMS

## Introduction

This feature allows Microsoft Office 365 contacts in IT Glue to be automatically pushed and synced into BMS. You will no longer need to manually edit, and save your new Office 365 Contacts in IT Glue to have your data flow into BMS. This ensures data integrity between your core tools - PSA and IT documentation.

Benefits of this feature include:

* No requirement to access each individual contact for syncing with BMS.
* Leverage sync settings in Office 365 and BMS to automatically set required data for a new BMS contact.
* Automate contact creation with IT Glue and BMS.

## How does it work?

IT Glue can push a BMS contact only if the following contact information is available:

* First name
* Primary email address
* Primary phone number
* Location

With our Office 365 integration, we received the first name, primary email address, and location. What we did not receive in a consistent manner for use in BMS was a phone number value and a way to identify if it was considered primary or not.

Our Partners who synced in Office 365 contacts could have missed a phone number in IT Glue as this was not mandatory in Office 365 initially. If a phone number was specified in Office 365, the contact in IT Glue will possess it, but the number would not be marked as “primary”. This poses a problem as the phone number was not fully ready to push to BMS.

This feature provides you with the tools to apply the right values needed for your new contacts, and subsequently push them to BMS. The following scenarios explain how new contacts are created:

### Scenario 1

The Office 365 data **does not** match to existing IT Glue data.  
  
Matching Logic used between an Office 365 contact and an IT Glue contact:

|  |  |  |
| --- | --- | --- |
| **IT Glue Asset** | **IT Glue Field** | **Office 365 Field** |
| Contacts | Email | 1. Attempt match on any alias of the Microsoft user. 2. Attempt match on the username value (e.g. the *@onmicrosoft.com* domain). 3. Attempt match on combination of First Name + Last Name. |

If the match is not successful, A brand new IT Glue contact will be created with the data from Microsoft and pushed on the fly to BMS.

### Scenario 2

A match was made, and the IT Glue contact does not have the sync controls for BMS present at the bottom of the contacts details page. (e.g. The information that states “Manage | Sync now | Disable sync with Kaseya BMS”). In this situation, The existing IT Glue contact will be updated by the Microsoft data and pushed on the fly to BMS.

This feature will not push an IT Glue contact over to BMS if the sync controls for BMS is seen at the bottom of the contacts details page. (e.g. the information that states “Manage | Sync now | Disable sync” with Kaseya BMS”).

IMPORTANT  **Warning.** It is extremely important for you to check your BMS to ensure that you do not have contacts that are supposed to be present in IT Glue that did not sync into IT Glue. If your contacts in BMS did not reach IT Glue, there is no way for us to detect that you already had the contact(s) in BMS before the Office integration auto-pushes the new contact(s)**.** Please see the KB article [About the Manage Data screen](../psa-integrations/about-the-manage-data-screen.html) to review your currently synced contacts before you begin.

## Prerequisites

* Manager or Administrator access to IT Glue.
* An active BMS integration with two-way sync, and contact sync enabled.
* An active Microsoft 365 integration.

## Instructions

1. Navigate to **Admin > Integrations > BMS > Actions Menu > Sync Settings**.
2. In the **Sync Settings** tab, select the **Enable Contact sync** checkbox.
3. In the **Two-Way Sync Settings** tab, select the **Enable two-way sync** checkbox.
4. Select the **Enable automatic pushing of Office 365 contacts** checkbox
5. Specify an **Email Type** and **Phone Type** that will be used to pass the Microsoft 365 email and phone data to BMS.
6. Navigate to **Admin > Integrations > Office 365 > Actions Menu > Matching > Matched** and ensure that your Office 365 tenant(s) are “matched” to an IT Glue organization.
7. In Office 365 create the new active users, or verify if they are present.
8. Navigate to **Admin > Integrations > Office 365 > Actions Menu > Sync Settings** and select the **Set Phone numbers as Primary** checkbox.
9. Choose a **Phone Type** that IT Glue should automatically select and mark as primary.
10. Select the **Replace blank phone numbers with “000-000-0000” checkbox for syncing with BMS** checkbox.
11. Navigate to **Admin > Integrations > Office 365 > Actions Menu > Start Manual Sync** or wait for the next automatic sync to occur.

Your new contacts from Office 365 will flow into IT Glue and subsequently push into BMS according to the sync settings you specified in Office 365, and BMS.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
