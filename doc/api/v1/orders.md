# Orders API

- [Getting An Order](#getting-an-order)
- [Creating An Order](#creating-an-order)
- [Updating An Order](#updating-an-order)

This describes the FlyBuy Orders API v1. If you have any problems or
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

## <span id="getting-an-order">Getting An Order</span>

```http
GET /api/v1/orders/1
```

### <span id="getting-an-order-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "data": {
    "type": "order",
    "order_id": 1,
    "order_state": "created",
    "id": 1,
    "arrived_at": null,
    "customer_state": "created",
    "eta_at": null,
    "partner_identifier": null,
    "state": "created",
    "redemption_code": "31S4VF",
    "created_at": "2020-02-20T17:23:39.708Z",
    "updated_at": "2020-02-20T17:23:39.708Z",
    "area_name": null,
    "customer_id": null,
    "site_id": 1,
    "site_partner_identifier": "site1",
    "customer_name": null,
    "customer_car_type": null,
    "customer_car_color": null,
    "customer_license_plate": null,
    "customer_rating_value": null,
    "customer_rating_comments": null,
    "pickup_window": "2020-02-20T15:23:39.706Z/2020-02-20T16:23:39.706Z",
    "push_token": null
  },
  "included": [
    {
      "type": "site",
      "id": 1,
      "partner_identifier": "site1",
      "name": "A Site",
      "full_address": "123 Any Street, Any Locality, Any Region, 12345",
      "street_address": "123 Any Street",
      "locality": "Any Locality",
      "region": "Any Region",
      "country": "Any Country",
      "postal_code": "12345",
      "latitude": "0.0",
      "longitude": "0.0",
      "instructions": null,
      "description": null,
      "phone": "555-367-8309"
    }
  ]
}
```

### <span id="getting-an-order-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/orders/1?include=site \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"'
```

## <span id="creating-an-order">Creating An Order</span>

```http
POST /api/v1/orders
```

### <span id="creating-an-order-parameters">Parameters</span>

**Must** be sent under a top-level `data` parameter.

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `site_id` | `integer` | **Required.** Must reference a site in a project you have access to. |
| `customer_name` | `string` | _Optional._ The customer's name |
| `customer_token` | `string` | _Optional._ If given a customer token the order will be linked with their account, otherwise the customer will be required to redeem the order via a link supplied by the system. |
| `customer_phone` | `string` | _Optional._ The customer's phone number. |
| `customer_car_color` | `string` | _Optional._ The color of the customer's car. |
| `customer_car_type` | `string` | _Optional._ The customer's car type |
| `customer_license_plate` | `string` | _Optional._ The customer's license plate |
| `partner_identifier` | `string` | _Optional._ An identifier used to track this order in another system. |
| `push_token` | `string` | _Optional._ A token used to send push notifications to the user's mobile device |
| `pickup_window` | `string` | _Optional._ When the order should be picked up. It can either be a date/time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601), or a [date/time interval](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) of the format `"start/end"` |

### <span id="creating-an-order-example">Example</span>

```json
{
  "data": {
    "site_id": 1,
    "partner_identifier": "123XYZ",
    "customer_name": "William Adama",
    "pickup_window": "2019-03-25T17:57:34.603Z"
  }
}
```

### <span id="creating-an-order-response">Response</span>

```http
Status: 201 Created
Content-Type: application/json; charset=utf-8
```
```json
{
  "data": {
    "type": "order",
    "order_id": 1,
    "order_state": "created",
    "id": 1,
    "arrived_at": null,
    "customer_state": "created",
    "eta_at": null,
    "partner_identifier": "123XYZ",
    "state": "created",
    "redemption_code": "RRMFJF",
    "created_at": "2020-02-20T17:23:39.891Z",
    "updated_at": "2020-02-20T17:23:39.891Z",
    "area_name": null,
    "customer_id": null,
    "site_id": 1,
    "site_partner_identifier": "site1",
    "customer_name": "William Adama",
    "customer_car_type": null,
    "customer_car_color": null,
    "customer_license_plate": null,
    "customer_rating_value": null,
    "customer_rating_comments": null,
    "pickup_window": "2019-03-25T17:57:34.603Z/2019-03-25T17:57:34.603Z",
    "push_token": null
  },
  "included": [

  ]
}
```

### <span id="creating-an-order-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/orders \
  -is \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"' \
  -d '{
    "data": {
      "site_id": 1,
      "partner_identifier": "123XYZ",
      "customer_name": "William Adama",
      "pickup_window": "2019-03-25T17:57:34.603Z"
    }
  }'
```

## <span id="updating-an-order">Updating An Order</span>

```http
PUT /api/v1/orders/1
```

### <span id="updating-an-order-parameters">Parameters</span>

**Must** be sent under a top-level `data` parameter.

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `site_id` | `integer` | **Required.** Must reference a site in a project you have access to. |
| `customer_name` | `string` | _Optional._ The customer's name |
| `customer_phone` | `string` | _Optional._ The customer's phone number. |
| `customer_car_color` | `string` | _Optional._ The color of the customer's car. |
| `customer_car_type` | `string` | _Optional._ The customer's car type |
| `customer_license_plate` | `string` | _Optional._ The customer's license plate |
| `partner_identifier` | `string` | _Optional._ An identifier used to track this order in another system. |
| `push_token` | `string` | _Optional._ A token used to send push notifications to the user's mobile device |
| `pickup_window` | `string` | _Optional._ When the order should be picked up. It can either be a date/time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601), or a [date/time interval](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) of the format `"start/end"` |

### <span id="updating-an-order-example">Example</span>

```json
{
  "data": {
    "site_id": 1,
    "pickup_window": "2020-02-20T15:23:39.961Z/2020-02-20T16:23:39.961Z"
  }
}
```

### <span id="updating-an-order-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "data": {
    "type": "order",
    "order_id": 1,
    "order_state": "created",
    "id": 1,
    "arrived_at": null,
    "customer_state": "created",
    "eta_at": null,
    "partner_identifier": null,
    "state": "created",
    "redemption_code": "UGZFJJ",
    "created_at": "2020-02-20T17:23:40.001Z",
    "updated_at": "2020-02-20T17:23:40.019Z",
    "area_name": null,
    "customer_id": null,
    "site_id": 1,
    "site_partner_identifier": "site1",
    "customer_name": null,
    "customer_car_type": null,
    "customer_car_color": null,
    "customer_license_plate": null,
    "customer_rating_value": null,
    "customer_rating_comments": null,
    "pickup_window": "2020-02-20T15:23:39.961Z/2020-02-20T16:23:39.961Z",
    "push_token": null
  },
  "included": [

  ]
}
```

### <span id="updating-an-order-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/orders/1 \
  -is \
  -X PUT \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"' \
  -d '{
    "data": {
      "site_id": 1,
      "pickup_window": "2020-02-20T15:23:39.961Z/2020-02-20T16:23:39.961Z"
    }
  }'
```
