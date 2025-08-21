---
title: "When to use sub-organizations"
source: "https://help.itglue.kaseya.com/help/Content/2-using/organizations/when-to-use-sub-organizations.html"
crawled_at: "2025-08-18T21:14:49.367940Z"
---

v1.118.88

# When to use sub-organizations

This article is intended for account administrators. When thinking about how to use sub-organizations, there are a few points to consider.

Let's start by defining the key terms and then explain how sub-organizations can be useful.

**Organizations**

* Represent the top-level structure of clients and can have as many locations and sub-organizations as you want.
* Each asset or document can belong to only one organization and can be viewed by users who have access to that organization depending on the item's permissions.

**Sub-organizations**

* Sub-organizations are used to segment an organization so that there is a parent and one or more child sub-organizations. They can be used for locations or departments, if needed.
* Assets and documents can belong to the sub-organization (not the parent) and can be viewed by users with access to that sub-organization depending on the item's permissions.
* Sub-organizations do not inherit any permissions from their parent.

**Locations**

* Represent physical locations and addresses where the client's users may work.
* Each asset or document can be shown to exist in a particular location only if a relationship is created (tagging).

## When to use sub-organizations

With PSA syncing, IT Glue will automatically create sub-organizations if our sync logic detects parent-child relations coming from the PSA. A typical use for these child sub-organizations in your PSA is to bill to separate entities from the same client. In IT Glue, sub-organizations do not have a pre-defined use, and for your clients that are billed as one entity, organizations and locations will often be enough to match the desired structure.

However, as fully separate entities, sub-organizations may make it easier to manage location-based documentation for certain clients, for example, if the infrastructure used at one of the client's locations doesn't rely on the infrastructure of the parent organization. In this model, the documentation can be structured in a way that will match better with client infrastructure and with each location's documentation needs.

The ability to have defined access permissions is a secondary benefit of sub-organizations. For example, permissions can be managed such that an overarching authoritative user (client's CEO) can be granted permissions to the parent and all child sub-organizations, and conversely a user (project leader) can be granted access to just a sub-organization, and not to the parent.

## Navigating to sub-organizations

When viewing an organization's home page, you can see its sub-organizations by scrolling to the bottom of the screen. You can also search for a sub-organization by its name and navigate to it directly instead of going to the parent organization.

When you view a sub-organization, you'll see the top-level organization in the breadcrumbs navigation near the top of the screen.

For information about creating sub-organizations, see the following article:

* [Adding and deleting organizations](add-and-delete-organizations.html)

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
