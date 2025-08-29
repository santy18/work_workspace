---
title: "Syncing between IT Glue and PSAs overview"
source: "https://help.itglue.kaseya.com/help/Content/1-admin/psa-integrations/syncing-between-it-glue-and-psas-overview.html"
crawled_at: "2025-08-18T21:14:43.384871Z"
---

v1.118.88

# Syncing between IT Glue and PSAs overview

## Introduction

IT Glue fields automatically map into your PSA once an integration is successfully established.

See the articles below for information on how IT Glue fields map to fields in your PSA.

* [Autotask field mappings](integrating-with-autotask.html#Autotask-IT-Glue-field-mappings)
* [BMS field mappings](integrating-with-kaseya-bms.html#BMS-IT-Glue-field-mappings)
* [ConnectWise field mappings](connectwise-manage-field-mappings.html)
* [Pulseway PSA field mappings](psa-field-mappings.html)
* [Tigerpaw field mappings](tigerpaw-field-mappings.html) (configuration sync is not available for Tigerpaw integrations)

In these articles, you'll also find details on the matching logic that's used to determine whether to match records between the two systems.

NOTE  IT Glue uses an exact matching method that looks for strings that match exactly. Fuzzy matching (which looks for approximate matches based on patterns) is not supported.

## Creating organizations and configurations from PSA records

Most organization and configuration fields in IT Glue will sync with your PSA. The types and statuses that are enabled for syncing in IT Glue are integral to PSA sync logic. When a syncing type and status is assigned to an organization or configuration in your PSA, a new record is created in IT Glue after the next full sync.

If a matching organization or configuration is already in IT Glue, the records will sync and the one that is in IT Glue will be changed to reflect the information coming from the PSA. The PSA always wins this data syncing relationship.

## Creating contacts from PSA records

If the **Enable Contacts sync** setting is enabled in your sync settings (**Account > Integrations > [PSA] Actions > Sync Settings**tab) and a new contact is created in your PSA, a new contact will be created in IT Glue, assuming there is not already a contact in IT Glue with the same name in that organization. As previously mentioned, if there is a conflict between the two systems, the PSA will always win.

If the **Enable Contacts sync** setting is not enabled, IT Glue will not automatically create new contacts.

NOTE  IT Glue will create contacts that are associated with a configuration *only* if the contact in the PSA is also documented in the same client as the configuration. Any contacts documented outside of the client in the PSA are ignored during the sync.

## Network Glue

For our partners who have Network Glue, you can create contacts from Active Directory data if it was enabled during set up. For instructions on how to do so, refer to our [Setting up Network Glue for an IT Glue organization](../../4-network-glue/using-network-glue/setting-up-network-glue-for-an-it-glue-organization.html) topic.

If a created contact matches your PSA’s sync requirements, then a PSA badge will appear in the Contact show page and created contacts will be automatically pushed to your PSA. To ensure your created contacts match your PSA’s sync requirements, refer to our [Enriching IT Glue Contacts with Active Directory user data](../../4-network-glue/using-network-glue/enriching-it-glue-contacts-with-active-directory-user-data.html) topic for further details.

## Creating locations from PSA records

IT Glue syncs with location records (most fields) for ConnectWise, Kaseya BMS, and Tigerpaw. Whenever there is a conflict between the two systems, the PSA will always win.

## Two-way syncing

Two-way syncing is available for Autotask, ConnectWise, Kaseya BMS, and Pulseway PSA. With two-way syncing, IT Glue lets you update field values that are syncing with your PSA directly in IT Glue. These changes will then immediately push to your PSA.

When you enable two-way sync, this does not automatically push to your PSA any organizations, configurations, contacts, or locations that were in IT Glue before the first sync or that are imported later on. You would need to edit and save these as confirmation that you want these new items created in your PSA. See the [two-way sync](enabling-two-way-sync.html) article for more details.

## Pushing All Syncable Assets from IT Glue to PSA when switching to or adopting a new PSA

For partners who are switching to a new PSA solution or adopting their first PSA solution, you can request a one-time push to have all your data synced to your PSA. As IT Glue is your single source of truth, this push allows you to quickly sync your well-documented assets in one go rather than having to manually edit, save, and push each one before completing a sync. This feature is available if your PSA integration is capable of two-way syncing.

Refer to our [Pushing all syncable assets to PSA](pushing-all-syncable-assets-to-psa.html) KB article for more details.

## Related articles

* [Overview of client onboarding steps](../../2-using/documentation-guide/overview-of-client-onboarding-steps.html)

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
