---
title: "Microsoft Integration: Entra ID groups auto-documentation"
source: "https://help.itglue.kaseya.com/help/Content/1-admin/microsoft/microsoft-entra-id-groups-auto-documentation.html"
crawled_at: "2025-08-18T21:14:30.416550Z"
---

v1.118.88

# Microsoft Integration: Entra ID groups auto-documentation

NAVIGATION  Admin > Integrations > Microsoft > Microsoft 365 > Microsoft Entra ID Sync

SECURITY  Manager or Administrator users can set up this feature and enable or disable groups.

SECURITY  All users can access the **Entra ID: Security Groups** and **Microsoft 365: Groups** flexible asset types for the organizations to which they have access.

Directly from IT Glue, Network Glue administrators can enable or disable the automatic documentation of groups from Microsoft Entra ID to facilitate greater control over this sensitive information.

This feature provides the following benefits:

* Eliminates the need for manual documentation.
* Ensures that only the most up-to-date data is presented.
* Ensures accuracy of sensitive information.

In urgent situations, having Microsoft Entra ID groups documented in IT Glue allows for instant access to critical details without needing to log in to multiple systems. Administrators and technicians can leverage this feature to quickly check a user's group membership. The ability to check that users and devices are added or removed from the appropriate groups helps streamline your onboarding and offboarding processes.

The **Microsoft 365: Groups** and **Entra ID: Security Groups** flexible assets are also available to MyGlue users.

BEFORE YOU BEGIN  To review prerequisites and learn how to fully set up an integration with Microsoft in IT Glue, refer to [Microsoft Integration](microsoft-integration.html).

## Prerequisites

