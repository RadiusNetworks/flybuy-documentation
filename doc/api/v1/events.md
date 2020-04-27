# Events API

- [API Specs](#api-specs)
- [Adding A State Change Event](#adding-a-state-change-event)
- [Adding A Location Update Event](#adding-a-location-update-event)
- [Adding A Customer Rating Event](#adding-a-customer-rating-event)
- [Adding An Event To An Order That Is No Longer Active](#adding-an-event-to-an-order-that-is-no-longer-active)

This describes the FlyBuy Events API v1. If you have any problems or
requests please contact [support](https://support.radiusnetworks.com).

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


## <span id="adding-a-state-change-event">Adding A State Change Event</span>

```http
POST /api/v1/events
```

### <span id="adding-a-state-change-event-parameters">Parameters</span>

**Must** be sent under a top-level `data` parameter.

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `order_id` | `integer` | **Required.** Must reference an existing order. |
| `event_type` | `string` | **Required.** Must be `"state_change"`. |
| `eta_seconds` | `integer` | if a value is given, the ETA for the order will be adjusted to this number of seconds into the future. |
| `state` | `string` | Must be one of the following: `"created"`, `"ready"`, `"delayed"`, `"cancelled"`, `"completed"`. |
| `customer_state` | `string` | Must be one of the following: `"created"`, `"en_route"`, `"nearby"`, `"arrived"`, `"waiting"`, `"completed"`. |

### <span id="adding-a-state-change-event-example">Example</span>

```json
{
  "data": {
    "order_id": 1,
    "event_type": "state_change",
    "state": "delayed"
  }
}
```

### <span id="adding-a-state-change-event-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json
```

### <span id="adding-a-state-change-event-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/events \
  -is \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"' \
  -d '{
    "data": {
      "order_id": 1,
      "event_type": "state_change",
      "state": "delayed"
    }
  }'
```

## <span id="adding-a-location-update-event">Adding A Location Update Event</span>

```http
POST /api/v1/events
```

### <span id="adding-a-location-update-event-parameters">Parameters</span>

**Must** be sent under a top-level `data` parameter.

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `order_id` | `integer` | **Required.** Must reference an existing order. |
| `event_type` | `string` | **Required.** Must be `"location_update"`. |
| `eta_seconds` | `integer` | if a value is given, the ETA for the order will be adjusted to this number of seconds into the future. |
| `longitude` | `decimal` | The user's longitude. |
| `latitude` | `decimal` | The user's latitude. |
| `accuracy` | `decimal` | When providing the user's coordinates, this gives the accuracy of those coordinates in meters. |
| `speed` | `decimal` | The user's speed in meters / second. |

### <span id="adding-a-location-update-event-example">Example</span>

```json
{
  "data": {
    "order_id": 1,
    "event_type": "location_update",
    "longitude": -77.0650202035904,
    "latitude": 38.903783196923044,
    "accuracy": 8,
    "speed": 0.5
  }
}
```

### <span id="adding-a-location-update-event-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json
```

### <span id="adding-a-location-update-event-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/events \
  -is \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"' \
  -d '{
    "data": {
      "order_id": 1,
      "event_type": "location_update",
      "longitude": -77.0650202035904,
      "latitude": 38.903783196923044,
      "accuracy": 8,
      "speed": 0.5
    }
  }'
```

## <span id="adding-a-customer-rating-event">Adding A Customer Rating Event</span>

```http
POST /api/v1/events
```

### <span id="adding-a-customer-rating-event-parameters">Parameters</span>

**Must** be sent under a top-level `data` parameter. The order must be **completed** to create a customer rating event (either customer state or order state).

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `order_id` | `integer` | **Required.** Must reference an existing order. |
| `event_type` | `string` | **Required.** Must be `"customer_rating"`. |
| `customer_rating_value` | `integer` | The customer's star rating of the order (1-5). |
| `customer_rating_comments` | `string` | Any feedback comments from the customer about the order |

### <span id="adding-a-customer-rating-event-example">Example</span>

```json
{
  "data": {
    "order_id": 1,
    "event_type": "customer_rating",
    "customer_rating_value": 5,
    "customer_rating_comments": "Comments go here"
  }
}
```

### <span id="adding-a-customer-rating-event-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json
```

### <span id="adding-a-customer-rating-event-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/events \
  -is \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"' \
  -d '{
    "data": {
      "order_id": 1,
      "event_type": "customer_rating",
      "customer_rating_value": 5,
      "customer_rating_comments": "Comments go here"
    }
  }'
```

## <span id="adding-an-event-to-an-order-that-is-no-longer-active">Adding An Event To An Order That Is No Longer Active</span>

```http
POST /api/v1/events
```

If an event is added to an order that is no longer active, the service will respond
with a status of [`410 Gone`](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#410).
This should indicate to the client that it should not attempt to send any more events for
this order.

### <span id="adding-an-event-to-an-order-that-is-no-longer-active-response">Response</span>

```http
Status: 410 Gone
Content-Type: application/json
```

### <span id="adding-an-event-to-an-order-that-is-no-longer-active-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/events \
  -is \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"' \
  -d '{
    "data": {
      "order_id": 1,
      "event_type": "location_update",
      "longitude": -77.0650202035904,
      "latitude": 38.903783196923044,
      "accuracy": 8,
      "speed": 0.5
    }
  }'
```