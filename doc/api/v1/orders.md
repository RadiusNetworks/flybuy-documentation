# Orders API

- [Getting A List Of All Orders](#getting-a-list-of-all-orders)
- [Getting Orders With A Given Partner Identifier](#getting-orders-with-a-given-partner-identifier)
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

## <span id="getting-a-list-of-all-orders">Getting A List Of All Orders</span>

```http
GET /api/v1/orders
```

This returns a paginated response of all orders, across all projects and sites, accessible by
the account associated with the API key authorizing the request.

### <span id="getting-a-list-of-all-orders-parameters">Parameters</span>



| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `partner_identifier` | `string` | _Optional._ If given, the API returns only orders with a `partner_identifier` that matches the provided value. |
| `page` | `integer` | _Optional._ Allows retrieving a specific page of the results. Defaults to 1. |
| `per` | `integer` | _Optional._ Specifies how many orders should be included in a page of results. Defaults to 50. |

### <span id="getting-a-list-of-all-orders-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "data": [
    {
      "type": "order",
      "order_id": 1,
      "order_state": "created",
      "redemption_url": "http://flybuy.radiusnetworks.com/m/o?r=QJ1ZED",
      "id": 1,
      "arrived_at": null,
      "customer_state": "created",
      "eta_at": null,
      "partner_identifier": null,
      "state": "created",
      "redemption_code": "QJ1ZED",
      "created_at": "2020-03-22T18:46:41.706Z",
      "updated_at": "2020-03-22T18:46:41.706Z",
      "area_name": null,
      "customer_id": null,
      "site_id": 1,
      "site_partner_identifier": "site1",
      "customer_name": null,
      "customer_car_type": null,
      "customer_car_color": null,
      "customer_license_plate": null,
      "customer_rating_value": null,
      "customer_rating_value_string": "",
      "customer_rating_comments": null,
      "pickup_window": "2020-03-22T16:46:41.704Z/2020-03-22T17:46:41.704Z",
      "push_token": null
    }
  ],
  "pages": {
    "current": 1,
    "count": 1,
    "per": 50
  }
}
```

### <span id="getting-a-list-of-all-orders-curl-example">Curl Example</span>

```sh
curl http://flybuy.radiusnetworks.com/api/v1/orders \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"'
```

## <span id="getting-orders-with-a-given-partner-identifier">Getting Orders With A Given Partner Identifier</span>

```http
GET /api/v1/orders?partner_identifier=12345
```

### <span id="getting-orders-with-a-given-partner-identifier-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "data": [
    {
      "type": "order",
      "order_id": 1,
      "order_state": "created",
      "redemption_url": "http://flybuy.radiusnetworks.com/m/o?r=EXACCT",
      "id": 1,
      "arrived_at": null,
      "customer_state": "created",
      "eta_at": null,
      "partner_identifier": "12345",
      "state": "created",
      "redemption_code": "EXACCT",
      "created_at": "2020-03-22T18:46:41.893Z",
      "updated_at": "2020-03-22T18:46:41.893Z",
      "area_name": null,
      "customer_id": null,
      "site_id": 1,
      "site_partner_identifier": "site1",
      "customer_name": null,
      "customer_car_type": null,
      "customer_car_color": null,
      "customer_license_plate": null,
      "customer_rating_value": null,
      "customer_rating_value_string": "",
      "customer_rating_comments": null,
      "pickup_window": "2020-03-22T16:46:41.891Z/2020-03-22T17:46:41.891Z",
      "push_token": null
    }
  ],
  "pages": {
    "current": 1,
    "count": 1,
    "per": 50
  }
}
```

### <span id="getting-orders-with-a-given-partner-identifier-curl-example">Curl Example</span>

```sh
curl http://flybuy.radiusnetworks.com/api/v1/orders?partner_identifier=12345 \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"'
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
    "redemption_url": "http://flybuy.radiusnetworks.com/m/o?r=H8PUYP",
    "id": 1,
    "arrived_at": null,
    "customer_state": "created",
    "eta_at": null,
    "partner_identifier": null,
    "state": "created",
    "redemption_code": "H8PUYP",
    "created_at": "2020-03-22T18:46:41.999Z",
    "updated_at": "2020-03-22T18:46:41.999Z",
    "area_name": null,
    "customer_id": null,
    "site_id": 1,
    "site_partner_identifier": "site1",
    "customer_name": null,
    "customer_car_type": null,
    "customer_car_color": null,
    "customer_license_plate": null,
    "customer_rating_value": null,
    "customer_rating_value_string": "",
    "customer_rating_comments": null,
    "pickup_window": "2020-03-22T16:46:41.997Z/2020-03-22T17:46:41.997Z",
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
curl http://flybuy.radiusnetworks.com/api/v1/orders/1?include=site \
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
    "redemption_url": "http://flybuy.radiusnetworks.com/m/o?r=2YCKLS",
    "id": 1,
    "arrived_at": null,
    "customer_state": "created",
    "eta_at": null,
    "partner_identifier": "123XYZ",
    "state": "created",
    "redemption_code": "2YCKLS",
    "created_at": "2020-03-22T18:46:42.143Z",
    "updated_at": "2020-03-22T18:46:42.143Z",
    "area_name": null,
    "customer_id": null,
    "site_id": 1,
    "site_partner_identifier": "site1",
    "customer_name": "William Adama",
    "customer_car_type": null,
    "customer_car_color": null,
    "customer_license_plate": null,
    "customer_rating_value": null,
    "customer_rating_value_string": "",
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
curl http://flybuy.radiusnetworks.com/api/v1/orders \
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
    "pickup_window": "2020-03-22T16:46:42.214Z/2020-03-22T17:46:42.214Z"
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
    "redemption_url": "http://flybuy.radiusnetworks.com/m/o?r=JJSSES",
    "id": 1,
    "arrived_at": null,
    "customer_state": "created",
    "eta_at": null,
    "partner_identifier": null,
    "state": "created",
    "redemption_code": "JJSSES",
    "created_at": "2020-03-22T18:46:42.254Z",
    "updated_at": "2020-03-22T18:46:42.267Z",
    "area_name": null,
    "customer_id": null,
    "site_id": 1,
    "site_partner_identifier": "site1",
    "customer_name": null,
    "customer_car_type": null,
    "customer_car_color": null,
    "customer_license_plate": null,
    "customer_rating_value": null,
    "customer_rating_value_string": "",
    "customer_rating_comments": null,
    "pickup_window": "2020-03-22T16:46:42.214Z/2020-03-22T17:46:42.214Z",
    "push_token": null
  },
  "included": [

  ]
}
```

### <span id="updating-an-order-curl-example">Curl Example</span>

```sh
curl http://flybuy.radiusnetworks.com/api/v1/orders/1 \
  -is \
  -X PUT \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"' \
  -d '{
    "data": {
      "site_id": 1,
      "pickup_window": "2020-03-22T16:46:42.214Z/2020-03-22T17:46:42.214Z"
    }
  }'
```
