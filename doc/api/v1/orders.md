# Orders API

- [API Specs](#api-specs)
- [Create An Order](#create-an-order)
- [Create An Order With Tags](#create-an-order-with-tags)
- [Get An Order With A FlyBuy Order Identifer](#get-an-order-with-a-flybuy-order-identifer)
- [Get An Order With A Partner Order Identifier](#get-an-order-with-a-partner-order-identifier)
- [Get A List Of All Orders](#get-a-list-of-all-orders)
- [Update An Order](#update-an-order)

The FlyBuy Orders API enables partners to create orders, fetch information about an order, and update order details.

Must Do's:
- To kick off the FlyBuy experience for a customer, an order must be created at minimum.
- FlyBuy also requires an order to be in the `ready` state to start collecting location information from the customer.
Once the order is ready, [send](doc/api/v1/events.md#adding-a-state-change-event) a `ready` state change for the order.
If your system does not have a distinct `ready` state that would ever get sent, send FlyBuy the `ready` state change immediately after creating an order.

## <span id="api-specs">API Specs</span>

A sample Postman collection can be found [here](https://www.getpostman.com/collections/3684da81f53275af8c22).
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

### <span id="api-specs-parameters">Parameters</span>

When creating and updating orders, the body payload should be a JSON object. All items must be sent under a top-level `data` object unless they are specified as `metadata`. Items that are specified as `metadata` must be passed in as a top-level `metadata` object.

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `site_id` | `integer` | **Required.** A FlyBuy site identifier that references a site in a project you have access to. |
| `customer_phone` | `string` | _Recommended._ The customer's phone number. The customer's phone number is required to initiate the FlyBuy experience. |
| `customer_name` | `string` | _Optional._ The customer's name. |
| `customer_token` | `string` | _Optional._ If given a customer token, FlyBuy will automatically associate the order with the customer's account. Otherwise, the customer will be required to redeem the order via a link supplied by the system. This can only be used when creating the order. |
| `customer_car_color` | `string` | _Optional._ The color of the customer's car. |
| `customer_car_type` | `string` | _Optional._ The customer's car type (ex: Toyota Camry). |
| `customer_license_plate` | `string` | _Optional._ The customer's license plate. |
| `partner_identifier` | `string` | _Optional._ An identifier used to track this order in another system. If provided, an order can also be retrieved using this value. |
| `push_token` | `string` | _Optional._ A token used to send push notifications to the user's mobile device. |
| `pickup_window` | `string` | _Optional._ When the order should be picked up. It can either be a date/time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601), or a [date/time interval](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) of the format `"start/end"`. |
| `metadata.taggable_keywords` | `string` | _Optional._ If matching tags are found, they will be applied to the order. |


## <span id="create-an-order">Create An Order</span>

```http
POST /api/v1/orders
```

### <span id="create-an-order-response">Response</span>

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
    "redemption_url": "https://flybuy.radiusnetworks.com/m/o?r=TFPQUVAXA5",
    "id": 1,
    "arrived_at": null,
    "customer_state": "created",
    "eta_at": null,
    "partner_identifier": "123XYZ",
    "state": "created",
    "redemption_code": "TFPQUVAXA5",
    "created_at": "2020-04-24T19:19:45.000Z",
    "updated_at": "2020-04-24T19:19:45.000Z",
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
    "pickup_type": null,
    "push_token": null,
    "tag_ids": [

    ]
  },
  "included": [

  ]
}
```

### <span id="create-an-order-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/orders \
  -is \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"' \
  -d '{
    "data": {
      "site_id": 1,
      "partner_identifier": "123XYZ",
      "customer_name": "William Adama",
      "pickup_window": "2019-03-25T17:57:34.603Z"
    }
  }'
```

## <span id="create-an-order-with-tags">Create An Order With Tags</span>

```http
POST /api/v1/orders?include=tags
```

Tags allow UI customization in the FlyBuy dashboard.
For example, if an order is created with a tag called `fries`, FlyBuy can associate that tag with an image of fries to provide a visual cue to the staff that a particular order contains fries.

### <span id="create-an-order-with-tags-response">Response</span>

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
    "redemption_url": "https://flybuy.radiusnetworks.com/m/o?r=TFPQUVAXA5",
    "id": 1,
    "arrived_at": null,
    "customer_state": "created",
    "eta_at": null,
    "partner_identifier": "123XYZ",
    "state": "created",
    "redemption_code": "TFPQUVAXA5",
    "created_at": "2020-04-24T19:19:45.000Z",
    "updated_at": "2020-04-24T19:19:45.000Z",
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
    "pickup_type": null,
    "push_token": null,
    "tag_ids": [
      1
    ]
  },
  "included": [
    {
      "type": "tag",
      "id": 1,
      "name": "Fries"
    }
  ]
}
```

### <span id="create-an-order-with-tags-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/orders?include=tags \
  -is \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"' \
  -d '{
    "data": {
      "site_id": 1,
      "partner_identifier": "123XYZ",
      "customer_name": "William Adama",
      "pickup_window": "2019-03-25T17:57:34.603Z"
    },
    "metadata": {
      "taggable_keywords": [
        "fries"
      ]
    }
  }'
```

## <span id="get-an-order-with-a-flybuy-order-identifer">Get An Order With A FlyBuy Order Identifer</span>

```http
GET /api/v1/orders/1?include=site,tags
```

Orders can be fetched with a FlyBuy order identifer (1 in the example above).
This unique value is returned as order_id when creating an order via the API.

If you would like to view site or tag information for the order, add `include=site,tags` in the query parameters.

### <span id="get-an-order-with-a-flybuy-order-identifer-response">Response</span>

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
    "redemption_url": "https://flybuy.radiusnetworks.com/m/o?r=TFPQUVAXA5",
    "id": 1,
    "arrived_at": null,
    "customer_state": "created",
    "eta_at": null,
    "partner_identifier": null,
    "state": "created",
    "redemption_code": "TFPQUVAXA5",
    "created_at": "2020-04-24T19:19:45.000Z",
    "updated_at": "2020-04-24T19:19:45.000Z",
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
    "pickup_window": "2020-04-24T17:19:45.000Z/2020-04-24T18:19:45.000Z",
    "pickup_type": null,
    "push_token": null,
    "tag_ids": [
      1
    ]
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
    },
    {
      "type": "tag",
      "id": 1,
      "name": "Fries"
    }
  ]
}
```

### <span id="get-an-order-with-a-flybuy-order-identifer-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/orders/1?include=site,tags \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```

## <span id="get-an-order-with-a-partner-order-identifier">Get An Order With A Partner Order Identifier</span>

```http
GET /api/v1/orders?partner_identifier=12345
```

Orders can be fetched with a partner order identifier (12345 in the example above).
This value can be optionally passed in as partner_identifier when creating an order via the API.

FlyBuy does not guarantee uniqueness for a partner order identifier.
For a unique identifier, use the FlyBuy order identifier (order_id) instead.

### <span id="get-an-order-with-a-partner-order-identifier-response">Response</span>

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
      "redemption_url": "https://flybuy.radiusnetworks.com/m/o?r=TFPQUVAXA5",
      "id": 1,
      "arrived_at": null,
      "customer_state": "created",
      "eta_at": null,
      "partner_identifier": "12345",
      "state": "created",
      "redemption_code": "TFPQUVAXA5",
      "created_at": "2020-04-24T19:19:45.000Z",
      "updated_at": "2020-04-24T19:19:45.000Z",
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
      "pickup_window": "2020-04-24T17:19:45.000Z/2020-04-24T18:19:45.000Z",
      "pickup_type": null,
      "push_token": null,
      "tag_ids": [

      ]
    }
  ],
  "pages": {
    "current": 1,
    "count": 1,
    "per": 50
  }
}
```

### <span id="get-an-order-with-a-partner-order-identifier-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/orders?partner_identifier=12345 \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```

