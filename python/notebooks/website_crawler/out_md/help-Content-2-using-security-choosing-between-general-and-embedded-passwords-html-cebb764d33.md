---
title: "Choosing between general and embedded passwords"
source: "https://help.itglue.kaseya.com/help/Content/2-using/security/choosing-between-general-and-embedded-passwords.html"
crawled_at: "2025-08-18T21:14:46.371296Z"
---

v1.118.88

# Choosing between general and embedded passwords

You have two kinds of passwords you can create: General and Embedded.

## General passwords

A general password is a password that's created from the main Passwords section, and then usually linked as a related item to the relevant assets.

These passwords have many uses, but should always be used whenever you have a password that can be linked to multiple assets. Think one to many relationships.

For example, you have a password for a domain registrar (such as GoDaddy) that's associated with several domains. You could create embedded passwords in the relevant assets instead, but each time the same data is entered more than once, it causes a drop in productivity levels and also introduces the risk of data entry error.

Key benefits of general passwords:

* Eliminates data duplication.
* Reduces risk of accidental deletion.
* Can set security permissions on just the password itself.

When this kind of password can be particularly useful:

* Active Directory
* Domain registrar
* DNS hosting
* Web hosting

## Embedded passwords

An embedded password is a password that is created from within configuration items and other assets through an Embedded Passwords section on the side panel.

You may want to use an embedded password when you have a password that can only be used in one context, such as one device. Think one-to-one relationships.

When this kind of password may be useful:

* Administrative Web Interface (username, password, and URL) for a firewall or switch
* Local admin account on a Windows server

## Protecting your passwords

We know how important your password security is to you. With general passwords, you will always have fine-grained control over who can access each individual password. But keep in mind that there are no permission settings for individual embedded passwords. To change who can access an embedded password, you will need to apply permissions to the containing item.

For more information about managing network and server credentials in IT Glue, see [Passwords](../documentation-guide/passwords.html).

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
