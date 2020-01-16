# Events API

- [Adding A State Change Event](#adding-a-state-change-event)
- [Adding A Location Update Event](#adding-a-location-update-event)
- [Adding An Event To An Order That Is No Longer Active](#adding-an-event-to-an-order-that-is-no-longer-active)

This describes the FlyBuy Events API v1. If you have any problems or
requests please contact [support](https://support.radiusnetworks.com).

## Headers <a href="#headers" id="headers" class="headerlink"></a>

The API Key is passed via the Authorization header:

```http
Authorization: Token token="secret"
```

The API Key is associated with your account and has access to all the resources
associated with your account. Account specific API keys have different
permissions than the web login users that can interact with the dashboard, and
the access may be different.

If you do not have an API key, [you can create one here](https://account.radiusnetworks.com/personal_tokens).

### Content Type <a href="#content-type" id="content-type" class="headerlink"></a>
The content type is `application/json` and should be set in the `Content-Type`
header:
```http
Content-Type: application/json
```

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
curl http://www.example.com/api/v1/events \
  -is \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"' \
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
curl http://www.example.com/api/v1/events \
  -is \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"' \
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
curl http://www.example.com/api/v1/events \
  -is \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"' \
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
