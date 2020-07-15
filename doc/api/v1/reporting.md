# Reporting API

- [API Specs](#api-specs)
- [Get A List Of All Archived Orders](#get-a-list-of-all-archived-orders)
- [FAQ](#faq)
- [Key Mapping](#key-mapping)

The FlyBuy Reporting API enables partners to build custom analytics based on archived data.

## <span id="api-specs">API Specs</span>

A sample Postman collection can be found [here](https://www.getpostman.com/collections/3684da81f53275af8c22).
Example curl commands can also be found at the end of each respective section.

### Hostname

Use this hostname with the path specified in each request to get the full API URL.

```http
https://flybuy.radiusnetworks.com
```

### Headers

```http
Accept: application/json
Content-Type: application/json
Authorization: Token token="api-token"
```

The API token is a 48-character key associated with your account that allows access to all resources under that account.
Create and manage API tokens [here](https://account.radiusnetworks.com/personal_tokens).

The API token is different from webhook and SDK tokens. If you require a webhook or SDK token, please reach out to your FlyBuy customer success representative.


## <span id="get-a-list-of-all-archived-orders">Get A List Of All Archived Orders</span>

```http
GET /api/v1/archived_orders?end_time=2020-04-20T23:59:59Z&start_time=2020-04-20T00:00:00Z
```

This returns a paginated response of all archived orders that the owner of the API key has access to.
This can span multiple projects and sites.

Use the `pages.next` URL provided in the response body for the next page of results.

### <span id="get-a-list-of-all-archived-orders-parameters">Parameters</span>

Include any desired query parameters.

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `start_time` | `string` | **Required.** The API returns only archived orders that have an `archived_at` that is later than the provided value. |
| `end_time` | `string` | **Required.** The API returns only archived orders that have an `archived_at` that is earlier than the provided value. |
| `partner_identifier` | `string` | _Optional._ If provided, sites can be fetched with a partner site identifier. In the merchant portal, this is the `Site Number`. |
| `project_id` | `string` | _Optional._ If provided, sites can be fetched with a FlyBuy project identifier. |
| `page` | `integer` | _Optional._ Allows retrieving a specific page of the results. Defaults to 1. |
| `per` | `integer` | _Optional._ Specifies how many archived orders should be included in a page of results. Defaults to 50. Max of 100. |

### <span id="get-a-list-of-all-archived-orders-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "time_range": {
    "start_time": "2020-04-20T00:00:00Z",
    "end_time": "2020-04-20T23:59:59Z"
  },
  "data": [
    {
      "type": "archived_order",
      "id": 1,
      "archived_at": "2020-04-20T18:00:00.000Z",
      "arrived_at": null,
      "completed_at": null,
      "expired_at": null,
      "location_permission": null,
      "location_started_at": null,
      "order_reminder_at": null,
      "partner_identifier": null,
      "payment_method": null,
      "pickup_type": null,
      "pickup_window": null,
      "postarrival_at": null,
      "prearrival_at": null,
      "project_name": null,
      "redeemed_at": null,
      "sdk_platform": null,
      "sdk_version": null,
      "site_name": null,
      "sms_delivered_timestamps": null,
      "sms_failed_timestamps": null,
      "sms_undelivered_timestamps": null,
      "starting_latitude": null,
      "starting_longitude": null,
      "timezone": null,
      "trip_distance_meters": null,
      "viewed_timestamps": null,
      "wait_time_seconds": null,
      "waiting_at": null,
      "app_authorization_id": null,
      "customer_id": null,
      "project_id": null,
      "site_id": 1,
      "created_at": null,
      "updated_at": "2020-04-24T19:19:45.000Z"
    }
  ],
  "pages": {
    "current": 1,
    "count": 1,
    "per": 50
  }
}
```

### <span id="get-a-list-of-all-archived-orders-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/archived_orders?end_time=2020-04-20T23:59:59Z&start_time=2020-04-20T00:00:00Z \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```

## <span id="faq">FAQ</span>

### What is an archived order?

An archived order is a closed order that has been stripped of the customer's personally identifiable information (PII).

### When do orders get archived?

An order gets archived once it is closed.
A closed order is an order that has an `order_state` of `completed` or `cancelled`.
If an order remains open for 60 days, it will automatically get archived regardless of the `order_state`.

### How do I know an order is redeemed?

If `redeemed_at` is not null, the order is redeemed.

### How do I know an order received location updates?

If `location_started_at` is not null, the order received location updates.

### Is there a script I can run that will generate an export?

Use [this](https://github.com/RadiusNetworks/flybuy-documentation/blob/master/doc/api/v1/examples/reporting-orders.py) sample Python script to generate a CSV file.


## <span id="key-mapping">Key Mapping</span>

This is a list of all keys returned in the response.

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
|  `type` | `string` | Always `"archived_order"` |
|  `id` | `integer` | FlyBuy order identifier |
|  `archived_at` | `timestamp` | Time order was archived |
|  `arrived_at` | `timestamp` | Time user reached the `arrived` state |
|  `completed_at` | `timestamp` | Time order was completed by staff or customer |
|  `location_permission` | `string` | Possible values [`not_determined`, `restricted`, `denied`, `authorized`, `authorized_always`, `authorized_when_in_use`] |
|  `location_started_at` | `timestamp` | Time user began sharing location |
|  `order_reminder_at` | `timestamp` | Time order reminder message sent |
|  `partner_identifier` | `string` | Partner-provided order identifier |
|  `payment_method` | `string` | Method of payment used |
|  `pickup_type` | `string` | Possible values [`null`, `curbside`, `pickup`, `delivery`, `dispatch`] |
|  `pickup_window` | `range of timestamp` | Can be a pickup time or a pickup window with start and stop times |
|  `postarrival_at` | `timestamp` | Time postarrival event occurred |
|  `prearrival_at` | `timestamp` | Time prearrival event occurred |
|  `project_name` | `string` | Brand name in FlyBuy |
|  `redeemed_at` | `timestamp` | Time user redeemed the order (e.g., Tapped "I'm on my way" in the FlyBuy mobile app or web flow) |
|  `sdk_platform` | `string` | Possible values [`android`, `ios`, `web`, `sms`] |
|  `sdk_version` | `string` | iOS or Android SDK version |
|  `site_name` | `string` | Site name in the FlyBuy merchant portal |
|  `sms_delivered_timestamps` | `array of timestamps` | Time each SMS message was delivered |
|  `sms_failed_timestamps` | `array of timestamps` | Time of each failed SMS message |
|  `sms_undelivered_timestamps` | `array of timestamps` | Time of each undelivered SMS message |
|  `starting_latitude` | `decimal` | Latitude of first location update |
|  `starting_longitude` | `decimal` | Longitude of first location update |
|  `timezone` | `string` | Time zone for site |
|  `trip_distance_meters` | `integer` | Straight-line distance from first location update to site location |
|  `viewed_timestamps` | `array of timestamps` | Times the order was viewed by clicking on the redemption URL |
|  `wait_time_seconds` | `integer` | `completed_at` - `waiting_at` converted to seconds |
|  `waiting_at` | `timestamp` | Time user entered a pickup area (or pressed "I'm Here") |
|  `app_authorization_id` | `integer` | `1` = FlyBuy iOS app, `2` = FlyBuy Android app, other values for 3rd party apps |
|  `customer_id` | `integer` | FlyBuy customer identifier |
|  `project_id` | `integer` | FlyBuy project identifier |
|  `site_id` | `integer` | FlyBuy site identifier |
|  `created_at` | `timestamp` | Time order record was created |
|  `updated_at` | `timestamp` | Time order record was last updated |
