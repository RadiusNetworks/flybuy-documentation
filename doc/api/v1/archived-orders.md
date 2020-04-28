# ArchivedOrders API

- [API Specs](#api-specs)
- [Getting A List Of All Archived Orders](#getting-a-list-of-all-archived-orders)
- [Getting Archived Orders With A Given Partner Identifier](#getting-archived-orders-with-a-given-partner-identifier)
- [Getting Archived Orders With A Given Project ID](#getting-archived-orders-with-a-given-project-id)

This describes the FlyBuy Archived Orders API v1. If you have any problems or
requests please contact [support](https://support.radiusnetworks.com).

## What are Archived Orders?

An `Archived Order` is an `Order` that has been stripped of the customer's personal
identifiable information.  Orders are archived as soon as the Order `state` is changed
to `completed` or `cancelled`.  For all other orders with states of `created`, `ready`,
or `delayed`, we consider those to be incomplete.  Incomplete orders are archived
after 60 days.  All those Archived Orders are available in this API.  If you have more
questions or need help, please contact [support](https://support.radiusnetworks.com).

## <span id="api-specs">API Specs</span>

Example curl commands can also be found at the end of each respective section.

### Hostname

Use this hostname with the HTTP protocol specified in each section to get the full API URL.

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


## <span id="getting-a-list-of-all-archived-orders">Getting A List Of All Archived Orders</span>

```http
GET /api/v1/archived_orders?end_time=2020-04-20T23:59:59Z&start_time=2020-04-20T00:00:00Z
```

This returns a paginated response of archived orders across all projects and sites, accessible
by the account associated with the API key authorizing the request that have been archived
between the `start_time` and `end_time`.

### <span id="getting-a-list-of-all-archived-orders-parameters">Parameters</span>



| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `start_time` | `string` | **Required.** The API returns only archived orders that have an `archived_at` that is later than the provided value. |
| `end_time` | `string` | **Required.** The API returns only archived orders that have an `archived_at` that is earlier than the provided value. |
| `partner_identifier` | `string` | _Optional._ If given, the API returns only archived orders with a `partner_identifier` that matches the provided value. |
| `page` | `integer` | _Optional._ Allows retrieving a specific page of the results. Defaults to 1. |
| `per` | `integer` | _Optional._ Specifies how many archived orders should be included in a page of results. Defaults to 50. |

### <span id="getting-a-list-of-all-archived-orders-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "time_range": {
    "start_time": "2020-04-20T00:00:00.000Z",
    "end_time": "2020-04-20T23:59:59.000Z"
  },
  "data": [
    {
      "type": "archived_order",
      "id": 1,
      "archived_at": "2020-04-20T18:00:00.000Z",
      "arrived_at": null,
      "completed_at": null,
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

### <span id="getting-a-list-of-all-archived-orders-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/archived_orders?end_time=2020-04-20T23:59:59Z&start_time=2020-04-20T00:00:00Z \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```

## <span id="getting-archived-orders-with-a-given-partner-identifier">Getting Archived Orders With A Given Partner Identifier</span>

```http
GET /api/v1/archived_orders?end_time=2020-04-20T23:59:59Z&partner_identifier=1234&start_time=2020-04-20T00:00:00Z
```

### <span id="getting-archived-orders-with-a-given-partner-identifier-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "time_range": {
    "start_time": "2020-04-20T00:00:00.000Z",
    "end_time": "2020-04-20T23:59:59.000Z"
  },
  "data": [
    {
      "type": "archived_order",
      "id": 1,
      "archived_at": "2020-04-20T18:00:00.000Z",
      "arrived_at": null,
      "completed_at": null,
      "location_permission": null,
      "location_started_at": null,
      "order_reminder_at": null,
      "partner_identifier": "1234",
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

### <span id="getting-archived-orders-with-a-given-partner-identifier-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/archived_orders?end_time=2020-04-20T23:59:59Z&partner_identifier=1234&start_time=2020-04-20T00:00:00Z \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```

## <span id="getting-archived-orders-with-a-given-project-id">Getting Archived Orders With A Given Project ID</span>

```http
GET /api/v1/archived_orders?end_time=2020-04-20T23:59:59Z&project_id=593363173&start_time=2020-04-20T00:00:00Z
```

### <span id="getting-archived-orders-with-a-given-project-id-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "time_range": {
    "start_time": "2020-04-20T00:00:00.000Z",
    "end_time": "2020-04-20T23:59:59.000Z"
  },
  "data": [
    {
      "type": "archived_order",
      "id": 1,
      "archived_at": "2020-04-20T18:00:00.000Z",
      "arrived_at": null,
      "completed_at": null,
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
      "project_id": 593363173,
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

### <span id="getting-archived-orders-with-a-given-project-id-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/archived_orders?end_time=2020-04-20T23:59:59Z&project_id=593363173&start_time=2020-04-20T00:00:00Z \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```
