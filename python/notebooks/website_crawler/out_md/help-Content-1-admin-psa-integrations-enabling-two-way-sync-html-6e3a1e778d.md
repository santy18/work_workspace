---
title: "Enabling two-way sync"
source: "https://help.itglue.kaseya.com/help/Content/1-admin/psa-integrations/enabling-two-way-sync.html"
crawled_at: "2025-08-18T21:14:31.618837Z"
---

v1.118.88

# Enabling two-way sync

*For partners subscribed to Select or Enterprise plans.*

If you are integrated with ConnectWise, Autotask, or BMS follow the steps below to turn on two-way sync. Two-way sync allows you to update field values that are syncing with your PSA directly in IT Glue. These changes will then immediately push to your PSA.

For an introduction to syncing between your PSA and IT Glue, see [Syncing between IT Glue and PSAs overview](syncing-between-it-glue-and-psas-overview.html).

## Prerequisites

* You must have Manager or Administrator access to IT Glue.
* An integration with Autotask, ConnectWise, Kaseya BMS, Pulseway PSA or Vorex PSA. Two-way syncing is currently available for only these PSAs.

## Instructions

1. Navigate to **Account > Integrations**. Click on **Actions > Sync Settings.**
2. Click the **Two-Way Sync Settings** tab. Select the **Enable two-way sync** checkbox. For partners with Network Glue and Active Directory enabled, configure your contact attributes so that new contacts created from Active Directory are automatically pushed to your PSA (refer to the *Syncing IT Glue Contacts created with Active Directory user data section* in this KB).

   In the **Contacts** section, select the contact attributes from your PSA that will be applied to new contacts you create. If you do not select an email or phone type, the contact will be pushed without email or phone data with the exception of Kaseya BMS. In BMS, if the email type is not selected, contacts will not be pushed.
3. Click **Save**.

After you turn on two-way sync, any updates that are made to mapped fields will immediately push to your PSA. With one-way sync, select synced fields were read-only because data coming from the PSA was prioritized over the data in IT Glue.

NOTE  If you had existing Organizations, Configurations, Contacts, or Locations populated in your PSA that also exist in IT Glue, you must edit and save each asset individually to trigger the two-way sync. Enabling the two-way sync alone will **not** automatically push these assets. See the *Common Questions* section in this KB for more details.

NOTE   If you are switching PSAs or adopting one for the first time, you can complete a one-time push to have all your IT Glue data synced at once. As IT Glue is your single source of truth, this push allows you to quickly sync all your well-documented assets in one go rather than having to manually edit, save, and push each one before completing a sync. Refer to our [Pushing all syncable assets to PSA](pushing-all-syncable-assets-to-psa.html) topic for more details.

### Syncing IT Glue Contacts created with Active Directory user data

For our partners who have Network Glue, you can create contacts from [Active Directory](../../4-network-glue/using-network-glue/setting-up-network-glue-for-an-it-glue-organization.html) data if it was enabled during set up. For instructions on how to do so, refer to our [Setting up Network Glue for an IT Glue organization](../../4-network-glue/using-network-glue/setting-up-network-glue-for-an-it-glue-organization.html) topic. If a created contact matches your PSA’s sync requirements, then a PSA badge will appear in the Contact show page. To ensure your created contacts match your PSA’s sync requirements, refer to our [Enriching IT Glue Contacts with Active Directory user data](../../4-network-glue/using-network-glue/enriching-it-glue-contacts-with-active-directory-user-data.html) KB article for further details.

## Common Questions

**Will data already in IT Glue be pushed to my PSA?**

*If you currently have a PSA and it is populated:*

Turning on two-way sync is what allows any new IT Glue data in mapped fields to be pushed to your PSA. But, as a precautionary measure, two-way sync will not automatically push data that was already in IT Glue before you turned on two-way sync. Items not yet pushed will display the following message: *"Record not yet pushed to [PSA]. To trigger a push, try updating the record"*. You would need to edit and save these items one-by-one, which will then queue them to sync per our standard sync behavior.

While you are editing and saving, make sure that each organization or configuration's type and status are ones that are set to sync. Please note that for Autotask integrations, configuration items will also need field values for manufacturer and model.

*If you are switching to a new PSA or adopting a PSA for the first time:*

You can complete a one-time push to have all your IT Glue data synced to your PSA. As IT Glue is your single source of truth, this push allows you to quickly sync your well-documented assets in one go rather than having to manually edit, save, and push each one before completing a sync.

For details on how to complete a one-time push all of your syncable IT Glue assets into your PSA, refer to our [Pushing all syncable assets to PSA](pushing-all-syncable-assets-to-psa.html) topic for more details.

**How do I make imported data push to my PSA?**

*If you currently have a PSA and it is populated:*

Two-way sync was not intended for data imported from spreadsheets or added to your account via an integration to sync back to your PSA tool. Such data will need to be edited and saved one by one to trigger a push to your PSA tool.

The primary reason for not pushing such data automatically is to ensure that the integrity of the data stored in your PSA is not affected by bulk changes made in IT Glue. That could easily result in hundreds or thousands of records being duplicated or incorrectly updated.

*If you are switching to a new PSA or adopting a PSA for the first time:*

Since your new PSA is not populated, you can complete a one-time push to have all your IT Glue data synced at once. Please refer to our [Pushing all syncable assets to PSA](pushing-all-syncable-assets-to-psa.html) topic for more details on how to complete this action.

**Is automatic push supported for contacts created from an external integration ?**

New contacts are automatically pushed to an existing PSA from the data source they were created from (that is, manually or via the API). CSV is the only external data source that automatic push does not support. Contacts created from a .CSV file will require an edit/save action to force the push. You must have two-way sync enabled, and contacts must meet the push criteria.

**A company added to IT Glue isn't showing up in our PSA. How do I begin troubleshooting?**

As you work with your data in both systems, remember that the type and status fields are integral to PSA sync logic. The most common reason for something in IT Glue not populating in your PSA is that the type and status are set to a type or status that is not set to sync. To fix this, edit the organization to update the type or status to ones that are syncing.

You might want to read the [Overview of client onboarding steps](../../2-using/documentation-guide/overview-of-client-onboarding-steps.html) topic, which has a good overview of the best practices for entering information about new clients.

**What is the sync frequency and duration?**

After you follow the instructions to enable two-sync, any updates to a mapped field in IT Glue will always be immediately pushed to your PSA.

The initial sync with your PSA tool typically completes in under an hour, but a sync job may wait in the queue for a longer time, depending on the system load and how many new items you have. At any time, a manual sync can be scheduled (from **Account > Integrations**), which will prioritize the sync to start sooner.

## Related articles

* [Syncing between IT Glue and PSAs overview](syncing-between-it-glue-and-psas-overview.html)

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
