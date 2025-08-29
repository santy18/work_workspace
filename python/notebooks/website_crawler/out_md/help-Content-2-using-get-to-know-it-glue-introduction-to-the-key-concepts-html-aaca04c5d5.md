---
title: "Introduction to the key concepts"
source: "https://help.itglue.kaseya.com/help/Content/2-using/get-to-know-it-glue/introduction-to-the-key-concepts.html"
crawled_at: "2025-08-18T21:14:14.348298Z"
---

v1.118.88

# Introduction to the key concepts

This is an introduction to the key concepts of IT Glue: Core Assets, Flexible Assets, and Documents. These are the foundations of the design and optimization of your entire account structure.

With IT Glue, you have a way to take the information that may be cluttering up other systems and structure it properly inside IT Glue, to provide a more effective organization of information to your team. You can think of IT Glue like adding a flexible shelving system to a cluttered home office. By organizing and labeling the shelves in a logical way, you're improving efficiency.

**In this guide, you'll learn how to create a structure that can be easily navigated**, which will help you eliminate the most frustrating aspect of any system: not being able to find information. You also don't want to run the chance of creating more information than is needed, spread out all over your account, by not spending any time designing the structure. If that happens, your team won't be able to find the information they need. Plus, with a well designed navigation system, you won't have the training headache later since the structure and the way information is stored will be very intuitive.

