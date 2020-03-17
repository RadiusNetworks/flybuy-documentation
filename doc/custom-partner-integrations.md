# Customer Partner Integrations

FlyBuy is already integrated with many popular e-commerce and fulfillment platforms (e.g., Olo, Toast, ShopperKit) to seamlessly import orders after they are placed and to handle any updates should those orders change. If your platform of choice isn't included in our list of existing integrations or you have your own system for tracking orders, we are happy to work with you build a custom partner integration to fit your needs. Read below for more information, and contact your Account Executive or drop an email to support@radiusnetworks.com when you're ready to get started.

For a new custom partner integration, FlyBuy can consume webhooks (preferred) or utilize APIs to receive new orders or updates to existing orders. With a webhook integration, FlyBuy will subscribe appropriately and listen for any events that are important for your pickup solution (e.g., order placed, order ready for pickup, order completed). In the absence of webhooks, FlyBuy can instead use your API to receive all this information by querying it on a regular interval to ensure things are up-to-date.

Below is a list of order and customer parameters (some required) that we typically look for from a webhook or API response when building a custom integration.

## Required Parameters

| **Attribute** | **Description** |
| --- | --- |
| Customer Phone Number | Having the customer's mobile phone number enables us to send an SMS to kick off the FlyBuy experience |
| Site Identifier | Your internal store reference number is used to associate an order with a site |
| Order Identifier | Your internal order reference number is used so you can identify an order in the FlyBuy system |

## Recommended Parameters

| **Attribute** | **Description** |
| --- | --- |
| Customer Name | Information displayed on the FlyBuy dashboard |
| Vehicle Information | Information displayed on the FlyBuy dashboard |
| Pickup Time/Window | Information displayed on the FlyBuy dashboard |
| Order Contents | Orders that contain specific items can be tagged with custom icons displayed on the dashboard (e.g. fries, frozen items) |
| Order Status | Allows you to update FlyBuy to reflect any order status changes on your end (e.g. created, ready, delayed, cancelled, completed) |

## Recommended Parameters
| **Attribute** | **Description** |
| --- | --- |
| Pickup Type | How the customer will be receiving their order (e.g. pickup, curbside, delivery) |
| Order Origin | How was this order created (e.g. e-commerce website, mobile app) |