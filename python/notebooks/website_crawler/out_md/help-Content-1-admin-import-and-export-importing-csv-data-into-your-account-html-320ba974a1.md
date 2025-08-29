---
title: "Importing CSV data into your account"
source: "https://help.itglue.kaseya.com/help/Content/1-admin/import-and-export/importing-csv-data-into-your-account.html"
crawled_at: "2025-08-18T21:14:48.525155Z"
---

v1.118.88

# Importing CSV data into your account

IT Glue's CSV import feature was designed to help you import large amounts of data to populate flexible assets or deploy IT Glue without syncing in data from a PSA integration.

## Prerequisites

* You must be an Administrator or a Manager who has access to all organizations. For any large or complex imports, you should be an Administrator to have full visibility to all data.
* We strongly recommend that you review our [File Import and Matching Guide](file-import-and-matching-guide.html)  before starting your import. This article contains full instructions on how the matching data works.
* The import file must be encoded in UTF-8 and be no greater than 300 MB. For best results, save the CSV file exactly as described below.
* Organization names and manufacturers/models must be written exactly as they appear in IT Glue. The importer won't do any fuzzy matching tests. It doesn't know, for example, that **Happy Frog** is the same organization as **Happy Frog Inc.**, or that **Dell Inspiron** is the same model as **Dell Insprion**. It will create new organizations or manufacturers/models when no match exists.

## Instructions

The instructions for importing are broken down into the following sections:

