---
title: "IT Glue V1.118.77: May 8, 2025"
source: "https://help.itglue.kaseya.com/help/Content/3-product-updates/it-glue-release-notes/V1.118.77-2025-05-08.htm"
crawled_at: "2025-08-18T21:15:50.282148Z"
---

v1.118.88

# IT Glue V1.118.77: May 8, 2025

## New feature

SOP Generator now supports capturing Web Remote sessions in Datto RMM, supporting creation of standard operating procedures for device monitoring and management, including all remote desktop activity, on the fly. Refer to [Cooper Copilot Smart SOP Generator](../../2-using/documentation-guide/sop-generator.htm).

## Fixes

* Organizations in Datto Endpoint Backup now sync correctly with IT Glue.
* Attachments are now accessible on public documents when account IP address restrictions are enabled.
* A sync issue that caused reporting organization data from IT Glue to not transfer to myITprocess has been fixed.
* A bug that caused some users to be unable to open specific configurations in IT Glue, resulting in a blank page, has been fixed.
* Search functionality has been improved to ensure partial keyword matches now return accurate results.

EXAMPLE  Searching **sal** or **sales** will now correctly show results for Patron Manager / Salesforce.

* Manual runbooks are no longer failing for individual organizations that include flexible assets.
* A 414 error that caused Auvik integration syncs to fail has been resolved.
* A bug that caused missing key information in newly created SSL records has been fixed.
* Users can now successfully delete the **AD Security Groups** flexible asset type from IT Glue.
* Updating a group after selecting assets in the **Deny Assets** menu no longer produces a 500 error.
* A display issue where switches were not showing connections in Network Glue diagrams has been fixed.
* A bug that caused Network Glue to not detect devices on the network has been fixed.
* Devices connected to Microsoft Entra ID virtual networks now appear correctly in Network Glue on the **Device Matching** page, in the network view, and on the network topology map because the placeholder MAC address is no longer used for device identification. Previously, these devices were not displayed because they all shared a non-unique placeholder MAC address, which caused them to be merged into a single device.
* The **bulk\_destroy** API call is now deleting organizations as expected.
* Domain data is now properly updated to reflect the latest public information.
* Network Glue now correctly updates **Last Logon** data in the sync with Active Directory, fixing delays.
* WHOIS data for domains is now correctly updated even if the record has no expiry date.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
