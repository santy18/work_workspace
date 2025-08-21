---
title: "Search Best Practices"
source: "https://help.itglue.kaseya.com/help/Content/2-using/get-to-know-it-glue/search-best-practices.html"
crawled_at: "2025-08-18T21:14:07.718847Z"
---

v1.118.88

# Search Best Practices

Use IT Glue's Search feature to quickly find information in your account from wherever you are in the platform. Here are some best practices when using Search in IT Glue.

## Choosing the right search scope

From any screen in IT Glue, you can begin your search by:

* Clicking the **Search bar** at the top of the screen
* Pressing "**Q**" on your keyboard
* Pressing "**/**" on your keyboard
* **For GlueConnect users only:** Press "**G**" on your keyboard to launch the search bar automatically toggled to GlueConnect parameters.

If you are searching outside of an organization, all three methods above will allow you to search on a global level only. If you are searching within an organization, you can toggle the parameters of the search to either organizational or global.

* An *organizational search* means searching only within the organization you are currently viewing.
* A *global search* means searching across all organizations you have access to.

To toggle the parameters of the search between an organizational or global levels, simply click the globe/house icon in the search bar.

For GlueConnect users, click the icon until the GlueConnect Search text appears in the search box to have your global search return results from across all your GlueConnected accounts.

## Narrowing your search results

As you start typing search terms into the search bar, results will start to appear. The maximum number of results is 50. Continue to type more keywords to refine your search results.

The top results are associated with the **Name** field of IT Glue items, followed by results for other fields. Search shows results across multiple fields containing any of your keywords.

For example, if you search for the words **Happy Frog**, you will get results for:

* just the word **happy**
* just the word **frog**
* both words

First to display are exact matches for the full term, as if you had put quotations around the words.

Note that the results of your searches will only show results you have access to. Therefore, your colleagues may see different results, even if you’re both searching with the same keywords.

## Document title search vs. document content search

When searching for terms in the search bar, note that the returned results will differ for document titles versus the content of a document, depending on the input you provide.

### Document title search

* Partial matching (fuzzy) search

Document titles support fuzzy or partial matching. This means even if a search term is misspelled or incomplete, the system can still return relevant results based on similarity. The title search uses algorithms that allow for approximate matches, making it more forgiving of typos or variations. We strongly recommend you only search for exact whole words and avoid partial word searches.

EXAMPLE  Searching for "runnning" (with an extra "n") may still return documents with "running" in the title, because fuzzy matching is applied.

### Document content search

* Exact matching with root word analysis

Content search relies on analyzing words and reducing them to their root forms (e.g., "running" becomes "run"). This helps match different grammatical forms of a word.

EXAMPLE  This process does not support fuzzy matching. Therefore, a misspelled word like "runnning" will not match "running" in the body of the document.

* Acronym handling

Acronyms like "MSP" are treated differently. Since they are not natural language words, they are stored as exact terms.

EXAMPLE  "MSP" and "MSPs" are considered distinct terms, so searching for one won't return results containing the other.

### Summary Table

|  |  |  |
| --- | --- | --- |
| Feature | Document Title Search | Document Content Search |
| Fuzzy matching | Yes | No |
| Root word analysis | No | Yes |
| Handles misspellings | Yes (partial match) | No |
| Acronym matching | No (exact match only) | No (exact match only) |

## Partial word (fuzzy) searching

We strongly recommend you only search for exact whole words and avoid partial word searches. For example, searching for **serv** or even **server** will not necessarily return a server named *server4thfloor*.

## Refining searches by short name

Another way to refine your search results is by adding the organization short name as one of your search words. You can find an organization short name by clicking **Edit** on any organization.

## Keyboard Shortcuts

Do you rely on your keyboard to navigate? IT Glue's Search feature is packed full of useful [Keyboard shortcuts](search.html) to make searching even more convenient.

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
