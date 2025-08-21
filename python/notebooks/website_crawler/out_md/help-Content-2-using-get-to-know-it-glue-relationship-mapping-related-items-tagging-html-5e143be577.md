---
title: "Relationship mapping (related items/tagging)"
source: "https://help.itglue.kaseya.com/help/Content/2-using/get-to-know-it-glue/relationship-mapping-related-items-tagging.html"
crawled_at: "2025-08-18T21:14:38.950373Z"
---

v1.118.88

# Relationship mapping (related items/tagging)

IT Glue lets you map relationships between assets to give you a full picture of your client's IT environment.

Relationship mapping involves entering all assets and then creating logical, two-way relationships between them. After that's done, you can see the dependencies and relationships for a single IT component, which makes it easy to know what's at stake any time a problem is reported within the network. The logical structure allows for better information management, which in turn drives performance.

For example, let's say one of your client's servers crashes. You immediately check IT Glue to see what's hosted on that server. IT Glue lists two applications. You open the applications in IT Glue to see what they're used for and whether there are any failover systems in place. You now know what steps to take immediately before looking for a more permanent solution for the failed server, such as ordering new hardware.

## Related items

This process will allow you to relate anything to anything, including configurations, passwords, folders, documents, etc.

1. Open an item, for example, a server.
2. Under **Related Items** (right side), click **Add Related Item**.
3. **Search** for and select an item to relate to the server, such as a firewall or a switch. A blank text field will display below it.
4. (Optional) Enter notes about the relationship in the text field.
5. Click **Save**. When you hover your mouse over the item, you can see the notes.

After that's done, any assets that you've related to the item you're viewing are listed in the Related Items section. Clicking on an item takes you to that item, where there will be a link back to the source in the Related Items section.

## Tagging

For clarification, the Related Items field is not the same as the Tag field in flexible assets. Tags are used to tag items and create relations to other assets. They can also create relations to organizations or users.

With tags, you specify what you want tagged, which means you have greater control over what is entered. The Tag field can also be made a required field. For more information, see [Using Tag fields](../flexible-assets/create-tag-fields.html).

Using the server example again:

1. Search for and open an application that was created with the Application flexible asset.
2. Click **Edit** to enable edit mode and then scroll down.
3. Under **Application Servers**, search for and select the server the application runs on.
4. Click **Save** at the bottom of the screen.

After that's done, a link to the server will display under Application Servers. Clicking on this link takes you to that item, where there will be a link back to the application in the Related Items section.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
