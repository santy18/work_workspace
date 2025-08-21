---
title: "IT Glue glossary of common terms"
source: "https://help.itglue.kaseya.com/help/Content/2-using/get-to-know-it-glue/it-glue-glossary-of-common-terms.html"
crawled_at: "2025-08-18T21:14:06.854801Z"
---

v1.118.88

# IT Glue glossary of common terms

This glossary defines a number of key terms you will see used often in the knowledge base.

|  |  |
| --- | --- |
| **Account Admin Rights** | [Administrators and Managers](../permissions/about-roles-and-permissions.html) have administrative powers, such as managing users and groups, adding integrations, and other account maintenance tasks. They can have full admin rights (Administrator user role) or partial (Manager user role). To minimize downtime and accidental changes to cloud resources, the number of users with admin rights should be limited to only a few people. |
| **Configurations** | Configurations are typically network-attached devices/assets (physical or virtual) - in other words, anything with an IP address. Configurations can also be pieces of hardware that need to be controlled and managed but that do not have IP addresses, for example, a display, camera, security panel/alarm, or backup power supply. Configuration fields are limited to the physical attributes of the device. |
| **Core Assets** | Core assets are the physical and non-physical components that contribute to a managed service: configurations, contacts, locations, passwords, etc. To ensure compatibility with PSA and RMM sync requirements, core assets are standardized and not customizable. Flexible assets let you track additional information about your assets that the default asset attributes don’t cover. |
| **Documents** | Documents are procedures and longer reference documentation, for example, “How to install QuickBooks”. |
| **Flexible Assets** | [Flexible assets](introduction-to-flexible-assets.html) are structured documentation that can be completely customized to support the data entry and workflow processes that will be followed by your team. For example, if you offer a backup service, then the details of your service can be documented as a flexible asset that has comprehensive information about that service such as client-specific business rules, checklists, and reference material. |
| **Flexible Asset Templates** | Several pre-built templates, including Applications, Licenses, and Virtualization, are provided in the app. We designed them to be used "out-of-the-box" but a best practice is to customize them for your data entry and workflow processes. |
| **Groups** | [Groups](../../1-admin/users-and-groups/adding-groups-group-members.html) are a secure method of [controlling access](../permissions/control-access-with-security-permissions.html) to information. Determining how groups are used is an essential part of deploying IT Glue. |
| **Import** | User-activated, one-way pull of information from an external source. To [import CSV data](../../1-admin/import-and-export/importing-csv-data-into-your-account.html), you must have an Administrator role, or a Manager role that has access to all organizations. |
| **IT Glue Library** | The [IT Glue Library](../../1-admin/other-integrations/importing-the-it-glue-library.html) is an in-app library that provides processes and topics on how to successfully design and run your MSP. You can browse the articles as written, or alter them for your own context. |
| **Multi-factor authentication** | [Multi-factor authentication (MFA)](../your-user-account/set-up-multi-factor-authentication-mfa.html) adds an extra layer of protection for your IT Glue account. When a user logs in to IT Glue with MFA enabled, they will be prompted for an authentication code from their MFA device in addition to their user name and password. Taken together, these multiple factors provide increased security for your account and resources. |
| **Passwords** | Passwords are where you can put all of your network and server login credentials. Passwords can be added under the main Passwords section, or they can be added as device-specific (embedded on the device) passwords. For more information, see [[general and embedded passwords](../security/choosing-between-general-and-embedded-passwords.html)](../security/choosing-between-general-and-embedded-passwords.html). Be cautious about who has access to passwords to ensure that you don't give access to users and groups who should not be provided access. |
| **Primary organization** | Your business is termed as the primary organization. The primary organization is automatically set based on the business name used to create your account. |
| **Related items** | [Related items](relationship-mapping-related-items-tagging.html) are a way to create logical relationships between items to get a full picture of the client's IT environment. |
| **Roles** | [Roles](../permissions/about-roles-and-permissions.html) define the type of access granted to a user. Roles consist of a logical group of special permissions that are pre-defined. There are six roles: Administrator, Manager, Editor, Creator, Read-only, and Lite. |
| **Single sign-on** | [Single sign-on (SSO)](https://helpdesk.kaseya.com/hc/en-gb/sections/4406285461521) is a process that permits someone to enter their name and password from one system (like AuthAnvil) in order to access their IT Glue account, without needing to also enter their IT Glue credentials. |
| **Sub-organizations** | [Sub-organizations](../organizations/when-to-use-sub-organizations.html) are a way to isolate a parent organization (UPS) from smaller child organizations (UPS - Detroit, UPS - New York, UPS - Chicago), so that configurations and other information can be displayed within their sub-organizations. |
| **Sync** | [Sync](../../1-admin/psa-integrations/syncing-between-it-glue-and-psas-overview.html) means that you only have to make changes to synced data once. For example, if you are set up for a one-way sync with a PSA, select synced fields are read-only in IT Glue. Any changes made in your PSA to fields that are syncing with IT Glue will be pushed to IT Glue during the next data load. |
| **Two-way sync** | [Two-way sync](../../1-admin/psa-integrations/enabling-two-way-sync.html) provides bi-directional maintenance of synced data between your PSA and IT Glue. It allows you to edit and update synced data directly in IT Glue and immediately push the update to your PSA. |
| **Timestamps** | Timestamps show you the exact dates and time of activity that took place in IT Glue, such as when a document was published. Make sure that you [update your time zone](../your-user-account/edit-your-profile.html). This setting affects timestamps in activity logs. |
| **Workflows** | [Workflows](../../1-admin/workflows/quick-guide-for-workflows.html) are a way for IT Glue to notify you about items that need your attention, such as updates about expiration dates and other IT Glue activity. You can receive notifications by email or through integrations with third-party activity feeds. |

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
