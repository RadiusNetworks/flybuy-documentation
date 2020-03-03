# Customer Partner Integrations

For custom partner integrations, FlyBuy can consume either webhooks (preferred) or APIs. The purpose of a custom integration is to import orders from the partner's backend system into FlyBuy's and to update orders in FlyBuy if any changes have occurred.

If the partner opts for webhooks, FlyBuy will subscribe appropriately and listen for push events. If the partner opts for APIs, FlyBuy will ping the endpoint every X number of minutes with an interval agreed upon between FlyBuy and the partner.

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