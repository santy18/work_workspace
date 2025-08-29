---
title: "Search"
source: "https://help.itglue.kaseya.com/help/Content/2-using/get-to-know-it-glue/search.html"
crawled_at: "2025-08-18T21:14:50.174004Z"
---

v1.118.88

# Search

IT Glue's powerful search feature allows you to quickly find information without you having to exit the screen you're working in. This article provides an overview on how to make the most of your search capability in IT Glue. For general best practices on this topic, please read our [Search best practices](search-best-practices.html) KB article.

## Search scopes in IT Glue

All search engines should be simple, efficient, and accurate. To achieve this, the IT Glue search feature intuitively selects the right search scope for you based on three scenarios:

* If you begin your search *outside* of an organization, IT Glue Search defaults the search to a global level only. This means you are searching information from across all organizations you have access to.
  + **For GlueConnect users only:** You would like your global search to return results from across all your GlueConnected accounts. Refer to the next section in this KB for more details.
* If you begin your search *within* an organization, IT Glue Search will search within the organization you are currently viewing. However, you'll also have the option of quickly toggling the search parameters between organizational *and* global. To do so, simply click the globe/house icon in the search bar.

## GlueConnect Universal Search

For IT Glue users that are connected to more than one IT Glue account via GlueConnect, you can change the parameters of your global search to search all information across all GlueConnected accounts. This way, you can find information regardless of what organization or connect account you begin your search in. To access this feature, you require Read-only level and above access within IT Glue.

Toggle the search parameters to search across all GlueConnect accounts by clicking the icon in the search bar. It will shuffle between Global, Organizational, and GlueConnect. When searches are set to GlueConnect, your search will return all global results AND GlueConnect results. In the list of search results, you will see the GlueConnect account names under results that reside in connected accounts.

## Document title and document content search

When searching for terms in the search bar, note that the returned results will differ for document titles versus the content of a document, depending on the input you provide.

EXAMPLE  If you search using a misspelled word (runnning with an extra "n"), seach results with return the document with "running" in the title but not a document with "running" in the body.

The partial search works for document titles but not for the content of a document. This is because the document title or name uses partial (fuzzy) matching.

EXAMPLE  Searching for **serv** or even **server** will not necessarily return a server named *server4thfloor*.

We strongly recommend you only search for exact whole words and avoid partial word searches in order to return the most relevant search results.

## Keyboard shortcuts

Using keyboard shortcuts can make your search experience more convenient. From any screen in IT Glue, you can begin your search in three ways:

* Clicking the **Search bar**at the top of the screen
* Pressing "**Q**" on your keyboard
* Pressing "**/**" on your keyboard

NOTE  All three methods above will only launch a global search if you begin your search *outside* of an organization. If you begin your search *within* an organization, press "**Q**" to launch an organizational search. Clicking the search bar or pressing "**/**" within an organization will launch a global search with the option of toggling to organizational search.

You can also search for a specific asset type by pressing one of the keys below:

| To search for... | Use shortcut... |
| --- | --- |
| Configurations | C |
| Contacts | E |
| Documents | D |
| Domains | W |
| Flexible Assets | F |
| Locations | L |
| Organizations | O |
| Passwords | P |
| SSL Certificates | S |
| Tickets | T |

**For GlueConnect users only:** Press "**G**" on your keyboard to launch the search bar automatically toggled to GlueConnect parameters.

***A note on searching for passwords***

If your IT Glue administrator has set up a [Password Access Workflow](../security/password-access-workflow-in-it-glue.html), please note that clicking the **Show password** button or the **Copy to clipboard** icon on a password’s search result will trigger a notification indicating that you have viewed or copied the password in question. Also, depending on the filters set by your Administrator, clicking **Show Password** or the **Copy to clipboard** icon will also trigger a notification.

**A note on searching for IP addresses**

If the IP of a configuration is associated with the IP address IT Glue field, it is searchable. However, if the IP is associated to the configuration in the PSA or RMM in a ‘Custom Question & Answer Field’ or a ‘User Defined Field (UDF)’ which are not mapped to any fields in IT Glue, the data becomes read-only. As this data does not reside in an IT Glue field in the configuration record, it will not be searchable.

### Start searching in IT Glue

As you start typing in the Search bar, results will be listed in order of relevance. The top results are associated with the **Name**field in IT Glue, followed by results for other fields. All the **Types** will also be displayed.

Check the preview pane to the right of the results list to confirm you've found the right item. You can use the up and down arrow keys on your keyboard to navigate through more previews.

Clicking any of the items in the list will take you directly to its location in the platform.

### Search from any webpage

The IT Glue Chrome Extension enables searching IT Glue from any open webpage using the "**Q**" shortcut. For more information on how to set up the Chrome Extension, refer to our [Quick guide for the IT Glue Chrome Extension](quick-guide-for-the-it-glue-browser-extension.html) and [Using IT Glue Search](using-it-glue-search.html) topics.

## Show recently viewed items

Use the '**.**'(period) shortcut to quickly open and close the recently viewed items menu. The shortcut opens a drop-down menu that shows you the last nine items you viewed. Click on an item to be taken to one of the pages you want to revisit. You can also press the corresponding item number on your keyboard to visit the page.

## Additional Quick Search shortcuts

Check out these additional keyboard shortcuts to further enhance how you use Search in IT Glue:

| **Action** | **Shortcut** |
| --- | --- |
| Open the highlighted result in the current tab | Enter |
| Open the highlighted result in a new tab in the background (leave search open in the current tab) | Ctrl + Enter (Windows)  Cmd + Enter (Mac) |
| Open one result at a time in a new tab in the background (leave search open in the current tab) | Ctrl + Click (Windows)  Cmd + Click (Mac) |
| Cycle the search scope forward through the different asset types | Tab (Shift + Tab reverses direction) |
| Toggle the search scope between the current organization and all organizations | Alt + G (Windows)  Option+ G (Mac) |
| Display keyboard shortcuts | Alt + / (Windows)  Option + / (Mac) |
| Clear text in the search input/Exit current context | Escape |

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
