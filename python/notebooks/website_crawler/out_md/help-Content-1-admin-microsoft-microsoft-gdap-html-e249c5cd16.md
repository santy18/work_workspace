---
title: "Microsoft Integration: GDAP"
source: "https://help.itglue.kaseya.com/help/Content/1-admin/microsoft/microsoft-gdap.html"
crawled_at: "2025-08-18T21:14:32.487943Z"
---

v1.118.88

# Microsoft Integration: GDAP

BEFORE YOU BEGIN  To review prerequisites and learn how to fully set up an integration with Microsoft in IT Glue, refer to [Microsoft Integration](microsoft-integration.html).

Microsoft’s GDAP follows the principle of least privilege for access control. As follows are the three important steps to perform in Microsoft Azure to set up granular delegated admin permissions (GDAP):

1. [Creating a service account user for GDAP](#Creating-a-service-account-user-for-GDAP).
2. [Creating a new security group](#Creating-a-new-security-group) and assigning the service account user to the group.

   NOTE  It is required to assign this security group to each GDAP relationship for all the tenants.
3. [Configuring the IT Glue application with proper permissions](#Configuring-the-IT-Glue-application-with-proper-permissions).

   NOTE  Both **Delegated** and **Application** permissions are required to be added.

## Creating a service account user for GDAP

IMPORTANT  The procedure in this section is required for only granular delegated admin permissions (GDAP) tenants and not relevant for delegated admin permissions (DAP).

1. Log in to your Microsoft Azure portal.
2. From the left navigation menu, navigate to **Microsoft Entra ID > Users**.
3. From the **New user** drop-down menu, select **Create new user**.
4. Fill in the required fields.
5. Click the **Assignments** tab.
6. Click **Add group**.
7. Select the **AdminAgents** group check box, and click **Select** at the bottom of the page.
8. Click **Add role**.
9. Select the **Global Administrator** role check box, and click **Select** at the bottom of the page.
10. Create the new service account user.

NOTE  MFA must be enabled for this service account.

## Creating a new security group

Create a new security group in Microsoft Azure and add the service account user to the group as follows:

1. From the left navigate menu, navigate to **Microsoft Entra ID > Groups**.
2. Click **New group**.
3. Fill in the required fields, leaving the **Group type** as the default option, **Security**.
4. In the **Members** section, click **No members selected**.
5. Select the service account user created in [Creating a service account user for GDAP](#Creating-a-service-account-user-for-GDAP), and click **Select** at the bottom of the page to add the user to the group.
6. Click **Create** to create the security group.
7. From Microsoft Partner Center, assign this security group to the GDAP relationship that includes the service account created in the previous section. You must ensure that this security group is assigned to each GDAP relationship and has at least one of the following permissions:
   * Global Administrator
   * Privileged Role Administrator
   * Cloud Application Administrator

If you assign any permission other than Global Administrator (Privileged Role Administrator or Cloud Application Administrator), the following permissions are required to be assigned:

* Global Reader
* Intune Administrator
* Insights Business Leader
* Reports Reader

For more information, refer to [Obtain granular admin permissions to manage a customer's service](https://learn.microsoft.com/partner-center/customers/gdap-obtain-admin-permissions-to-manage-customer) and [Grant granular permissions to security groups](https://learn.microsoft.com/partner-center/customers/gdap-assign-microsoft-entra-roles) in the Microsoft Partner Center documentation.

## Configuring the IT Glue application with proper permissions

For instructions, refer to [Register IT Glue as an application in your Microsoft account](microsoft-integration.html#Register-IT-Glue-as-an-application-in-your-Microsoft-account) in [Microsoft Integration](microsoft-integration.html).

NOTE  The **Redirect URI** field is required for users setting up GDAP.

NA: https://[subdomain].itglue.com/microsofts

EU: https://[subdomain].eu.itglue.com/microsofts

AU: https://[subdomain].au.itglue.com/microsofts

## Retrieving the client ID, tenant ID, and client secret value to activate the integration in IT Glue

For instructions, refer to [Copy your client ID and tenant ID from Microsoft](microsoft-integration.html#Copy-your-client-ID-and-tenant-ID-from-Microsoft) and [Generate and copy your client secret value in Microsoft](microsoft-integration.html#Generate-and-copy-your-client-secret-value-in-Microsoft) in [Microsoft Integration](microsoft-integration.html).

## Configuring API access permissions

For instructions, refer to [Configure API access permissions in Microsoft](microsoft-integration.html#Configure-API-access-permissions-in-Microsoft) in [Microsoft Integration](microsoft-integration.html).

|  |  |
| --- | --- |
|  | [Need troubleshooting help? Open the Kaseya Helpdesk.](https://helpdesk.kaseya.com/) |
|  | [Want to talk about it? Head on over to the Community!](https://community.kaseya.com/it-operations) |
|  | [Have an idea for a new feature? Want to learn about upcoming enhancements? Visit the Ideas forum!](https://community.kaseya.com/ideas/categories/ITGlue-ideas-portal) |
|  | [Provide feedback for the Documentation team.](javascript:(function()%7BSendLinkByMail()%3B%7D)()%3B) |

**How would you rate this KB article?**

[[^](#Top)](#Top)

Copyright © 2025 Kaseya | [Privacy Policy](https://www.kaseya.com/legal/kaseya-privacy-statement/) | [Edit Cookies](#) | [Website Terms of Use](https://www.kaseya.com/legal/website-terms-of-use/)
