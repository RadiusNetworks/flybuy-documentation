# Order Events API

- [API Specs](#api-specs)
- [Send A State Change Event](#send-a-state-change-event)
- [Send A Location Update Event](#send-a-location-update-event)
- [Send A Customer Rating Event](#send-a-customer-rating-event)

The FlyBuy Order Events API enables partners to send order events for an already existing order.

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

### Error Codes
If an event is sent for an order that is no longer active, the API will respond with a status of `410 Gone`.
In this case, do not make any more attempts to send events for the order.


## <span id="send-a-state-change-event">Send A State Change Event</span>

```http
POST /api/v1/events
```

### <span id="send-a-state-change-event-parameters">Parameters</span>

The body payload should be a JSON object. All items must be sent under a top-level `data` parameter.

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `order_id` | `integer` | **Required.** The FlyBuy order identifer that gets returned when an order is created. |
| `event_type` | `string` | **Required.** Must be `"state_change"`. |
| `eta_seconds` | `integer` | The number of seconds until the customer arrives on-site. |
| `state` | `string` | Must be one of the following: `"ready"`, `"delayed"`, `"cancelled"` `"completed"`. |
| `customer_state` | `string` | Must be one of the following: `"nearby"`, `"arrived"`, `"waiting"`, `"completed"`. |

### <span id="send-a-state-change-event-example">Example</span>

```json
{
  "data": {
    "order_id": 1,
    "event_type": "state_change",
    "state": "delayed"
  }
}
```

### <span id="send-a-state-change-event-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json
```

### <span id="send-a-state-change-event-curl-example">Curl Example</span>

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

## <span id="send-a-location-update-event">Send A Location Update Event</span>

```http
POST /api/v1/events
```

### <span id="send-a-location-update-event-parameters">Parameters</span>

The body payload should be a JSON object. All items must be sent under a top-level `data` parameter.

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `order_id` | `integer` | **Required.** The FlyBuy order identifer that gets returned when an order is created. |
| `event_type` | `string` | **Required.** Must be `"location_update"`. |
| `eta_seconds` | `integer` | The number of seconds until the customer arrives on-site. |
| `longitude` | `decimal` | The customer's longitude. |
| `latitude` | `decimal` | The customer's latitude. |
| `accuracy` | `decimal` | The accuracy of `longitude` and `latitude` in meters, if provided. |
| `speed` | `decimal` | The customer's speed in meters/second. |

### <span id="send-a-location-update-event-example">Example</span>

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

### <span id="send-a-location-update-event-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json
```

### <span id="send-a-location-update-event-curl-example">Curl Example</span>

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

## <span id="send-a-customer-rating-event">Send A Customer Rating Event</span>

```http
POST /api/v1/events
```

To send a customer rating event, the order or customer state must be `completed`.

### <span id="send-a-customer-rating-event-parameters">Parameters</span>

The body payload should be a JSON object. All items must be sent under a top-level `data` parameter.

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `order_id` | `integer` | **Required.** The FlyBuy order identifer that gets returned when an order is created. |
| `event_type` | `string` | **Required.** Must be `"customer_rating"`. |
| `customer_rating_value` | `integer` | The customer's star rating of the order (1-5). |
| `customer_rating_comments` | `string` | Any feedback comments from the customer about the order. |

### <span id="send-a-customer-rating-event-example">Example</span>

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

### <span id="send-a-customer-rating-event-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json
```

### <span id="send-a-customer-rating-event-curl-example">Curl Example</span>

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
