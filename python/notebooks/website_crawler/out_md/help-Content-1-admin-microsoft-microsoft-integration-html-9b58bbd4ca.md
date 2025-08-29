---
title: "Microsoft Integration"
source: "https://help.itglue.kaseya.com/help/Content/1-admin/microsoft/microsoft-integration.html"
crawled_at: "2025-08-18T21:14:05.920565Z"
---

v1.118.88

# Microsoft Integration

NAVIGATION  Admin > Integrations > Microsoft

SECURITY  Manager or Administrator

This integration enables the flow of data from Microsoft directly to IT Glue. Microsoft tenants, users, mailbox information, and more will sync automatically to IT Glue, ensuring accurate and up-to-date data.

NOTE  IT Glue will only pull mailbox information for instances with Microsoft Enterprise licenses.

Benefits of this integration include the following:

* Manage the options of your Microsoft asset, including manual syncing and comparing data between IT Glue and Microsoft.
* Jump from IT Glue to a user list in the tenant portal when you click **Manage** on a synced contact.
* Match data between Intune devices and existing IT Glue configurations, allowing you to compare data between IT Glue and Microsoft Intune.
* View logs related to your integration in the sync logs.

At any time, you can return to the **Active Integrations** page (**Admin > Integrations**) to make changes to the integration.

NOTE  This integration supports direct logins to client admin centers, but integrating in this way requires an additional data source and following the steps in this article for each client you wish to integrate.

NOTE  IT Glue syncs with Microsoft every hour. After a new sync between Microsoft and IT Glue is finished, updated data will appear after a 15-minute period.

## Microsoft field mappings

Microsoft fields are automatically mapped to IT Glue when you set up the integration. Refer to [Microsoft field mappings](microsoft-field-mapping.html).

BEFORE YOU BEGIN  Before you set up this integration, thoroughly review your existing contacts in IT Glue and ensure they adhere to the following matching logic. If existing contacts do not *exactly* match this logic, the integration will create unwanted duplicates.

| IT Glue Asset | Field in IT Glue | Field in Microsoft |
| --- | --- | --- |
| Contacts | Email | 1. Attempt match on any alias of the Microsoft user. 2. Attempt match on the username value (for example, the @onmicrosoft.com domain). 3. Attempt match on combination of **First Name** + **Last Name**. |

## Prerequisites

* Manager or Administrator access to IT Glue.
* Microsoft Cloud Partner certified to offer delegated administration (optional for Intune).
* Delegated admin permissions (DAP) to each of your clients' Microsoft tenants through your own Microsoft Partner Center rather than direct logins to their admin portals (optional for Intune).

### Required for Microsoft 365 only

* One available data source.
* Granular delegated admin permissions (GDAP) relationship with Microsoft Entra roles to each of your clients' Microsoft tenants through your own Microsoft Partner Center. (Not applicable to single tenants.) Refer to [Microsoft Integration: GDAP](microsoft-gdap.html).

## Features

From the sync settings, this integration supports syncing Microsoft 365 contacts, locations, Entra ID functionality, and licenses from the **Microsoft 365** tab as well as Intune devices from the **Intune** tab. Refer to the following topics to explore the various features offered through this integration, depending on what you choose to sync:

* [Microsoft Integration: Intune](intune-integration.html)
* [Microsoft Integration: Syncing contacts with BMS](office-365-auto-sync-contacts-with-bms.html)
* [Microsoft Integration: Syncing Microsoft licenses with IT Glue](microsoft-license-integration.html)
* [Microsoft Integration: Entra ID password rotation](microsoft-entra-id-password-rotation.htm)
* [Microsoft Integration: Entra ID groups auto-documentation](microsoft-entra-id-groups-auto-documentation.html)
* [Microsoft Integration: BitLocker recovery keys](../../2-using/documentation-guide/BitLocker_Keys.html)
* [Microsoft Integration: Copilot Smart Relate](microsoft-copilot-smart-relate.html)

## Displaying concealed Microsoft 365 user, group, and site names

You will need to turn off a feature in Microsoft 365 that conceals users, groups, and site names. If you do not turn off this feature, the integration will not be able to retrieve mailbox usage.

To prevent this issue, complete the following steps in the Microsoft 365 admin center.

1. In the Microsoft 365 admin center, navigate to **Settings > Org Settings > Services**.
2. Select **Reports**.
3. Clear **Display concealed user, group, and site names in all reports**, and click **Save**.

