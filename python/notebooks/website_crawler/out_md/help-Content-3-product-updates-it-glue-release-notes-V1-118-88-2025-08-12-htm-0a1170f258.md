---
title: "IT Glue V1.118.88: August 12, 2025"
source: "https://help.itglue.kaseya.com/help/Content/3-product-updates/it-glue-release-notes/V1.118.88-2025-08-12.htm"
crawled_at: "2025-08-18T21:14:13.342959Z"
---

v1.118.88

# IT Glue V1.118.88: August 12, 2025

## New feature

IT Glue administrators and managers can now customize passphrase complexity for improved security and usability. New options allow you to configure six randomly generated words separated by spaces, with additional requirements for uppercase letters, special symbols, and numbers. This helps you strengthen security while keeping passphrases easy to read and remember.

## Enhancement

The groups documentation in the IT Glue API is now publicly available, enabling easier integration and development.

## Fixes

* Fixed an issue where the Network Show Page UI displayed the manual sync job status as “Completed” after a page refresh, even if the job was still processing in the background.
* Resolved an issue where downloaded attachments from Configurations or Documents saved with an incorrect file extension (e.g., “.conf” files saving as “.txt”).
* Corrected an error where creating a new configuration from RMM with only one IP and one MAC address incorrectly created two interfaces. The logic now creates a single configuration interface when an RMM record has only one IP and one MAC address. For multiple IPs, the existing behavior remains.
* Fixed a delay of up to two minutes when loading the user Edit page in the IT Glue Admin portal.
* Fixed an issue where new devices from the Datto RMM integration were not syncing into IT Glue. New devices are now properly pulled and reflected in IT Glue.
* Resolved an issue where global user statistics and filter functions were not displaying or calculating correctly in the Account-Wide Statistics section across NA, EU, and AU regions.
* Corrected an issue where the IT Glue Domain Tracker did not update for some domains. It now displays complete and accurate domain information.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
