---
title: "Control access with security permissions"
source: "https://help.itglue.kaseya.com/help/Content/2-using/permissions/control-access-with-security-permissions.html"
crawled_at: "2025-08-18T21:14:39.785820Z"
---

v1.118.88

# Control access with security permissions

We encourage you to familiarize yourself with how the security permissions work.

## Managing permissions

In IT Glue, there are several different types of permissions that are managed separately but work together to provide the proper security permissions.

* Organizations: Permissions are managed at the user or group level.
* Assets: Permissions are managed at the asset-level.
* Asset Types: Permissions are managed at the group level.
* Users: Permissions to be able to perform a set of actions are managed through user roles.

## What makes up a user's permissions

User permissions are the *total* permissions from various permissions.

When IT Glue determines a user's permissions, it considers the following top-level permissions:

|  |  |
| --- | --- |
| **Organizations** | [Organizations](../organizations/about-organizations.html) are secure containers for all of a business's assets. Each organization is private, visible only to those users who have been explicitly granted access to it. |
| **Groups** | [Groups](../../1-admin/users-and-groups/adding-and-removing-users.html) are used to manage groups of users for easy administration of organization and asset security permissions, and also to [restrict access to asset types](about-permissions-for-asset-types.html). Individual users who are members of a group will inherit the group's permissions. |
| **Roles** | [Roles](about-roles-and-permissions.html) are used to define how logged-in users can interact with the data in your account. Each user is assigned a pre-defined user role that gives them permission to perform a set of actions. |

The Account tab is where all of the top-level permissions are set. You can't see the Account tab unless you have a Manager or Administrator role.

Keep in mind that Managers may have only limited access to some Account features. For example, they can only manage groups that they themselves are a member of. Administrators, on the other hand, have free rein of all Account settings.

## Permissions for assets

For every asset created in IT Glue, there is a set of permissions that allows access to that asset. Anyone with a Creator or above role can edit an asset's permissions. For more on asset-level permissions, see [Editing an asset's permissions](edit-an-asset-s-permissions.html).

## Viewing asset permissions

You can see the resulting permissions for any asset when you view it in list view. From [Global > Assets](../get-to-know-it-glue/view-global-lists.html), you can navigate to any type of asset to see permissions across all organizations. This gives you the ability to conduct audits of asset permissions.

Hover over the padlock icon to see who can access that asset. When the padlock is open, the permissions associated with that asset are the same as the organization’s. When the padlock is closed, there have been changes to a person’s or group’s access to that password.

## Related documentation

From time to time, something happens that requires you to answer the "who did it?" question. There are a few different ways you might look for the answer depending on the nature of the change:

* [Activity Logs](../../1-admin/account-administration/activity-logs.html) - See who created, edited, viewed, or deleted data.
* [Passwords accessed reporting](../../1-admin/engagement-and-reporting/viewing-the-at-risk-password-report.html) - Run a report that lists all passwords that have been accessed by a specific user.
* [Revision history](../get-to-know-it-glue/revisions-to-core-and-flexible-assets.html) - View the revision history of an asset to see who has made changes and, if necessary, go into the revision history to revert the changes.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