[Creating a test environment](#)

BEFORE YOU BEGIN  Before continuing with the following steps, review [File Import and Matching Guide](file-import-and-matching-guide.html). If you have any questions, feel free to [submit a Kaseya Helpdesk request](https://helpdesk.kaseya.com/hc/en-gb/requests/new) before you start your import.

If you make a mistake with your list import, you *cannot* undo it, and there is currently no bulk edit functionality. You would need to work through changes one at a time. Therefore, we suggest you set up a test organization in your account and make a few tests before you import large amounts of data into a production organization. It's easy to delete the test organization afterward.

While you're testing, make sure your data is formatted for our field types. When the test import finishes, open the [Global > Assets](../../2-using/get-to-know-it-glue/view-global-lists.html) list view and compare it against your spreadsheet.

IMPORTANT  We don't recommend that you create data from an import if you'd like to then have it populate from IT Glue to your PSA. Any items created or updated by this process will not be pushed to your PSA unless you go through and edit and save each and every item. This step is absolutely manual and is not recommended.

[Creating your CSV file](#)

When setting up a new IT Glue account, your existing data can be imported as a CSV file. These steps will help you create your CSV file so that it will import successfully.

### Importing the data

Two ZIP files are provided at the bottom of this article. Refer to [Sample downloadable files](#Sample-downloadable-files).

Download one of these ZIP files to start importing data into the following areas of IT Glue:

* **Sample Excel import files with required fields highlighted** (Save as CSV when you're ready to import.)
* **Sample CSV import files**
  + Organizations
  + Locations
  + Contacts
  + Configurations
  + Passwords
  + Domains
  + SSL certificates

1. Open the file you want to use and delete the sample data, but not the header row.
2. Copy data from the matching columns in your existing spreadsheets into the IT Glue sample file. Note that you can change the order of the columns if needed, but make sure you leave the values of the header cells intact.

NOTE  When you add a domain that has an SSL certificate installed, the public aspects of the certificate are automatically added to the SSL tracker, but you will have to add any missing details, such as private SSL certificates, via an import or manually.

### Flexible asset imports

For flexible asset imports, we recommend adding one or two test flexible assets to IT Glue manually, which you can then export and populate with your real data:

1. [Create your flexible asset type](../../2-using/flexible-assets/quick-guide-for-flexible-assets.html) from template or from scratch.
2. Open your test organization and click the name of the flexible asset from the left sidebar.
3. Create one or more test flexible assets using placeholder data, completing all the fields.
4. [[Export your data](exporting-and-backing-up-account-data.html)](exporting-and-backing-up-account-data.html). This requires an Administrator role.
5. Open the exported CSV file and delete the placeholder data.
6. You're now ready to populate this CSV file with real data and then import it into IT Glue.

[Saving your CSV file](#)

When you save the file, make sure you save it as a CSV file.

* If on a PC, save as **CSV (Comma delimited) (\*.csv)**.
* If on a Mac, save as **Windows Comma Separated (.csv)**.

If there are any problems importing your CSV on a PC:

1. Open the CSV file in Notepad.
2. Click **Save As...** and then select UTF-8 under **Encoding**.
3. After selecting UTF-8, save the file in a slightly different file name from the original.
4. Do not reopen the file, which will cause it to be re-encoded by Windows.
5. Import this new file into IT Glue.

[Importing into a single organization](#)

1. Navigate to **Account > Import Data** and click the **+ New** button. Then, choose the type of import you want to create in the drop-down menu. In this example, we will be importing Configurations.
2. Select **Single Organization** and then select the organization you'd like to import data into.
3. Click **Choose File** to select the saved CSV file.
4. Set **Allow partial imports** to "No," which means the whole import will fail if there are any non-UTF-8 characters or missing required fields in the CSV. If that happens, you can rerun the import and allow partial imports to find out which rows have errors.
5. Click **Continue**.
6. On the following **Import** page, review the information carefully to ensure your CSV columns match up with IT Glue fields.
   1. Click each of the drop-down menus under the right-hand **[Configuration] Field** column to select the matching field.
   2. Choose to ignore a match, or match to either a required or optional field. Each import type will have required fields that must be matched to your columns at minimum. Other fields are optional.
7. Click **Run Import**.
8. Wait a few minutes for the import to complete. Once the import is done, you'll get an email from support@itglue.com that includes a link to view imported rows or details regarding errors in your import.

You can verify your import was successful by waiting for the email confirmation or by navigating to **Account > Import Data** and then clicking on the link for your import. Alternatively, you can also navigate to the [Global > Assets](../../2-using/get-to-know-it-glue/view-global-lists.html) area to view the information that you imported.

[Importing into multiple organizations](#)

IMPORTANT  Make sure each organization name in the CSV data is spelled exactly the same as it appears in your IT Glue account. If the names are different, new organizations will be created.

1. Navigate to **Account > Import Data** and click the **+ New** button. Then, choose the type of import you want to create in the drop-down menu. In this example, we will be importing Contacts.
2. Select **Multiple Organizations**.
3. Click **Choose File** to select the saved CSV file.
4. Set **Allow partial imports** to "No," which means the whole import will fail if there are any non-UTF-8 characters or missing required fields in the CSV. If that happens, you can rerun the import and allow partial imports to find out which rows have errors.
5. Click **Continue**.
6. On the following **Import** page, review the information carefully to ensure your CSV columns match up with IT Glue fields.
   1. Click each of the drop-down menus under the right-hand **[Contact] Field** column to select the matching field.
   2. Choose to ignore a match, or match to either a required or optional field. Each import type will have required fields that must be matched to your columns at minimum. Other fields are optional.
7. Click **Run Import**.
8. Wait a few minutes for the import to complete. Once the import is done, you'll receive an email from support@itglue.com that includes a link to view imported rows or details regarding errors in your import.

### Example of imported contacts

### Sample downloadable files

Sample import files are provided below. The XLS files highlight the fields required by each asset for the import to work. The CSV files are the correct file format for importing. Both sets of samples include a line of sample data, which should be removed prior to executing the import.

* [Sample-XLS-import-files](../../Resources/Images/ITGlue/Sample-XLS-import-files.zip)
* [Sample CSV import files](../../Resources/Images/ITGlue/Sample-CSV-import-files.zip)

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