* A Network Glue subscription is required. If you're not already a Network Glue customer, [request a demo](https://www.itglue.com/networkglue).
* An integration with Microsoft must be active in your IT Glue account. Refer to [Microsoft Integration](microsoft-integration.html).
* No additional API permissions are required to be added in Microsoft beyond the steps outlined in [Configure API access permissions in Microsoft](microsoft-integration.html#Configure-API-access-permissions-in-Microsoft). In the event of unforeseen permissions issues when it comes to multi-tenants, you can attempt to add **Directory.ReadWrite.All** permissions at the following direct link: https://login.microsoftonline.com/<tenant id>/v2.0/adminconsent?client\_id=<app\_id>&scope=https://graph.microsoft.com/Directory.ReadWrite.All

NOTE  Replace <tenant id> with the applicable tenant ID.

## Overview

Active Microsoft Entra ID groups of the **Microsoft 365** type or **Security** type can be synced to IT Glue as part of an existing integration with Microsoft.

**Microsoft 365** groups provide collaboration opportunities by giving group members access to a shared mailbox, calendar, files, SharePoint sites, and more. This option also lets users give people outside of an organization access to the group.

**Security** groups are used to manage user and computer access to shared resources. For example, users can create a security group so that all group members have the same set of security permissions. Members of a security group can include users, devices, and other groups (also known as nested groups).

NOTE  IT Glue syncs with Microsoft every hour. After a new sync between Microsoft and IT Glue is finished, updated data will appear after a 15-minute period.

### Lists of Microsoft Entra ID groups

Two separate lists of synced Microsoft Entra ID groups are available at the organization level in IT Glue:

[Microsoft 365: Groups](#)

When enabled for a Microsoft integration, the **Sync Microsoft 365 Groups** setting automatically establishes a sync between IT Glue and active Microsoft Entra ID groups with the group type **Microsoft 365**. To learn how to enable this setting, refer to [Sync Microsoft 365 groups and/or security groups to IT Glue](#Sync-Microsoft-365-groups-and/or-security-groups-to-IT-Glue).

After the first successful sync, all Microsoft 365 groups stored in Microsoft Entra ID are created and automatically documented in the **Microsoft 365: Groups** flexible asset type. Refer to [View the Microsoft 365: Groups flexible asset for a group](#View-the-Microsoft-365:-Groups-flexible-asset-for-a-group) for access instructions.

[Entra ID: Security Groups](#)

When enabled for a Microsoft integration, the **Sync Entra ID Security Groups** setting automatically establishes a sync between IT Glue and active Microsoft Entra ID groups with the group type **Security**. To learn how to enable this setting, refer to [Sync Microsoft 365 groups and/or security groups to IT Glue](#Sync-Microsoft-365-groups-and/or-security-groups-to-IT-Glue).

After the first successful sync, all security groups stored in Microsoft Entra ID are created and automatically documented in the **Entra ID: Security Groups** flexible asset type. Refer to [View the Entra ID: Security Groups flexible asset for a group](#View-the-Entra-ID:-Security-Groups-flexible-asset-for-a-group) for access instructions.

The actions available to perform for an individual group from the flexible asset (editing a group, deleting a group, creating a new group, and archiving a group) can also be performed from these lists. Groups can be deleted or archived in bulk using the check boxes. For descriptions of these actions, refer to [Action buttons](#Action-buttons).

These lists display the following information for Microsoft Entra ID groups synced to IT Glue:

| Column | Available only for Microsoft 365: Groups | Available only for Entra ID: Security Groups | Description |
| --- | --- | --- | --- |
| Group Name |  |  | Displays the name of the synced group. Click the group name to open its flexible asset in IT Glue. Refer to [Flexible assets for Microsoft Entra ID groups](#Flexible-assets-for-Microsoft-Entra-ID-groups) . |
| Nested Groups |  |  | Displays the name of any nested groups in this security group. Click the group name to open its flexible asset in IT Glue. |
| Members (Matched To A Contact) |  |  | Displays the number of group members matched to IT Glue contacts from the Microsoft Entra ID users sync. To learn how to match contacts in the integration with Microsoft, refer to [Sync Microsoft contacts to IT Glue](microsoft-integration.html#Sync-Microsoft-contacts-to-IT-Glue) in [Microsoft Integration](microsoft-integration.html). Hover over the link to view the full list of their first and last names, which you can scroll through. Click the link to open the group flexible asset in IT Glue, where the members are listed and can be viewed individually.  If only one member is matched, this column displays that member's first and last name. Click the name to open the show page for the contact that exists in IT Glue.  Synced groups are automatically added as **Related Items**, which cannot be deleted, on the show pages for the IT Glue contacts. |
| Members (Not Matched To A Contact) |  |  | Displays the group members *not* matched to IT Glue contacts from the Microsoft Entra ID users sync. To learn how to match contacts in the integration with Microsoft, refer to [Sync Microsoft contacts to IT Glue](microsoft-integration.html#Sync-Microsoft-contacts-to-IT-Glue) in [Microsoft Integration](microsoft-integration.html). Hover over the link to view the full list of their first and last names. Click the number of contacts to open the group flexible asset in IT Glue, where the members are listed in plain text. |
| Devices (Matched To A Configuration) |  |  | Displays the names of Microsoft Entra ID devices matched to IT Glue configurations from the Microsoft Entra ID sync. If the configuration name or hostname matched the name of the Microsoft Entra ID device, the configuration will have been matched. Click the link to open the group flexible asset in IT Glue, where the devices are listed and can be viewed individually.  Synced security groups will be automatically added as **Related Items**, which cannot be deleted, on the show pages for the IT Glue configurations. |
| Devices (Not Matched To A Configuration) |  |  | Displays the names of Microsoft Entra ID devices *not* matched to IT Glue configurations from the Microsoft Entra ID sync. Click the link to open the group flexible asset in IT Glue, where the devices are listed in plain text. |
| Group Email Address |  |  | Displays the group email address from Microsoft Entra ID. Click the link to open the group flexible asset in IT Glue. From that page, you can click the email address to open a new email draft in your default email application, pre-filled with the recipient's address. |
| Domain |  |  | Displays the group domain from Microsoft Entra ID. Click the link to open the group flexible asset in IT Glue, where the domain is displayed in plain text. |
| Group Description |  |  | Displays the description of the group from Microsoft Entra ID. Click the link to open the group flexible asset in IT Glue, where the description is displayed in plain text. |
| Membership Type |  |  | Displays the group's membership type from Microsoft Entra ID. Click the link to open the group flexible asset in IT Glue, where the membership type is displayed in plain text. |
| Sync Status |  |  | The gray plug symbol indicates the syncing of this group is enabled. The yellow plug symbol indicates the syncing of this group is orphaned because the group was deleted in Microsoft Entra ID or archived in IT Glue. The group documented in IT Glue will no longer be updated after the next sync. To learn about archiving groups, refer to [Archive](#Archive) in [Flexible assets for Microsoft Entra ID groups](#Flexible-assets-for-Microsoft-Entra-ID-groups) .  The red plug symbol indicates the syncing of this group is disabled, the **Sync Microsoft 365 Groups** or **Sync Entra ID Security Groups** setting has been cleared from the integration sync settings, or the Microsoft integration that previously managed this sync has been removed. To learn about disabling the syncing of groups, refer to [Enable sync/Disable sync](#Enable-sync-Disable-sync) in [Flexible assets for Microsoft Entra ID groups](#Flexible-assets-for-Microsoft-Entra-ID-groups) . |
| Updated |  |  | Displays when the group was last updated in Microsoft Entra ID. The latest updates will be captured in IT Glue in the next integration sync. |
| Actions |  |  | The edit icon allows you to edit the group flexible asset. For details, refer to [Edit](#Edit). The access icon allows you to view the list of users who can access this group in IT Glue. To learn how to change this access, refer to the following:   * [Limit access to Microsoft 365 groups to specific IT Glue groups or users](#Limit-access-to-Microsoft-365-groups-to-specific-IT-Glue-groups-or-users) * [Limit access to security groups to specific IT Glue groups or users](#Limit-access-to-security-groups-to-specific-IT-Glue-groups-or-users)   Available only for **Orphaned** or **Disabled** groups. The trash can icon allows you to delete the group upon confirmation. For details, refer to [Delete](#Delete). |

The **List View Options** icon  allows you to select which columns should be visible in the list. The columns can be reordered using the drag-and-drop tool  in the list options and resized within the table itself. The order and size of the columns will persist the next time the page is accessed. Click **Restore Defaults** in the list options to revert the list to its default column selections.

### Flexible assets for Microsoft Entra ID groups

The flexible asset for a synced Entra ID Microsoft 365 group or security group displays all its data synced from Microsoft to IT Glue.

The name of the Microsoft integration in IT Glue that manages the syncing of this group is listed next to the status icon. The green, yellow, or red status icon corresponds with the **Sync Status** column in the list of groups. For status descriptions, refer to [Sync Status](#Sync-Status).

A Network Glue administrator can export the documented group in IT Glue and create a runbook.

[Microsoft 365: Groups](#)

You can click the names of Microsoft members matched to IT Glue contacts to open their contact show pages in IT Glue. Unmatched members cannot be clicked, as no corresponding records exist in IT Glue. Matched members are also added as **Related Items** that cannot be deleted.

[Entra ID: Security Groups](#)

Microsoft members and devices matched to IT Glue contacts and configurations, respectively, can be clicked to open their contact and configuration show pages in IT Glue. Unmatched members and devices cannot be clicked, as no corresponding records exist in IT Glue. Matched members and devices are also added as **Related Items** that cannot be deleted.

### Action links

The following options are available as links in the lower-left corner of the flexible asset:

| Action | Description |
| --- | --- |
| Manage | An IT Glue Manager or Administrator can open the group page in Microsoft Entra ID. |
| Enable sync/Disable sync | An IT Glue Manager or Administrator can disable the sync for this individual group (by clicking **Disable sync**). Upon doing so, the group status will change to **Disabled**, and the group will no longer be updated in IT Glue as part of future syncs. The group will remain available in the list of groups, and its sync can be reenabled (by clicking **Enable sync**). |

### Action buttons

The following options are available in the upper-right corner of the flexible asset:

| Action | Description |
| --- | --- |
| Edit | The default fields in the **Microsoft 365: Groups** or **Entra ID: Security Groups** flexible assets, which pull data from Microsoft, cannot be edited. If an administrator wishes to edit any group data pulled from Microsoft, they must do so in Microsoft Entra ID, which is the source of truth in this integration. All other fields are not grayed out and can be edited. To learn how to edit the flexible asset type (the template itself), refer to the following how-to steps:   * [View and edit the Microsoft 365: Groups flexible asset type](#View-and-edit-the-Microsoft-365:-Groups-flexible-asset-type) * [View and edit the Entra ID: Security Groups flexible asset type](#View-and-edit-the-Entra-ID:-Security-Groups-flexible-asset-type)   In the **Security** section, you have the option to specify which IT Glue users should have access to this group. For instructions, refer to the following how-to steps:   * [Limit access to Microsoft 365 groups to specific IT Glue groups or users](#Limit-access-to-Microsoft-365-groups-to-specific-IT-Glue-groups-or-users) * [Limit access to security groups to specific IT Glue groups or users](#Limit-access-to-security-groups-to-specific-IT-Glue-groups-or-users) |
| PDF | Downloads a PDF file of the group flexible asset to the default download location on the user's device. |
| Delete | A Network Glue administrator can delete the group only if it has either the **Orphaned** or **Disabled** status. If the status is **Enabled**, this option is grayed out. Refer to [Sync Status](#Sync-Status). Upon deleting a group, it will no longer be synced to IT Glue in subsequent syncs, no longer be automatically documented in IT Glue, and no longer appear in the list of synced groups in IT Glue. This action will not delete the group in Microsoft Entra ID. |
| New | A Network Glue administrator can create a new **Entra ID: Security Group** or **Microsoft 365: Group** in IT Glue, but this group and its fields you enter values for will *not* be synced to Microsoft Entra ID. A group created in IT Glue will not be included in future Microsoft integration syncs. |
| Archive | A Network Glue administrator can archive the group, which will cause its status to change to **Orphaned**. While archived, a group is not updated in IT Glue as part of integration syncs, but it can be unarchived at any time (changing it to **Enabled**) or can be deleted (changing it to **Disabled**). Refer to [Sync Status](#Sync-Status). Archived groups are hidden from the list of groups unless the **Include archived** check box is selected. |

## How to...

[Sync Microsoft 365 groups and/or security groups to IT Glue](#)

To use the Microsoft Entra ID auto-documentation feature, enable the applicable setting(s) in IT Glue as follows:

1. From the top navigation menu, click **Admin**.
2. From the left navigation menu, navigate to **Account > Integrations**.
3. From the more menu  in the Microsoft connector, select **Sync Settings**.
4. In the **Microsoft Entra ID Sync** section, select the **Sync Microsoft 365 Groups** and/or **Sync Entra ID Security Groups** check boxes.
5. A **Warning** dialog box will inform you that syncing Microsoft Entra ID security groups can create duplicate Active Directory groups if you've set up Microsoft Entra Connect. Click **Confirm** to proceed with syncing security groups. Clicking **Cancel** causes the applied changes to not be saved and disables the **Sync Entra ID Security Groups** check box.

IMPORTANT  If you enable the **Sync Entra ID Security Groups** setting and have Microsoft Entra Connect set up, both Microsoft Entra ID security groups and Active Directory groups will be automatically documented in the **Entra ID: Security Groups** flexible asset type. If you haven’t set up Microsoft Entra Connect, this setting will automatically document only security groups.

6. Click **Save**.

NOTE  If you do not have a Network Glue subscription, the sync between Microsoft Entra ID groups and IT Glue will be established. However, the corresponding flexible asset types will be hidden in IT Glue, and administrators will not be able to export groups via either manual or scheduled runbooks.

[View and edit the Microsoft 365: Groups flexible asset type](#)

Enabling the **Sync Microsoft 365 Groups** setting in the Microsoft integration sync settings creates a new flexible asset type in IT Glue named **Microsoft 365: Groups**, which cannot be deleted.

NOTE  If your Network Glue subscription is deactivated, this flexible asset type is automatically hidden from the **Flexible Asset Types** list.

After the first successful sync, this flexible asset type is available to be added to the left navigation menu for organizations (**Admin > Settings > General > Customize Sidebar**) in the **Apps & Services** section. Refer to [Organizations sidebar](../../2-using/organizations/organizations-sidebar.html).

To access this flexible asset type, complete the following steps:

1. From the top navigation menu, click **Admin**.
2. From the left navigation menu, click **Flexible Asset Types**.
3. Click the **Microsoft 365: Groups** flexible asset type in the list.

The default fields, which pull data from Microsoft, cannot be edited. If an administrator wishes to edit any group or its fields pulled from Microsoft, they must do so in Microsoft Entra ID, which is the source of truth in this integration. All other fields are not grayed out and can be edited.

You have the option to select the icon displayed for this flexible asset type, hide this flexible asset type from the left navigation menu, and add custom fields.

If you make any changes, click **Save**.

[View and edit the Entra ID: Security Groups flexible asset type](#)

Enabling the **Sync Entra ID Security Groups** setting in the Microsoft integration sync settings creates a new flexible asset type in IT Glue named **Entra ID: Security Groups**, which cannot be deleted.

NOTE  If your Network Glue subscription is deactivated, this flexible asset type is automatically hidden from the **Flexible Asset Types** list.

After the first successful sync, this flexible asset type is available to be added to the left navigation menu for organizations (**Admin > Settings > General > Customize Sidebar**) in the **Apps & Services** section. Refer to [Organizations sidebar](../../2-using/organizations/organizations-sidebar.html).

To access this flexible asset type, complete the following steps:

1. From the top navigation menu, click **Admin**.
2. From the left navigation menu, click **Flexible Asset Types**.
3. Click the **Entra ID: Security Groups** flexible asset type in the list.

The default fields, which pull data from Microsoft, cannot be edited. If an administrator wishes to edit any group or its fields pulled from Microsoft, they must do so in Microsoft Entra ID, which is the source of truth in this integration. All other fields are not grayed out and can be edited.

You have the option to select the icon displayed for this flexible asset type, hide this flexible asset type from the left navigation menu, and add custom fields.

If you make any changes, click **Save**.

[View the Microsoft 365: Groups flexible asset for a group](#)

1. From the top navigation menu, click **Organizations**.
2. Select an organization that is matched to a Microsoft tenant. Refer to [Review sync and match Microsoft tenants to IT Glue organizations](microsoft-integration.html#Review-sync-and-match-Microsoft-tenants-to-IT-Glue-organizations) in [Microsoft Integration](microsoft-integration.html).
3. From the left navigation menu, click **Microsoft 365: Groups**. Refer to [Lists of Microsoft Entra ID groups](#Lists-of-Microsoft-Entra-ID-groups).

NOTE  To learn how to add this flexible asset to the left navigation menu for an organization, refer to [Organizations sidebar](../../2-using/organizations/organizations-sidebar.html).

4. In the **Group Name** column, click the name of the group for which you want to view the flexible asset. Refer to [Flexible assets for Microsoft Entra ID groups](#Flexible-assets-for-Microsoft-Entra-ID-groups) .

[View the Entra ID: Security Groups flexible asset for a group](#)

1. From the top navigation menu, click **Organizations**.
2. Select an organization that is matched to a Microsoft tenant. Refer to [Review sync and match Microsoft tenants to IT Glue organizations](microsoft-integration.html#Review-sync-and-match-Microsoft-tenants-to-IT-Glue-organizations) in [Microsoft Integration](microsoft-integration.html).
3. From the left navigation menu, click **Entra ID: Security Groups**. Refer to [Lists of Microsoft Entra ID groups](#Lists-of-Microsoft-Entra-ID-groups).

NOTE  To learn how to add this flexible asset to the left navigation menu for an organization, refer to [Organizations sidebar](../../2-using/organizations/organizations-sidebar.html).

4. In the **Group Name** column, click the name of the group for which you want to view the flexible asset. Refer to [Flexible assets for Microsoft Entra ID groups](#Flexible-assets-for-Microsoft-Entra-ID-groups) .

[Limit access to Microsoft 365 groups to specific IT Glue groups or users](#)

By default, all IT Glue users with access to a selected organization can access a group part of that organization. To grant access to specific IT Glue users instead, complete the following steps:

1. From the top navigation menu, click **Organizations**.
2. Select an organization that is matched to a Microsoft tenant. Refer to [Review sync and match Microsoft tenants to IT Glue organizations](microsoft-integration.html#Review-sync-and-match-Microsoft-tenants-to-IT-Glue-organizations) in [Microsoft Integration](microsoft-integration.html).
3. From the left navigation menu, click **Microsoft 365: Groups**.
4. For the group you wish to edit, click the edit icon  in the list. Alternatively, click the group name and click **Edit** in the upper-right corner of the flexible asset page.
5. In the **Security** section at the bottom of the page, select **Specific Groups and/or Users can access this Microsoft 365: Group**.
6. Select the check box(es) for the IT Glue group(s) or user(s) you wish to grant access to. Expand the drop-down menus to select specific groups or users. Or, select the **Select All** check box for a certain group or group of users to grant access to all users belonging to that segment.
7. Click **Save**.

[Limit access to security groups to specific IT Glue groups or users](#)

By default, all IT Glue users with access to a selected organization can access a group part of that organization. To grant access to specific IT Glue users instead, complete the following steps:

1. From the top navigation menu, click **Organizations**.
2. Select an organization that is matched to a Microsoft tenant. Refer to [Review sync and match Microsoft tenants to IT Glue organizations](microsoft-integration.html#Review-sync-and-match-Microsoft-tenants-to-IT-Glue-organizations) in [Microsoft Integration](microsoft-integration.html).
3. From the left navigation menu, click **Entra ID: Groups**.
4. For the group you wish to edit, click the edit icon  in the list. Alternatively, click the group name and click **Edit** in the upper-right corner of the flexible asset page.
5. In the **Security** section at the bottom of the page, select **Specific Groups and/or Users can access this Entra ID: Security Group**.
6. Select the check box(es) for the IT Glue group(s) or user(s) you wish to grant access to. Expand the drop-down menus to select specific groups or users. Or, select the **Select All** check box for a certain group or group of users to grant access to all users belonging to that segment.
7. Click **Save**.

## Microsoft Entra ID groups in the Activity Log

The Activity Log documents all instances of a manual change to Entra ID flexible assets, including the following:

* A Microsoft 365 or security group flexible asset was updated.
* A Microsoft 365 or security group flexible asset was archived.
* A Microsoft 365 or security group flexible asset was deleted.
* A Microsoft 365 or security group row was deleted.

## Removing the sync of Microsoft Entra ID groups

If you've previously synced Entra ID Microsoft 365 groups or security groups and wish to clear these check boxes in the sync settings, the sync between the groups and IT Glue organizations will be paused and no longer updated.

The corresponding flexible asset types will remain visible in the left navigation menu of a selected organization.

All data related to the previously synced groups will remain visible for IT Glue users and will not be deleted or archived.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
