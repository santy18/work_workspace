---
title: "Microsoft Integration: Intune"
source: "https://help.itglue.kaseya.com/help/Content/1-admin/microsoft/intune-integration.html"
crawled_at: "2025-08-18T21:14:33.528912Z"
---

v1.118.88

# Microsoft Integration: Intune

NAVIGATION  Admin > Integrations > Microsoft > Intune

SECURITY  Manager or Administrator

BEFORE YOU BEGIN  To review prerequisites and learn how to fully set up an integration with Microsoft in IT Glue, refer to [Microsoft Integration](microsoft-integration.html).

Opting to sync Microsoft Intune devices as part of your integration with Microsoft allows Intune device details to sync automatically to IT Glue, ensuring accurate and up-to-date data.

## Syncing Intune devices

Refer to [Set up the integration in IT Glue](microsoft-integration.html#Set-up-the-integration-in-IT-Glue) in [Microsoft Integration](microsoft-integration.html) to learn how to perform the initial data sync. To sync Intune devices, you must select the **Sync Intune Devices** check box from the **Intune** tab in the sync settings.

## Reviewing sync and matching Microsoft devices to IT Glue configurations

IT Glue discovers tenants and devices and tries to match them to your data in your account based on the following logic:

| Rule | Matches on |
| --- | --- |
| Organization | Tenant name |
| Configuration | Intune device name, MAC, Serial |

After matching Microsoft tenants to IT Glue organizations in [Review sync and match Microsoft tenants to IT Glue organizations](microsoft-integration.html#Review-sync-and-match-Microsoft-tenants-to-IT-Glue-organizations), you can check for and map any unmatched devices as follows:

1. From the **Microsoft Tenant Matching** page, click the **Matched** filter.
2. Any organization displaying a count of matched devices that does not equal the total number of devices in the **Unmatched Machines** column requires review. From the more menu , select **Match Devices**.
3. You'll be redirected to the **System Matching** page for the selected organization. For each unmatched Microsoft device, you can perform one of the following actions:  
   * Match to a suggested IT Glue configuration by selecting **Accept Suggested Match** from the more menu .
   * Create a new IT Glue configuration to match to by selecting **Create Configuration** from the more menu .

   NOTE  Kaseya does not recommend that you create new configurations if your intent is to have them populate from IT Glue to your PSA solution. New items created in this way will not automatically sync with your PSA unless you manually edit and save each item.

   IMPORTANT  Before creating a configuration, you should first try to match the devices by MAC addresses or serial number. Only after you've verified that the corresponding configurations do not exist in IT Glue should you create them. You can expand a device to view its details.

   * Prevent an item from counting as unmatched in subsequent syncs by selecting **Ignore** from the more menu . The device will move to the **Ignored** filter, where you can match it in the future, if desired.
   * Search for and select an IT Glue configuration to match to by entering its name in the **Match To** column.

   You also have the option to accepted suggested matches for, create configurations for, or ignore multiple devices at once. Select the check boxes next to any number of devices, or select all devices by selecting the check box in the header, and select the applicable action from the **Bulk Actions** drop-down menu in the lower-left corner of the page.
4. Repeat this process for each organization until you've matched all unmatched devices. Once you've done so, the integration setup is complete.

### Reverting or changing a match

To revert a match, click the **Matched** filter. From the more menu  for a device, select **Revert Match** to move it back to the **Unmatched** filter.

To change a match, click the **Matched** filter. From the more menu  for a device, select **Change Match**, and enter an IT Glue configuration name in the **Matched To** column.

## Copilot Smart Relate for Intune devices

Refer to [Microsoft Integration: Copilot Smart Relate](microsoft-copilot-smart-relate.html).

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