Video link: [Key Concepts](https://embed-ssl.wistia.com/deliveries/fb4ae65ac4d7935965b2fb419a7b97ea5c1b3dd6.bin)

In this guide, you'll learn:

* About Core Assets and where to populate them
* What are Flexible Assets and why should you use them
* Where to create your procedures and public facing documents
* Example of how to document a client's total email infrastructure

## Part 1: Start with the Core Assets

Core Assets are used to build and support the applications and services you manage for your clients. Core Asset forms and fields can't be modified or changed.

|  |  |
| --- | --- |
| **Core Asset** | **Description** |
| **Configurations** | Configurations are used to capture any network-attached devices/assets (physical or virtual) - in other words, anything with an IP address. Configurations can also be pieces of hardware that need to be controlled and managed but that do not have IP addresses, for example, a display, camera, security panel/alarm, or back up power supply. |
| **Checklists** | Checklists let you document your tasks in order so you can accomplish the most important things first, stay on-track, and work efficiently. Easily delegate tasks to the right person and share your list with them so they can register their task as completed when done. |
| **Locations** | Locations are used to document the physical presence and addresses of sites, offices, or branches. |
| **Contacts** | Contacts are used to document client contacts. |
| **Domain Tracker** | Domain trackers capture any internet-facing domains. When you enter a domain into the domain tracker, the DNS entries and expiration dates will be retrieved automatically. |
| **SSL Tracker** | SSL trackers capture the certificate information of any internet-facing service secured by an SSL. Public details are retrieved automatically; private keys can be added. |
| **Passwords** | Passwords are used to document the credentials used to manage the client's various assets. |
| **\* Network Glue** | Network Glue is an automated network documentation tool that allows you to automatically create a network diagram for your clients. Use this tool to gain complete and comprehensive visibility into your clients’ network through automatic discovery, documentation, and diagramming. |
| **\*\* Tickets** | Take your Kaseya BMS integration even further with BMS Live Ticketing in IT Glue. This feature allows you to open, update, and resolve BMS tickets directly in IT Glue without having to switch between the applications. |
| **\*** For more information on how to purchase the Network Glue solution, please visit our [site.](https://www.itglue.com/networkglue/)  **\*\*** BMS tickets sync requires an active integration set up with BMS that has **Enable Ticket Integration** selected in the sync settings. Refer to [Integrating with BMS](../../1-admin/psa-integrations/integrating-with-kaseya-bms.html). | |

You can populate the configurations, locations, and contacts using your PSA.

If not using a PSA, the configurations, locations and contacts can be manually entered or imported from CSV/spreadsheets or your RMM.

If you need configuration items and other information to appear within distinct sub-organizations, you can easily create this parent/child relationship in IT Glue. Generally, you will want to reflect this structure in your PSA and RMM, if integrated with IT Glue, before making changes to IT Glue.

Note that if you are bringing in information from other systems, make sure you sanitize it as much as possible. Also, whatever you bring in to IT Glue should be information you need to support your current clients.

Core Assets are the building blocks of your account that you document before anything else. Once they are captured in IT Glue, you can make a structured, logical arrangement of this information (plus add more information) using flexible assets.

In other words, you can apply the glue that will stick it all together!

## Part 2: Design the optimal structure for Flexible Assets

The Core Assets can be linked in a way that will create relevant and logical relationships. These relationships keep information retrieval time down to a minimum (to just one or two clicks away), which creates efficiency, increases billable hours, and ultimately drives performance.

The key to building these relationships are the custom fields and forms known as Flexible Assets.

Flexible Assets are used to document information about the applications and services you manage for your clients. Flexible Assets can be completely customized to fit your team's information needs at the current stage of your organizational maturity. They are also the cornerstone to standardizing documentation across every organization you work with.

Things you might capture in a Flexible Asset to support your team:

* **Checklists:** A shortlist of the most important steps in a business-critical process (e.g. resolving a major incident, onboarding a new client).
* **Business rules:** "Prior approval required by person A and B to make changes to the configuration of router X and server Y."
* **Reference documentation:** Licensing agreements.

Several templates are available for download within the app, including:

|  |  |
| --- | --- |
| **Flexible Asset** | **Description** |
| **Site Summary** | Used to give an overview of basic information to help your team get to know the client organization. |
| **Active Directory** | Provides the authentication information for a Windows domain type network. |
| **Email** | Details the email infrastructure with links to the component parts. |
| **Applications** | Creates a full listing of any cloud based, on-premise, client-server, and client only applications. |
| **File Sharing** | Details the standard file shares on the network and how each mapped drive is added (manually, GPO, etc.). |
| **Printing** | Captures the printing infrastructure with links to the component parts. |
| **Backup** | Details information for a specific backup solution with links to the component parts. |
| **LAN** | Details specific LAN and VLAN configurations, including the various physical and logical components. |
| **Internet/WAN** | Captures any ISP/WAN/VPN information that is useful for resolving internet/WAN issues. |
| **Wireless** | Documents the wireless solution at a specific site. |
| **Security** | Provides your team with security related information, including firewalls, anti-virus, anti-spam, and password standards. |
| **Remote Access** | Captures all methods of remote access in one place (VPN, Webmail). |
| **Virtualization** | Details the virtualization/VMware/Hyper-V infrastructure with links to all the component parts. |
| **Voice/PBX** | Gives an overall picture of a specific voice solution with links to the component parts. |
| **Sales/Finance** | Stores any sales or finance preferences for that client. |
| **Licensing** | Captures software licensing information from individual software instances to volume site licenses. |
| **Vendors** | Creates a full listing of vendors with each vendor contact kept updated from one central place (e.g. through your PSA). |

Remember these templates were designed with input from MSPs. However, you're very welcome to design your own Flexible Assets. A best practice is to always ask yourself "how will my information be best presented to my team" instead of asking "how does IT Glue need me to document information."

Once you have your Flexible Asset forms and fields designed the way you want, Flexible Asset data will need to be manually added. If you have a lot of previously created data that you want to add as Flexible Assets, you can also import information from CSV/spreadsheets.

## Part 3: Documents

Take a look back through what you've done with your Flexible Assets and admire what you've accomplished so far. Make sure you have checked off all your structured documentation needs and wants. Your Core and Flexible Assets make up about 70% of what is needed to make your tech team efficient. The remaining approximately 30% will be in the Documents area of IT Glue.

After you have your Flexible Assets fully designed, you can focus on how to design a Knowledge Base structure for your documents. The [Developing your internal knowledge base](../documents/develop-your-internal-knowledge-base.html) topic is useful reading to you at this stage.

Documents are where your team will access your processes and procedures and any other long form documentation that needs to be created. This can be internal documentation that probably only your team will look at, or external documents that can be shared with non-authenticated users. Once these documents are created in IT Glue, they are fully indexed for search and can be linked to any asset where there is relevant context.

## Part 4: Organizing the sidebar

The sidebar on the left-hand side of the screen when you're viewing an organization is displayed consistently for every organization. If well designed, this will increase standardization and save in search time. Consider how to arrange the assets in the sidebar to support your team's efficiency. We generally suggest that core assets are grouped under a Core Assets heading and the Flexible Assets under an Apps & Services heading. For more information, see [Organizations sidebar](../organizations/organizations-sidebar.html).

### Part 5: Related Items

You have one other navigational aid you can use. On the right-hand side of the screen when you're viewing an asset is the Related Items section. This feature can be used to help your team navigate between closely related components. Our [Relationship mapping (related items/tagging)](relationship-mapping-related-items-tagging.html) article has a good explanation of how to use this section.

## Part 6: Putting it all together

As an example of how to document one of your services, here is a bare bones overview of the steps to take to document an email service from start to finish:

**Core Assets**

* Server
* Domain
* SSL certificate
* Password (for management console)

**Flexible Assets**

* Email
* Vendors
* Licensing

**Documents**

* Creating a user mailbox
* Decommissioning an email account
* Configuring an email client
* Troubleshooting connectivity issues for email

## What's next?

Now that you know how to use the key components of IT Glue, you’re on your way to documentation nirvana. Creating an easily navigated structure is not only helpful to your team on a day-to-day basis, but it also helps you become a more efficiently run MSP.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
