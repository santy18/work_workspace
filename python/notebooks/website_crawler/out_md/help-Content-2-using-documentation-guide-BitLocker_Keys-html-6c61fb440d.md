---
title: "Microsoft Integration: BitLocker recovery keys"
source: "https://help.itglue.kaseya.com/help/Content/2-using/documentation-guide/BitLocker_Keys.html"
crawled_at: "2025-08-18T21:14:26.753626Z"
---

v1.118.88

# Microsoft Integration: BitLocker recovery keys

BitLocker recovery keys from Intune devices stored in the Microsoft Intune admin center ([intune.microsoft.com](https://intune.microsoft.com/)) can be automatically documented and kept up to date in IT Glue. This feature is only available if you have purchased Network Glue.

You can access your BitLocker recovery keys from Intune devices associated with IT Glue configurations in organizations. You can view each BitLocker recovery key as a general password.

NOTE  All Network Glue users with access to the organization can access BitLocker recovery keys as passwords but only Network Glue administrators or managers can access the BitLocker Sync settings.

## Prerequisites

* An active Microsoft Integration setup.
* The **BitLockerKey.Read.ALL** API permission must be added on the Microsoft side when configuring a Microsoft integration. The Type should be **Delegated**.

## Gaining access to BitLocker recovery keys

1. To gain access to BitLocker recovery keys in IT Glue, you need to do the following:

   * Select at least one type of license.
   * Select contacts with which you would like to sync.
   * Enable the option **Sync BitLocker Keys** under **Microsoft Entra ID Sync** on the Microsoft Integration sync settings page.

   NOTE  This option is visible to all users, whether or not they have purchased Network Glue.

   IMPORTANT  If you already have an existing Microsoft Integration, the sync setting for BitLocker will be disabled by default and you will first need to add the BitLockerKey.Read.ALL API permission in [Microsoft integration](https://help.itglue.kaseya.com/help/Content/1-admin/microsoft/microsoft-integration.html) from the Microsoft’s website.   
     
   If you do not have a Microsoft integration, the sync setting for BitLocker will be enabled by default. You'll need to go to Microsoft’s website and configure the Microsoft integration from scratch. Ensure that you have added BitLockerKey.Read.ALL API permission. Then create a Microsoft Integration in IT Glue.
2. Ensure that the check box for Sync Intune Devices is selected under **IT Glue > Integrations > Microsoft > Intune tab**.
3. Match devices stored in Microsoft Intune with IT Glue configurations under **IT Glue > Integration > Microsoft Machine Matching:**

After a successful sync with Microsoft, users who have purchased Network Glue will be able to see the **BitLocker Keys (via Network Glue)** folder and the Bitlocker keys as passwords on the Passwords page.

## Viewing passwords created in BitLocker keys

1. Navigate to the organization to which the password belongs.
2. Click  **Passwords** in the left sidebar.
3. Click the **BitLocker Keys (via Network Glue)** folder.
4. View the list of BitLocker Keys and click the one for which you wish to view the password record. Filter BitLocker keys by the **BitLocker Keys (via Network Glue)** category.

   NOTE  You will not be allowed to create a category or folder with the name BitLocker Keys (via Network Glue). Also, this folder can be moved if within the same organization but cannot be moved to other organizations.
5. View the BitLocker key as a password record.

   * The name of the password displayed corresponds to the device name stored in Microsoft Intune.
   * **Username** is the BitLocker recovery key ID.
   * The **Password** value is the BitLocker recovery key collected from Microsoft Intune.

   NOTE  If you do not see the BitLocker keys for the subtenants in Microsoft, you will need to perform the following additional steps to grant consent to fetch BitLocker information for each tenant. Go to: https://login.microsoftonline.com/<tenant id - replace this with your client's tenant>/v2.0/adminconsent?client\_id=<app\_id - replace this with the App regiration ID created in your tenant>&scope=https://graph.microsoft.com/  
   Bitlockerkey.Read.All

### Deleting BitLocker keys

You are only able to delete BitLocker keys or the **BitLocker Keys (via Network Glue)** folder when the **Sync BitLocker Keys** setting under a Microsoft integration is disabled.

In addition, to delete the folder, all BitLocker keys stored as general passwords must be deleted first.

IMPORTANT  When the BitLocker key sync is disabled after being turned on, there are 10 minutes during which you cannot delete keys and the BitLocker Keys (via Network Glue) folder. When the recovery key sync is enabled after being turned off, there is a 10-minute window within which you can still delete keys and the BitLocker Keys (via Network Glue) folder.

### Viewing previous keys

The latest BitLocker key is visible in the **BitLocker keys (via Network Glue)** folder. To view previous keys, select the **Include archived** check box:

### General Notes

* When an IT Glue administrator has not created a configuration in IT Glue, the BitLocker Keys will not be created as general passwords as there will be nothing to match using Intune devices. An administrator needs to create a configuration in IT Glue first. Once it is created, devices can be matched from Intune to the configurations in IT Glue and BitLocker Keys can be created as general passwords.

  NOTE  BitLocker keys saved as general passwords are not allowed for password rotation.
* BitLocker Keys (via Network Glue) will be hidden if an IT Glue admin loses Network Glue subscription or has not purchased it.
* An IT Glue administrator cannot add their own items in the BitLocker Keys (via Network Glue) to prevent loss of personal information if they do not update the Network Glue subscription.
* You are not allowed to move BitLocker keys stored as general passwords outside of the folder.
* Only up-to-date keys are visible. All outdated BitLocker keys will be automatically archived. However, you can unarchive archived BitLocker keys, if needed.
* You can store BitLocker keys in Vault.

## Updating the Edit Password page

You cannot edit the **Name, Category, Username, Password** and **Notes**on the Edit Password page. This information is automatically pulled from Microsoft and cannot be changed in IT Glue. If changes are required, you need to make necessary changes in Microsoft. After a successful sync, all changes performed in Microsoft will be visible in IT Glue.

## Understanding BitLocker key as a password

BitLocker recovery key as a password is related to the IT Glue configuration to which it is associated.

When BitLocker key as a password is created, archived, accessed, and viewed, it will be recorded as an action in activity logs.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