## How to...

IMPORTANT  As of January 2024, IT Glue supports GDAP. If configuring GDAP, refer to [Microsoft Integration: GDAP](microsoft-gdap.html), following the instructions in [Creating a service account user for GDAP](microsoft-gdap.html#Creating-a-service-account-user-for-GDAP) and [Creating a new security group](microsoft-gdap.html#Creating-a-new-security-group), before proceeding with the following steps.

[Register IT Glue as an application in your Microsoft account](#)

1. Log in to your [Microsoft Entra ID admin center](https://entra.microsoft.com/#home).
2. From the left navigation menu, navigate to **Identity > Applications > App registrations**.
3. Click **New registration**.
4. On the **Register an application** page, fill in the following fields:
   1. **Name**: Enter an application name that will be displayed to users of the application.
   2. **Supported account types**: Select the **Accounts in any organizational directory and personal Microsoft accounts** option to map to.
   3. **Redirect URI**: Select **Web** in the drop-down menu and enter a URL for the app.

   NOTE  The **Redirect URI** field is required for users setting up GDAP. Refer to [Microsoft Integration: GDAP](microsoft-gdap.html).

   * NA: https://[subdomain].itglue.com/microsofts
   * EU: https://[subdomain].eu.itglue.com/microsofts
   * AU: https://[subdomain].au.itglue.com/microsofts
5. Click **Register** to access the newly created application.

[Copy your client ID and tenant ID from Microsoft](#)

Complete the following steps to copy the IDs for your IT Glue application in Microsoft, which you will later need to paste into IT Glue as part of the [Set up the integration in IT Glue](#Set-up-the-integration-in-IT-Glue) process:

1. From the **All applications** tab on the **App registrations** page, click the newly configured application in the list.
2. Click the **Copy to clipboard** icon next to the **Application (client) ID** and **Directory (tenant) ID**, which you will paste into IT Glue.

[Generate and copy your client secret value in Microsoft](#)

Complete the following steps to generate a secret key for your IT Glue application in Microsoft, which you will later need to paste into IT Glue as part of the [Set up the integration in IT Glue](#Set-up-the-integration-in-IT-Glue) process:

1. With your IT Glue application selected in the Microsoft Entra admin center, click **Certificates & secrets**.
2. Click **New client secret**.
3. Enter a description for the client secret and select **730 days (24 months)** from the **Expires** drop-down menu.
4. Click **Add**.
5. In the **Value** column, click the **Copy to clipboard** icon to copy the client secret value, which you will paste into IT Glue.

NOTE  Client secret values cannot be viewed, except for immediately after creation. Be sure to save the secret when created before leaving the page.

[Configure API access permissions in Microsoft](#)

You will need to add API access to complete the application.

IMPORTANT  Support for the Azure Active Directory Graph API is deprecated. Update your API permissions using the **App registrations** page in Microsoft Azure to reflect the information provided here. In addition to these permissions, Microsoft Partner Center permission should be added. This may be found within **APIs my organization uses** in Microsoft Entra Admin center using the following ID: fa3d9a0c-3fb0-42cc-9193-47c7ecd2edbd.

1. With the IT Glue application selected, click **API permissions** in the left navigation menu.
2. You will see that Microsoft Graph is already assigned a default **User.Read** permission. Click the more menu for this permission and select **Remove permission**.
3. In the confirmation dialog box, click **Yes, remove** to delete this permission.
4. Once the default permission is removed, click **Add a permission**.
5. From the **Request API permissions** pane, click the **Microsoft Graph** tile.
6. Click **Application permissions**.
7. Expand each of the following sections and make the following selections:
   1. **Directory**: Select the **Directory.ReadWrite.All** check box.
   2. **Reports**: Select the **Reports.Read.All** check box.
   3. **User**: Select the **User.Read.All** check box.
   4. (Required only if you are syncing Intune devices to IT Glue) **DeviceManagementManagedDevices**: Select the **DeviceManagementManagedDevices.Read.All** check box. Refer to [Microsoft Integration: Intune](intune-integration.html).
   5. (Required only if you are using IT Glue to update BitLocker recovery keys) **BitlockerKey**: Select the **BitlockerKey.Read.All** check box. Refer to [Microsoft Integration: BitLocker recovery keys](../../2-using/documentation-guide/BitLocker_Keys.html).

   NOTE  If you are syncing Intune devices and have a parent tenant, update the application permission in the parent tenant to include all the Device/DeviceManagement permissions.

   NOTE  If you have a GDAP configuration, review your API permissions to ensure they are up to date with the following requirements.

   * AuditLog.Read.All
   * DeviceManagementManagedDevices.Read.All
   * Directory.Read.All
   * Directory.ReadWrite.All
   * Reports.Read.All
   * User.Read.All

     IMPORTANT  **ReadWrite** access to directory data is required to add the created Azure application to the AdminAgents security group. Without this permission, this can only be done directly with Microsoft's API or PowerShell. Microsoft 365 only supports adding new users to groups and not the applications.

     IMPORTANT  Ensure that you add the corresponding DAP type, as well, for all application permission types, as shown.

     NOTE  In addition to these permissions, Microsoft Partner Center permission should be added. This can be found within **APIs my organization uses** in Microsoft Entra Admin center using the following ID: fa3d9a0c-3fb0-42cc-9193-47c7ecd2edbd.
8. Save the changes by clicking **Add permissions**.
9. On the **API permissions** page, click **Grant admin consent for <company>**.
10. In the confirmation dialog box, click **Yes**.

Once consent is granted, you will see a confirmation banner at the top of the page and that the **Status** column for all permissions displays **Granted**.

[Set up the integration in IT Glue](#)

Next, you'll authenticate the integration by completing the following steps in IT Glue:

1. From the top navigation menu, click **Admin**.
2. From the left navigation menu, navigate to **Account > Integrations**.
3. In the upper-right corner of the page, click **New**.
4. In the **Featured Integrations** section, click the **+** icon in the **Microsoft** tile.
5. In the **Name** field, enter a name for this integration's connector. The value you input here will appear in your list of integrations on the **Active Integrations** page in IT Glue.
6. In the **Tenant ID** field, paste the **Directory (tenant) ID** you copied from Microsoft in [Copy your client ID and tenant ID from Microsoft](#Copy-your-client-ID-and-tenant-ID-from-Microsoft).
7. In the **Application ID** field, paste the  **Application (client) ID** you copied from Microsoft in [Copy your client ID and tenant ID from Microsoft](#Copy-your-client-ID-and-tenant-ID-from-Microsoft).
8. In the **Secret Key** field, paste the client secret value you copied from Microsoft in [Generate and copy your client secret value in Microsoft](#Generate-and-copy-your-client-secret-value-in-Microsoft).
9. Click **Connect**.
10. You will be redirected to the Microsoft login page, where you will enter your integrating account credentials. If using GDAP, refer to [Microsoft Integration: GDAP](microsoft-gdap.html) to learn how to create the service account you will use for authentication.
11. Once you log in, you will be prompted to authorize and accept the permissions.
12. On the **Sync your data Microsoft** page, you will select the data you want to sync. By default, recommended options are listed first.

NOTE  As a best practice, we recommend that you select only the user subscriptions that you actively manage.

13. If you are a Network Glue customer, you can select the **Enhance Contacts with Microsoft Entra ID** check box in the **Microsoft Entra ID Sync** section to further enhance your IT Glue contacts with Microsoft Entra information. This feature pulls in fields for **Status**, **Last Logon**, and **Last Password Change**.

NOTE  To obtain all available Microsoft Entra fields, the Microsoft Graph permission must be enabled in the Microsoft application.

NOTE  The **Last Logon** field will appear only when the user has logged in within the past 30 days.

14. If you are syncing Intune devices from the **Intune** tab, refer to [Microsoft Integration: Intune](intune-integration.html) for instructions.
15. Click **Save and Continue**. The sync will be automatically queued on the **Active Integrations** page.
16. By default, newly queued syncs are scheduled to take place one hour later. From the more menu  in the Microsoft connector, select **Start Manual Sync** to initiate immediate syncing.

IT Glue will begin to import and match your Microsoft data. During this process, the **Status** column will display **Syncing**. When the process finishes, the **Status** column will change to **OK**, and you will receive an email notification.

### Pausing and resuming a sync

To pause a sync, select **Pause Sync** from the connector more menu . When ready to resume the sync, select **Resume Sync**.

NOTE  If you have a Microsoft Partner Network account with access to multiple tenants, disconnecting a Microsoft integration will not remove Admin privileges from your configured application. Remove these Admin privileges yourself or delete the configured application if no longer needed.

[Review sync and match Microsoft tenants to IT Glue organizations](#)

IT Glue discovers Microsoft tenants and users and attempts to match them to the data in your account based on the following logic:

| Rule | Matches on |
| --- | --- |
| Organization | Tenant name |
| Contact email address | **Username** + **@** domain |

If no IT Glue organization can be matched automatically, suggestions will be made based on name similarity. If no suggestions can be made, you will have the option to create a new organization.

**Tip!** If you have two-way sync enabled in Kaseya BMS or Vorex PSA, all contacts created with your Microsoft integration can be automatically pushed to your PSA. For two-way sync instructions, refer to [Enable two-way sync](../psa-integrations/enabling-two-way-sync.html).

Following the initial sync and automatic matching in IT Glue, it's important to review the results of the import to check for and manually map any unmatched tenants as follows:

1. From the top navigation menu, click **Admin**.
2. From the left navigation menu, navigate to **Account > Integrations**.
3. From the more menu  in the Microsoft connector, select **Matching**.
4. In the **Unmatched** filter, which is selected by default, review any unmatched tenants. If IT Glue has a mapping recommendation, it will appear in the **Suggested Match** column.
5. For any unmatched tenants, you can perform one of the following actions:
   * Match to a suggested IT Glue organization, if available in the **Suggested Match** column, by selecting **Accept Suggested Match** from the more menu .
   * Create a new IT Glue organization to match to by selecting **Create Organization** from the more menu .

   IMPORTANT  Before creating an organization, ensure that no corresponding organization already exists; otherwise, a duplicate will be created.

   * Prevent an item from counting as unmatched in subsequent syncs by selecting **Ignore** from the more menu . The group will move to the **Ignored** filter, where you can match it in the future, if desired.
   * Search for and select an IT Glue organization to match to by entering its name in the **Match To** column.

   You also have the option to accepted suggested matches for, create organizations for, or ignore multiple tenants at once. Select the check boxes next to any number of tenants, or select all tenants by selecting the check box in the header, and select the applicable action from the **Bulk Actions** drop-down menu in the lower-left corner of the page.

### Reverting or changing a match

To revert a match, click the **Matched** filter. From the more menu  for a tenant, select **Revert Match** to move it back to the **Unmatched** filter.

To change a match, click the **Matched** filter. From the more menu  for a tenant, select **Change Match**, and enter an IT Glue organization name in the **Matched To** column.

[Sync Microsoft contacts to IT Glue](#)

1. Once all tenants have been matched, you will need to start a new manual sync to sync all Microsoft contacts to IT Glue. From the more menu  in the Microsoft connector, select **Start Manual Sync**.
2. When the sync is complete, click any matched organization to open it in IT Glue. Then, click **Contacts** from the left navigation menu to review the list of synced Microsoft contacts and their data.

NOTE  Contact matching behaves slightly differently to standard matching logic. If no match can be made based on the criteria, a new duplicate contact will be created without further user input.

## Automating the creation of app registration and service principal using PowerShell

[This GitHub script](https://github.com/ITGlue-Support/Microsoft_Integration_App/blob/main/MI_App.ps1) will automatically create an app registration and a security group in your Microsoft tenant with all the required API permissions to connect the integration with IT Glue.

You must use PowerShell/Powershell ISE to run the script. The script will prompt you to insert the necessary information and provide admin consent to the API permission added to the app to pull the information into IT Glue.

NOTE  For this script to work, it will automatically install the required PowerShell modules and prompt you to log in with the local tenant Global Admin user.

At the end of the process, you will receive all the information you are required to enter on the Microsoft integration setup page in IT Glue, as detailed in [Set up the integration in IT Glue](#Set-up-the-integration-in-IT-Glue).

### Prerequisite

* Access to the Global Admin user for your local Microsoft tenant

### Steps after running the script

1. Create a Service Account user in Microsoft Entra with Global Admin permission. Refer to [Microsoft Integration: GDAP](microsoft-gdap.html).
2. Add a GDAP relationship in [Microsoft Partner Center](https://partner.microsoft.com/) with the appropriate Microsoft Entra roles assigned to the security group. Refer to [Microsoft Integration: GDAP](microsoft-gdap.html).
3. If you wish to enable password rotation or BitLocker, you will need to add additional API permissions and follow the steps in [Microsoft Integration: Entra ID password rotation](microsoft-entra-id-password-rotation.htm) or [Microsoft Integration: BitLocker recovery keys](../../2-using/documentation-guide/BitLocker_Keys.html), respectively.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
