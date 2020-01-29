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
    "id": 1,
    "arrived_at": null,
    "customer_state": "created",
    "eta_at": null,
    "partner_identifier": null,
    "state": "created",
    "redemption_code": "SHTBHF",
    "created_at": "2019-12-17T19:57:03.091Z",
    "updated_at": "2019-12-17T19:57:03.091Z",
    "area_name": null,
    "customer_id": null,
    "site_id": 1,
    "site_partner_identifier": "site1",
    "customer_name": null,
    "customer_car_type": null,
    "customer_car_color": null,
    "customer_license_plate": null,
    "pickup_window": "2019-12-17T17:57:03.089Z/2019-12-17T18:57:03.089Z"
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
curl http://www.example.com/api/v1/orders/1?include=site \
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

| **Name** | **Type** | **Description** | **Required** |
| -------- | -------- | --------------- | ----- |
| `site_id` | `integer` | Must reference a site in a project you have access to. | **Required** |
| `customer_name` | `string` | The customer's name | _Optional_ |
| `customer_token` | `string` | If given a customer token the order will be linked with their account, otherwise the customer will be required to redeem the order via a link supplied by the system. | _Optional_ |
| `customer_phone` | `string` | The customer's phone number | _Optional_ |
| `customer_car_color` | `string` | The color of the customer's car. | _Optional_ |
| `customer_car_type` | `string` | The customer's car type | _Optional_ |
| `customer_license_plate` | `string` | The customer's license plate | _Optional_ |
| `partner_identifier` | `string` | An identifier used to track this order in another system. | _Optional_ |
| `push_token` | `string` | A token used to send push notifications to the user's mobile device | _Optional_ |
| `pickup_window` | `string` | When the order should be picked up. It can either be a date/time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601), or a [date/time interval](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) of the format `"start/end"` | _Optional_ |

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
    "id": 1,
    "arrived_at": null,
    "customer_state": "created",
    "eta_at": null,
    "partner_identifier": "123XYZ",
    "state": "created",
    "redemption_code": "N6CNEQ",
    "created_at": "2019-12-17T19:57:03.228Z",
    "updated_at": "2019-12-17T19:57:03.228Z",
    "area_name": null,
    "customer_id": null,
    "site_id": 1,
    "site_partner_identifier": "site1",
    "customer_name": "William Adama",
    "customer_car_type": null,
    "customer_car_color": null,
    "customer_license_plate": null,
    "pickup_window": "2019-03-25T17:57:34.603Z/2019-03-25T17:57:34.603Z"
  },
  "included": [

  ]
}
```

### <span id="creating-an-order-curl-example">Curl Example</span>

```sh
curl http://www.example.com/api/v1/orders \
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

| **Name** | **Type** | **Description** | **Required** |
| -------- | -------- | --------------- | ------------ |
| `site_id` | `integer` | Must reference a site in a project you have access to. | **Required** |
| `customer_name` | `string` | The customer's name | _Optional_ |
| `customer_phone` | `string` | The customer's phone number | _Optional_ |
| `customer_car_color` | `string` | The color of the customer's car. | _Optional_ |
| `customer_car_type` | `string` | The customer's car type | _Optional_ |
| `customer_license_plate` | `string` | The customer's license plate | _Optional_ |
| `partner_identifier` | `string` | An identifier used to track this order in another system. | _Optional_ |
| `push_token` | `string` | A token used to send push notifications to the user's mobile device | _Optional_ |
| `pickup_window` | `string` | When the order should be picked up. It can either be a date/time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601), or a [date/time interval](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) of the format `"start/end"` | _Optional_ |

### <span id="updating-an-order-example">Example</span>

```json
{
  "data": {
    "site_id": 1,
    "pickup_window": "2019-12-17T17:57:03.290Z/2019-12-17T18:57:03.290Z"
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
    "id": 1,
    "arrived_at": null,
    "customer_state": "created",
    "eta_at": null,
    "partner_identifier": null,
    "state": "created",
    "redemption_code": "I9HS3H",
    "created_at": "2019-12-17T19:57:03.314Z",
    "updated_at": "2019-12-17T19:57:03.326Z",
    "area_name": null,
    "customer_id": null,
    "site_id": 1,
    "site_partner_identifier": "site1",
    "customer_name": null,
    "customer_car_type": null,
    "customer_car_color": null,
    "customer_license_plate": null,
    "pickup_window": "2019-12-17T17:57:03.290Z/2019-12-17T18:57:03.290Z"
  },
  "included": [

  ]
}
```

### <span id="updating-an-order-curl-example">Curl Example</span>

```sh
curl http://www.example.com/api/v1/orders/1 \
  -is \
  -X PUT \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"' \
  -d '{
    "data": {
      "site_id": 1,
      "pickup_window": "2019-12-17T17:57:03.290Z/2019-12-17T18:57:03.290Z"
    }
  }'
```

