---
title: "Structure and navigation"
source: "https://help.itglue.kaseya.com/help/Content/2-using/get-to-know-it-glue/structure-and-navigation.html"
crawled_at: "2025-08-18T21:14:11.485120Z"
---

v1.118.88

# Structure and navigation

The purpose of this topic is to help you familiarize yourself with the structure of IT Glue and some of the basic navigational tools that are included in the app.

## Touring the interface

The top navigation bar can help you navigate the different sections of the app. Not all users see the same navigation bar. Global and Account are not universal options.

**Dashboard** - Where you'll find your favorite organizations and various feeds, including things you've recently updated and any organizations that have been updated by your team in the past week.

**Organizations** - One central location for finding all your organizations. At the top of the screen are your favorite organizations.

**Personal** - Where you can access checklists and checklist tasks that are assigned to you. Passwords with the security set to Only me will also be found here.

**Global** - Where you can view progress/completion statistics, see and manage data stored for your account across all organizations that you can access, and view all items that have an expiration date. If you are integrated with Datto, you can also view device backup details (currently only shown to Managers and Administrators). Note that the Global area is always hidden from users with a Lite role.

**Account** - Where you can update your billing information, switch your plan, add users and groups, and more. Only users with a Manager or Administrator role can view the Account area. For more information, see [Account settings for Managers and Administrators](../../1-admin/getting-started/account-settings-for-managers-and-administrators.html).

**Search** - Where you can search for specific information. To perform a search, choose the search field or press the / (forward slash) key on your keyboard to place your cursor in the search field. Type the name of a configuration item, person, document, domain, or organization, and then choose from the list of options displayed. For more information about how to search, refer to our [[Search and search filters](search-best-practices.html)](search-best-practices.html) topic.

**Recently Viewed** - Where you find things you've recently visited. When you click on the recently viewed (clock) icon, a drop-down menu will show you the last nine items you viewed. Click on an item or press the number that's displayed to the right of an item to be taken to one of the pages you want to revisit. Press the . (period) key on your keyboard to quickly open and close this menu.

**Help Menu -** Where you can access our knowledge base, view video tutorials, submit a feature idea, view system status, privacy policy, terms of service, and product updates (Release Notes) of previous releases.

**User Name Menu** - Where you can access our knowledge base, [submit a feature idea](../miscellaneous/feature-request-portal.html), [[edit your profile](../your-user-account/edit-your-profile.html), switch](../your-user-account/edit-your-profile.html). Click on your name in the top right of the top navigation bar and choose an option from the drop-down menu.

**Footer** - Where you'll find links to our privacy policy, [terms of service](https://www.itglue.com/terms), [knowledge base](https://support.itglue.com/hc/en-us), and [release notes](https://helpdesk.kaseya.com/hc/en-gb/categories/4406076882449). If you don't see the footer, it means it's been hidden at the account level.

You'll also find a floating green **Support** button at the bottom of the screen, which you can use to submit support requests.

### Organizations

Organizations are used to contain all information about clients. Your clients' vendors can be included as individual organizations to help you manage vendors. Your own company is also its own organization.

Clicking on **Organizations** from the top navigation takes you to a screen that lists all the organizations that you have access to, as well as your favorite organizations. You can also search organizations from this screen. Clicking on an organization's name takes you straight there.

Other actions you can perform from the Organizations list view:

|  |  |
| --- | --- |
| **Option** | **Description** |
|  | Opens the organization in edit mode. |
|  | Favorites the organization, which moves it to your Dashboard and anywhere there is section for your favorite organizations. |
|  | Deletes the organization. If the icon is grayed out, you can delete the organization only after opening it and stopping it from syncing. |

Other ways you can find an organization:

* Clicking on **Dashboard** from the top navigation provides a quick way to navigate to your favorite organizations and displays various feeds with links to organizations you can access.
* From anywhere in the app, you can search for an organization by its name or its short name (if set up).

## Organization home page

Every organization's home page is a dashboard that provides a quick way to navigate and see the recently updated items, as well as any items that you've recently viewed for that organization. The home page also shows you the most frequently viewed passwords and upcoming expirations. Any contacts that are starred for that organization are displayed as important contacts.

The home page also shows you any optional notes that have been entered for that client:

* **Alerts** are short, brightly colored messages that are entered from the Edit Organization screen and are visible to all users.
* **Quick notes** are messages (short or long) that are entered directly from the organization home page and are visible to everyone except users with a Lite role.

## Organizations sidebar

The left-hand sidebar that you see when you navigate organizations provides access to different areas within the organization.

The following group headings are usually used to organize the sidebar, though different headings may have been chosen:

|  |  |
| --- | --- |
| **Group Heading** | **Description** |
| **Core Assets** | Your most frequently accessed assets: configurations, contacts, documents, domains, SSL, locations, and passwords. |
| **Apps & Services** | Contains flexible assets (e.g. Applications, LAN, File Sharing), which provide comprehensive information about your managed services, in a structured format. |
| **Administration** | Non-technical information such as sales/finance, licensing, and operational information. |

## List views

Throughout IT Glue, list views are used to display information. These list views can be filtered, sorted, and searched to meet your needs.

For **Configurations**, **Contacts**, **Documents**, **Domains**, **Locations**, and **SSL Tracker** assets, any column filters and/or keyword searches are remembered by the platform until you choose to clear or change them. This allows you to drill in and out of data in the asset without having to re-enter the same filter/search values each time, saving you time and effort.

**What the icons and indicators mean**

This table describes the most commonly encountered icons and their meanings:

|  |  |  |
| --- | --- | --- |
| **Icon** | **Name** | **What it means** |
|  | **Sync enabled** | Indicates that the item meets the minimum sync requirements and is available for syncing. |
|  | **Orphaned data** | Indicates that the item is no longer syncing with your PSA. Reasons may include that the item's type or status is not enabled in your sync settings or that the item was deleted from your PSA. |
|  | **Sync disabled** | Indicates that someone on your team has disabled syncing on that item, probably in anticipation of deleting it. |
|  | **Error** | When the PSA sync encounters an error it cannot automatically recover from, it will display an error state. Open the item to view the full sync error message under the PSA sync status section. |
|  | **Padlock open** | If the padlock icon is open, the item inherits its organization-level security permissions. You can hover over the padlock icon to see who on your team has access to that item. |
|  | **Padlock closed** | When the item is secured beyond the default-level permissions, the padlock icon is closed. Hover your mouse over the padlock icon to see who in your team has access. |
|  | **Trash** | Deletes the item. If the icon is grayed out, you can delete the item only after opening it and stopping it from syncing. |
|  | **Edit** | Opens the item in edit mode. |

### Side panel

Throughout the app, a side panel appears on the right side of the screen that can be used to add and access other important information about assets:

|  |  |
| --- | --- |
| **Section** | **Description** |
| **Attachments** | The Attachments section allows you to drag/drop or upload from your computer an unlimited number of files of any type. The maximum attachment size is 100MB. |
| **Embedded Passwords** | [Embedded passwords](../security/choosing-between-general-and-embedded-passwords.html) are designed to be used in cases where the password only exists in the context of that asset. |
| **Related Items** | [Related items](relationship-mapping-related-items-tagging.html) are a way to create logical relationships between items to get a full picture of the client's IT environment. |
| **Revisions** | The [Revisions](revisions-to-core-and-flexible-assets.html) section shows you up to five of the most recent updates, the date and time of each change, and the name of the person who made the change. This section is only available for configurations, contacts, documents, domains, SSL, locations, and passwords. |

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
