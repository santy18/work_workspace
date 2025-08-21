---
title: "About roles and permissions"
source: "https://help.itglue.kaseya.com/help/Content/2-using/permissions/about-roles-and-permissions.html"
crawled_at: "2025-08-18T21:14:44.664045Z"
---

v1.118.88

# About roles and permissions

Each type of user role in IT Glue offers certain permission levels for available actions. Administrator and Manager users can assign roles to users on the user creation and editing pages.

## Administrator

Users with this permission level control the highest-level security and account settings and have access to all IT Glue data. We recommend that most teams have only a couple of Administrators. The first user to start a new account is given an Administrator role. Administrators added subsequently can change the role of the first user if needed.

## Manager

Managers can manage users and handle most administrative tasks, plus create, edit, and delete data within the organizations that they have permission to access. Certain destructive actions (for example, permanently deleting data) are permitted.

If these users have restricted access to organizations for any reason, they are not able to create new organizations.

## Editor

Editors can create, edit, and delete data within the organizations that they have permission to access, plus set asset permissions, controlling which other users have access to that asset.

If these users have restricted access to organizations for any reason, they are not able to create new organizations.

## Creator

Creators can create and edit data within the organizations that they have permission to access, plus set asset permissions, controlling which other users have access to that asset.

If these users have restricted access to organizations for any reason, they are not able to create new organizations.

## Read-only

Users with this permission level can only view data within the organizations that they have permission to access. This role is read-only.

## Lite

Users with this permission level can only view data within the organizations that they have permission to access. This role is read-only and is only allowed access to up to five organizations/sub-organizations. This role is ideal for clients you invite to your account.

For reference, the following table summarizes the different permission levels:

## Comparing Manager and Administrator roles

As follows is a quick overview of the Manager and Administrator roles.

### Managers

Managers can perform these administrative actions in the account:

* Turn on single-sign on (SSO) for all users
* Update billing
* Invite/edit/remove users (except Administrator roles)
* Manage user groups (except groups that they are not a member of)
* Create/edit/delete flexible asset templates
* Edit the organization sidebar
* Enable integrations and features
* Access sync settings and data management screens associated with PSA and RMM integrations
* View detailed activity logs
* Import data (requires access to all organizations)

### Administrators

Administrators have all the same administrative rights and permissions as Managers but with the following additions:

* Turn on enforced multifactor authentication (MFA) for all users
* Reset MFA for users
* Generate API keys for IT Glue API and Warranty Master API
* Configure GlueConnect
* View and share the Passwords Accessed report
* Export IT Glue data
* Full visibility to all IT Glue data; an all-access pass to the account (regardless of access settings)

Because the Manager and Administrator roles are highly privileged, [enabling multi-factor authentication](../your-user-account/set-up-multi-factor-authentication-mfa.html) to increase the level of security is strongly recommended.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
