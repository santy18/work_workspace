---
title: "RMM field mappings"
source: "https://help.itglue.kaseya.com/help/Content/1-admin/rmm-integrations/rmm-field-mappings.html"
crawled_at: "2025-08-18T21:14:24.885047Z"
---

v1.118.88

# RMM field mappings

This article defines how RMM fields are mapped to IT Glue fields.

## Prerequisites

* A Manager role will only be able to see RMM matched/unmatched data for organizations that they have explicit access to. To grant access to RMM data for all organizations, refer to **Step 7** of our [Adding and removing users](../users-and-groups/adding-and-removing-users.html) topic.

## Field Mappings

RMM is the primary data source so will overlay any similar data coming from your other integrations, PSA, as well as content manually input in to IT Glue. This means that if there is a discrepancy between the incoming data, RMM data will take precedence and appear in the combined view. For more details on how RMM data is displayed in IT Glue, refer to our [Why Can't I See RMM Data in Configuration View](#) topic.

In IT Glue, matched RMM configuration data is displayed along with data from these other sources to create a combined view of configuration items. For configurations you manually create from an RMM integration, the fields in the IT Glue column in the table below, are written one time to IT Glue. All other data will be overlaid on the IT Glue asset with each RMM data load.

|  |  |  |
| --- | --- | --- |
| **RMM** | **IT Glue** | **Overlaid data** |
| CPU | \* |  |
| Default Gateway | Default Gateway |  |
| Disks | \* |  |
| Device Type | Type |  |
| External URL | Manage URL\*\* |  |
| Hostname | Hostname |  |
| IP Addresses | IP Addresses |  |
| Last Login User | \* |  |
| Last Reboot | \* |  |
| Last Seen Online | \* |  |
| MAC Addresses | MAC Addresses |  |
| Manufacturer Name | Manufacturer |  |
| Memory Total | \* |  |
| Model Name | Model |  |
| Name | Name |  |
| RMM Location/Site | Location |  |
| RMM Organization | Organization |  |
| Operating System | Platform/Operating System |  |
| Serial Number | Serial Number |  |

\* Denotes new fields that IT Glue recognizes with an RMM integration. The exceptions for each RMM are listed in the image below. These fields are displayed when viewing a configuration item and are indexed by IT Glue's search.

\*\* This link takes you directly to the device in your RMM.

### Supported field exceptions

Each RMM integration can be slightly different when it comes to which fields are available or supported. The table below explains which fields may or may not be available for your RMM. Items with a black star icon are supported. Items without a star are not supported. The white star icon indicates that the item is only partially supported.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Integration Name** | **CPU** | **ExternalURL** | **LastSeenOnline** | **Disks** | **CompanyId** | **Location** |
| Addigy |  | - |  |  |  |  |
| Atera |  |  |  |  |  |  |
| Auvik | - |  | - | - |  |  |
| Barracuda Managed Workplace |  |  |  |  |  |  |
| ConnectWise Automate |  |  |  |  |  |  |
| ConnectWise RMM |  | - |  |  |  |  |
| Datto RMM |  |  |  |  | - |  |
| Jamf Pro |  |  |  |  |  |  |
| Kaseya VSA |  |  |  |  |  |  |
| LogMeIn Central |  | - |  |  |  |  |
| Meraki |  | - |  |  |  |  |
| NinjaRMM |  |  |  | - |  |  |
| Panorama9 |  |  |  |  |  |  |
| Pulseway RMM |  |  |  |  |  |  |
| N-able RMM |  | - |  |  |  |  |
| N-able N-central |  |  | 1 | 2 |  |  |
| Syncro |  |  |  |  |  |  |
| Watchman Monitoring |  |  |  |  |  |  |
| **Notes:**   1. Not always available 2. Not supported:`Disks.Used` | | | | | |  |

### RMM logic

NOTE  **Note 1:** Before an organization, site, location, or company in an RMM tool can sync with IT Glue to create an IT Glue organization, you must add at least one configuration to it. If there are none and the organization does not already exist in IT Glue from any other source, then it will **not** appear in IT Glue. In this case, you will need to create it manually.

NOTE  **Note 2:** Only RMM companies that have at least one RMM record will sync into IT Glue.

NOTE  **Note** **3:** If there are multiple RMM sites or customers, they can be matched to a single IT Glue organization.

Standard rules are used to associate RMM data to data that is already in your account. The sync will discover and attempt to associate data coming from your RMM to data in IT Glue (PSA, imported, or manually entered data) based on the following rules:

|  |  |
| --- | --- |
| **Rule** | **Matches on** |
| Organization | Name field exact match. If no exact match, suggests organizations based on name pattern recognition for manual matching. |
| Configurations | Exact match on primary MAC address and serial number. If no match on those fields, exact match on primary MAC address. If no match on that field, exact match on serial number. If no match on that field, suggests configurations based on exact name of the device for manual matching. |

[Learn more](../getting-started/sync-methods-which-one-to-choose.html) about how RMM data will be combined with PSA data.

### Showing IP addresses from all sources

You have the option of configuring your account so that you only display IP addresses from the RMM or also display any additional IP addresses written to your account. By default, you only see IP addresses from your RMM. For more information, see [What does the 'Display IT Glue IP addresses...' checkbox do?](../account-administration/what-does-the-display-it-glue-ip-addresses-checkbox-do.html)

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
