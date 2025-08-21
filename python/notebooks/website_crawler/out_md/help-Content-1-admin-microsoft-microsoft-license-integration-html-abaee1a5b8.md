---
title: "Microsoft Integration: Syncing Microsoft licenses with IT Glue"
source: "https://help.itglue.kaseya.com/help/Content/1-admin/microsoft/microsoft-license-integration.html"
crawled_at: "2025-08-18T21:14:27.652273Z"
---

v1.118.88

# Microsoft Integration: Syncing Microsoft licenses with IT Glue

To sync your Microsoft licenses with IT Glue you must first integrate and match your tenants. Refer to [Microsoft Integration](microsoft-integration.html).

1. Navigate to **Admin > Integrations > Microsoft Actions > Sync Settings**.
2. From the **Sync your data with Microsoft** screen, click the checkbox for **Licenses**. Then, click the **Save** button.

   NOTE  Selecting the **Licenses** checkbox will sync in all licenses from Microsoft regardless of what is checked in the list of licenses for the Microsoft users you decide to sync in.
3. From the **Active Integrations** screen (**Admin > Integrations**), click **Actions** and then **Start Manual Sync**.
4. Check the **Active Integrations** screen again. The overall sync status will change from **Syncing...** to **OK** when the sync is complete.

### Syncing Licenses

Microsoft licenses are synced as a flexible asset in IT Glue.

NOTE  If this is your first Microsoft integration, a new Flexible Asset Type named “Microsoft Licenses” will be created and formatted to display your Microsoft licensing data within Organizations. **This synced Flexible Asset Type, similar to synced Configuration Types, cannot be edited in order to protect the template of the synced Flexible Assets.**

Synced Microsoft License Flexible Assets, similar to other one-way synced assets, will have their synced fields locked to prevent editing. Security settings, however, will still be manageable when editing synced Microsoft License Flexible Assets.

### Viewing Licenses

IT Glue lets you track the number of Active, Consumed and Unused licenses at a glance.

After the licenses have synced, you can view licenses information by either visiting a matched organization and choosing the Microsoft Licenses flexible asset, or by viewing a Global list of Microsoft License flexible assets.

To view via an organization:

1. Select the organization you want to view and select Microsoft Licenses on the sidebar.
2. This will open the synced Microsoft Licenses list view.

### Viewing all Microsoft Licenses in the Global Page

1. Navigate to **Global > Microsoft Licenses**.
2. This opens the global list view of all synced tenants and license information.
3. You can filter or search for a particular Organization’s information using the filter options at the top of the list.

### Disconnecting Licenses

While removing an Microsoft integration, choosing the **"Permanently disconnect records from Microsoft but keep all data"** will stop syncing Flexible Assets and Flexible Asset Types and existing synced assets will be retained in your IT Glue account.

Choosing the **“Permanently delete all data including all related/child records”** option will delete all synced Flexible Assets and Flexible Asset Types.

For both options, any contacts or organizations created from the integration are not deleted.

### Special Considerations

Only Microsoft subscriptions that are active are counted as “Active” in IT Glue. Any managed subscriptions that are suspended will be reported as having 0 “Active” licenses in a synced Microsoft Licenses flexible asset. If an Microsoft tenant contains users that are assigned a suspended license, synced Contacts will still appear tagged in the flexible asset.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
