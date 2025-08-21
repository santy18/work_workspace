---
title: "Microsoft field mappings"
source: "https://help.itglue.kaseya.com/help/Content/1-admin/microsoft/microsoft-field-mapping.html"
crawled_at: "2025-08-18T21:14:36.148133Z"
---

v1.118.88

# Microsoft field mappings

This article defines how Microsoft fields are mapped to IT Glue fields. Refer to [Microsoft Integration](microsoft-integration.html) to learn how to set up an integration with Microsoft in IT Glue.

## Sync behavior

### Summary

* Microsoft tenants → IT Glue organizations
* Microsoft users → IT Glue contacts
* Microsoft devices → IT Glue configurations

### Organizations

| IT Glue: Organizations | Microsoft: Tenants |
| --- | --- |
| Name | Tenant Name |
| Location Name (use organization name) | Tenant Name |
| Address | Address |
| State/Province | State/Province |
| City | City |
| Postal / Zip Code | Postal / Zip Code |
| Location Phone | Phone |

### Contacts

| IT Glue: Contacts | Microsoft: Users |
| --- | --- |
| Name | First Name + Last Name |
| Title | Job Title |
| Office Phone | Phone |
| Mobile Phone | Mobile |
| Primary Email | User Name |
| Mailbox Aliases | Alias |

### Configurations

| IT Glue: Configurations | Microsoft: Devices |
| --- | --- |
| Type | Device Type |
| Manage URL | External URL |
| Office Phone | Phone |
| Hostname | Device Name |
| IP Addresses | IP Addresses |
| MAC Addresses | MAC Addresses |
| Manufacturer | Manufacturer Name |
| Model | Model |
| Serial Number | Serial Number |

NOTE  **Tip!** If you have two-way sync enabled in your PSA, all contacts created with your Microsoft integration can be automatically pushed to your PSA. For two-way sync instructions, review our [Enable two-way sync](../psa-integrations/enabling-two-way-sync.html) KB article or one of the applicable KB articles below:

* [ConnectWise or Autotask](../psa-integrations/integrating-with-autotask.html)
* [Kaseya BMS](../psa-integrations/enabling-kaseya-bms-two-way-sync.html)
* [Pulseway PSA](../psa-integrations/pulseway-psa-two-way-sync.html)

### Matching logic

Matching rules are used to match records within IT Glue when pulling data from Microsoft. The sync will discover tenants, contacts, and devices in Microsoft and match them to data in IT Glue using the following Microsoft fields:

| IT Glue Asset | Field in IT Glue | Field in Microsoft |
| --- | --- | --- |
| Organizations | Name | Tenant Name |
| Locations | Name | Tenant Name |
| Contacts | Email | 1. Attempt match on any alias of the Microsoft user. 2. Attempt match on the username value (for example, the @onmicrosoft.com domain). 3. Attempt match on combination of **First Name** + **Last Name**. |

Contact matching should satisfy any of the preceding three conditions, or else a new contact will be created.

### Locations

| IT Glue: Locations | Microsoft: Locations |
| --- | --- |
| Name | First Name + Last Name |
| Name | Location Name |
| Address 1 | Address 1 |
| Address 2 | Address 2 |
| State/Province | State/Province |
| Country | Country |
| City | City |
| Postal / Zip Code | Postal / Zip Code |
| Phone | Phone |
| Fax | Fax |

Location information is a one-time push into IT Glue and does not sync. If the location is updated in Microsoft, then IT Glue creates another location for the Organization.

The matching logic matches Address 1, City, State/Province, and Country with the Microsoft tenant and a location within IT Glue. If there is a match, there will be no location created in IT Glue, but will update the existing location.

After the initial sync, any updates to the Microsoft tenant location will result in another location creation in IT Glue. **If Address 1, City, State/Province, and Country do not match, then a new location is created.**

### Configurations

Standard rules are used to associate Intune data to data that is already in your account. The sync will discover and attempt to associate data coming from your Intune to data in IT Glue (PSA, imported, or manually entered data) based on the following rules:

| Rule | Matches on |
| --- | --- |
| Organization | Name field exact match. If no exact match, suggests organizations based on name pattern recognition for manual matching. |
| Configurations | Exact match on primary MAC address and serial number. If no match on those fields, exact match on primary MAC address. If no match on that field, exact match on serial number. If no match on that field, suggests configurations based on exact name of the device for manual matching. |

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
