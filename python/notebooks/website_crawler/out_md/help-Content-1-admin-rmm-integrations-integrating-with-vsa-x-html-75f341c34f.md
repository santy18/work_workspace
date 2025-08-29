---
title: "Integrating with VSA 10"
source: "https://help.itglue.kaseya.com/help/Content/1-admin/rmm-integrations/integrating-with-vsa-x.html"
crawled_at: "2025-08-18T21:14:03.563370Z"
---

v1.118.88

# Integrating with VSA 10

[Security and navigation](#)

### VSA 10

NAVIGATION  Modules > Integrations > IT Glue

SECURITY  
Administrator

### IT Glue

NAVIGATION  Admin > Account > Integrations

SECURITY  Manager or Administrator  
A Manager role will see matched and unmatched VSA 10 data for organizations to which they have explicit access only.

## Overview

This integration allows you to synchronize and map your VSA 10 groups to organizations in IT Glue, enabling the sharing of information about managed entities, including device status and details, between both platforms.

Upon performing your first synchronization, IT Glue will discover all organizations and devices in VSA 10. The system will automatically attempt to map organizations based on name and pattern recognition and configurations based on exact device name, MAC address, or serial number.

Once the discovery is finished, you'll have the opportunity to review and fine-tune the relationships of VSA 10 groups to their corresponding IT Glue organizations.

With this integration activated, you can view, manage, and create documentation from IT Glue while working in VSA 10. While in a Remote Control session, leverage the 1-Click feature for automatic password injection, eliminating the need to switch between screens.

BEFORE YOU BEGIN  If you plan to use a PSA platform with this integration, we strongly recommend that you first sync VSA 10 to your PSA solution and then sync the PSA platform to IT Glue to ensure accurate configuration matching.

### Automations powered by this integration

* In-context device documentation.
* IT Glue documentation in **VSA X** mobile app.
* IT Glue password support for VSA 10 1-Click.

## Prerequisites

To set up the integration, you'll need the following:

* An SSL connection with a valid VSA 10 certificate chain, including an intermediate certificate signed by a trusted authority, is required. The certificate must meet the following requirements:
  + The certificate must be signed by a valid issuer and cannot be a self-signed certificate.
  + The SSL chain, including the intermediate certificates, must be complete.
  + The fully qualified domain name (FQDN) for the server hosting the VSA 10 instance must match one of the certificate's common names.

  NOTE  You can use an online SSL checker, such as [SSL Shopper](https://sslshopper.com/ssl-certificate-tools.html), to check your certificate status.

## Field mappings

Refer to [RMM field mappings](rmm-field-mappings.html).

## How to...

[Activate the integration in VSA 10](#)

First, you'll activate the integration in VSA 10 by entering the IT Glue subdomain authorized to connect to your VSA 10 instance. Complete the following steps:

1. From the left navigation menu, navigate to **Integrations > IT Glue**.
2. In the **Integration Status** section, turn on the **Enabled** toggle.
3. In the **Region** section, select the hosting location of your IT Glue instance.
4. In the **Subdomain** section, enter your IT Glue subdomain.

   EXAMPLE  If your IT Glue URL is **abc-company.itglue.com**, enter **abc-company**.
5. Click **Save**.

[Connect the integration in IT Glue](#)

Next, you'll authenticate the integration by completing the following steps in IT Glue:

1. From the top navigation menu, click **Admin**.
2. From the left navigation menu, navigate to **Account > Integrations**.
3. In the upper-right corner of the page, click **New**.
4. In the **RMM Tools** section, click the **+** icon in the **VSA 10** tile.
5. In the **Name** field, enter a name for this integration's connector. The value you input here will appear in your list of integrations on the **Active Integrations** page in IT Glue.
6. In the **VSA X Server Hostname** field, enter the fully qualified domain name (FQDN) of the VSA 10 instance to which you'd like to connect.

EXAMPLE  **demo.vsax.net**

7. Click **Connect**.
8. On the API access authorization page, click **Allow** to grant IT Glue access to your VSA 10 data.

Once successfully connected, you will be redirected to the **Active Integrations** page in IT Glue, where the new VSA 10 connector will display the status **OK**.

NOTE  Enabling the integration may result in Kaseya data center IP addresses appearing in your activity logs.

[Import VSA 10 data to sync to IT Glue](#)

Initiating a data sync allows the integration to discover your VSA 10 groups and devices and match them to their IT Glue counterparts. After the sync finishes, you'll need to review and manually action any items the integration was unable to automatically match.

Import VSA 10 data into IT Glue as follows:

1. From the top navigation menu, click **Admin**.
2. From the left navigation menu, navigate to **Account > Integrations**.
3. From the more menu  in the VSA 10 connector, select **Start Manual Sync**.

IT Glue will begin to import and match your VSA 10 groups. During this process, the **Status** column will display **Syncing**. When the process finishes, the **Status** column will change to **OK**, and you will receive an email notification.

### Pausing and resuming a sync

To pause a sync, select **Pause Sync** from the connector more menu . When ready to resume the sync, select **Resume Sync**.

[Review sync and match VSA 10 groups to IT Glue organizations](#)

BEFORE YOU BEGIN  Before a VSA 10 group can sync to an IT Glue organization, you must add at least one VSA 10 device to it. If none exist, and the organization does not already exist in IT Glue from any other source, then it will not appear. In that case, you'll need to manually create it in IT Glue.

Following the initial sync and automatic matching in IT Glue, it's important to review the results of the import to check for and manually map any unmatched groups as follows:

1. From the top navigation menu, click **Admin**.
2. From the left navigation menu, navigate to **Account > Integrations**.
3. From the more menu  in the VSA 10 connector, select **Matching**.
4. In the **Unmatched** filter, which is selected by default, review any unmatched VSA 10 groups. If IT Glue has a mapping recommendation, it will appear in the **Suggested Match** column.
5. For any unmatched groups, you can perform one of the following actions:
   * Match to a suggested IT Glue organization, if available in the **Suggested Match** column, by selecting **Accept Suggested Match** from the more menu .
   * Create a new IT Glue organization to match to by selecting **Create Organization** from the more menu .

   IMPORTANT  Before creating an organization, ensure that no corresponding organization already exists; otherwise, a duplicate will be created.

   * Prevent an item from counting as unmatched in subsequent syncs by selecting **Ignore** from the more menu . The group will move to the **Ignored** filter, where you can match it in the future, if desired.
   * Search for and select an IT Glue organization to match to by entering its name in the **Match To** column.

   You also have the option to accepted suggested matches for, create organizations for, or ignore multiple groups at once. Select the check boxes next to any number of groups, or select all groups by selecting the check box in the header, and select the applicable action from the **Bulk Actions** drop-down menu in the lower-left corner of the page.

Once all groups have been matched or ignored, the same process should be followed for any unmatched devices, as described in the next section.

### Reverting or changing a match

To revert a match, click the **Matched** filter. From the more menu  for a group, select **Revert Match** to move it back to the **Unmatched** filter.

To change a match, click the **Matched** filter. From the more menu  for a group, select **Change Match**, and enter an IT Glue organization name in the **Matched To** column.

[Review sync and match VSA 10 devices to IT Glue configurations](#)

The final step in the integration deployment process is to check for and map any unmatched devices. Complete the following steps in IT Glue:

1. From the **VSA X Group Matching** page, click the **Matched** filter.
2. Any organization displaying a count of matched devices that does not equal the total number of devices in the **Unmatched Systems** column requires review. From the more menu , select **Match Devices**.
3. You'll be redirected to the **System Matching** page for the selected organization. For each unmatched VSA 10 device, you can perform one of the following actions:  
     
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

[Automatically inject IT Glue credentials in VSA 10 Remote Control sessions](#)

With the integration active, VSA 10 users with **Remote Control > Use IT Glue Passwords** permission will notice the Remote Control 1-Click manager includes IT Glue **Embedded** and **Related** password objects for supported devices.

You'll be able to select the credentials directly from within VSA 10 to automatically launch a remote session and log in to Windows computers in one step. IT Glue passwords will also be available for secure copy and paste while working within Remote Control sessions.

The integration improves efficiency by reducing the number of clicks and context-switching that are normally required when searching for credentials. It also eliminates the need to copy passwords to the clipboard, which improves security.

For more information about Remote Control 1-Click, refer to [Remote Control](../devices/device-list-manage-remote-control.htm).

[Disconnect or delete the integration](#)

Complete the following steps in IT Glue to disconnect or delete the integration:

1. From the top navigation menu, click **Admin**.
2. From the left navigation menu, navigate to **Account > Integrations**.
3. From the more menu  in the VSA 10 connector, select **Disconnect**.

NOTE  This option is also available from the **Edit Credentials** page.

4. If you may resync the integration in the future and wish to preserve the VSA 10 data in IT Glue, select **Pause syncing and keep all data**. Otherwise, select **Permanently disconnect integration and remove all organization and asset matchings**, which will remove overlaid data but retain IT Glue assets. [Learn about overlaid data](https://help.itglue.kaseya.com/help/Default_CSH.htm#1130).

Disabling the integration in VSA 10 will clear all user data. To do so, turn off the **Enabled** toggle, click **Save**, and then click **Confirm** in the confirmation dialog box.

## VSA 10 Agent status on the network diagram

Customers with Network Glue and a VSA 10 integration can view and filter all agent statuses on the network diagram. If your Network Glue devices are matched to IT Glue configurations and synced with VSA 10, your diagram will show the following statuses:

* VSA 10 Agent is currently online.
* VSA 10 Agent is currently offline.
* VSA 10 Agent and user are both currently online.

In addition, you can filter for devices that are matched or not matched to IT Glue via the **Matched to IT Glue** status. Refer to [Guide to the Network Glue network diagram](../../4-network-glue/using-network-glue/guide-to-the-network-glue-network-diagram.html).

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