## <span id="get-a-list-of-all-orders">Get A List Of All Orders</span>

```http
GET /api/v1/orders
```

This returns a paginated response of all orders that the owner of the API key has access to.
Typically, this spans multiple projects and sites.

### <span id="get-a-list-of-all-orders-parameters">Parameters</span>



| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `partner_identifier` | `string` | _Optional._ If given, the API returns only orders with a `partner_identifier` that matches the provided value. |
| `page` | `integer` | _Optional._ Allows retrieving a specific page of the results. Defaults to 1. |
| `per` | `integer` | _Optional._ Specifies how many orders should be included in a page of results. Defaults to 50. |

### <span id="get-a-list-of-all-orders-response">Response</span>

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
      "redemption_url": "https://flybuy.radiusnetworks.com/m/o?r=TFPQUVAXA5",
      "id": 1,
      "arrived_at": null,
      "customer_state": "created",
      "eta_at": null,
      "partner_identifier": null,
      "state": "created",
      "redemption_code": "TFPQUVAXA5",
      "created_at": "2020-04-24T19:19:45.000Z",
      "updated_at": "2020-04-24T19:19:45.000Z",
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
      "pickup_window": "2020-04-24T17:19:45.000Z/2020-04-24T18:19:45.000Z",
      "pickup_type": null,
      "push_token": null,
      "tag_ids": [

      ]
    }
  ],
  "pages": {
    "current": 1,
    "count": 1,
    "per": 50
  }
}
```

### <span id="get-a-list-of-all-orders-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/orders \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```

## <span id="update-an-order">Update An Order</span>

```http
PUT /api/v1/orders/1
```

### <span id="update-an-order-response">Response</span>

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
    "redemption_url": "https://flybuy.radiusnetworks.com/m/o?r=TFPQUVAXA5",
    "id": 1,
    "arrived_at": null,
    "customer_state": "created",
    "eta_at": null,
    "partner_identifier": null,
    "state": "created",
    "redemption_code": "TFPQUVAXA5",
    "created_at": "2020-04-24T19:19:45.000Z",
    "updated_at": "2020-04-24T19:19:45.000Z",
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
    "pickup_window": "2020-04-24T17:19:45.000Z/2020-04-24T18:19:45.000Z",
    "pickup_type": null,
    "push_token": null,
    "tag_ids": [

    ]
  },
  "included": [

  ]
}
```

### <span id="update-an-order-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/orders/1 \
  -is \
  -X PUT \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"' \
  -d '{
    "data": {
      "site_id": 1,
      "pickup_window": "2020-04-24T17:19:45.000Z/2020-04-24T18:19:45.000Z"
    }
  }'
```
