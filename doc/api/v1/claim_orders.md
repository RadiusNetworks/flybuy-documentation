# Claim Orders API

- [Get Order Details Using A Claim Code](#get-order-details-using-a-claim-code)
- [Claim An Order Using A Claim Code](#claim-an-order-using-a-claim-code)

The FlyBuy Orders API enables partners to claim orders using a known customer id associated with the order's project.

Must Do's:
- To claim an order for a customer, an order and a customer must be created at minimum under the same project.

## <span id="get-order-details-using-a-claim-code">Get Order Details Using A Claim Code</span>

```http
GET /api/v1/claim_orders/TFPQUVAXA5
```

### <span id="get-order-details-using-a-claim-code-response">Response</span>

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
    "partner_display_identifier": null,
    "partner_identifier_for_crew": null,
    "partner_identifier_for_customer": null,
    "state": "created",
    "redemption_code": "TFPQUVAXA5",
    "created_at": "2020-04-24T19:19:45.000Z",
    "updated_at": "2020-04-24T19:19:45.000Z",
    "area_name": null,
    "possible_areas": null,
    "customer_id": null,
    "site_id": 1,
    "site_partner_identifier": null,
    "customer_name": null,
    "customer_car_type": null,
    "customer_car_color": null,
    "customer_license_plate": null,
    "customer_rating_value": null,
    "customer_rating_value_string": "",
    "customer_rating_comments": null,
    "pickup_window": null,
    "pickup_type": null,
    "push_token": null,
    "tag_ids": [

    ]
  }
}
```

### <span id="get-order-details-using-a-claim-code-curl-example">Curl Example</span>

```sh
curl http://www.example.com/api/v1/claim_orders/TFPQUVAXA5 \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```

## <span id="claim-an-order-using-a-claim-code">Claim An Order Using A Claim Code</span>

```http
PUT /api/v1/claim_orders/TFPQUVAXA5
```

### <span id="claim-an-order-using-a-claim-code-parameters">Parameters</span>

The body payload should be a JSON object. All items must be sent under a top-level `data` parameter.

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `customer_id` | `integer` | **Required.** The customer's id to associate with the order. |
| `customer_car_color` | `string` | The color of the customer's car. |
| `customer_car_type` | `string` | A type or model of car. |
| `customer_license_plate` | `string` | The customer's license plate. |
| `customer_name` | `string` | The customer's name. |
| `customer_phone` | `string` | The customer's phone number. |
| `partner_identifier` | `string` | An identifier that can be used to lookup an order later. |
| `pickup_type` | `string` | The order's pickup type. |
| `app_authorization_token` | `string` | _Optional._ If given an app authorization token, FlyBuy will automatically associate the order with the app which will allow it to send push notifications about this order to the app. |
| `push_token` | `string` | _Optional._ A token used to send push notifications to the user's mobile device. |

### <span id="claim-an-order-using-a-claim-code-example">Example</span>

```json
{
  "data": {
    "customer_id": 1
  }
}
```

### <span id="claim-an-order-using-a-claim-code-response">Response</span>

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
    "partner_display_identifier": null,
    "partner_identifier_for_crew": null,
    "partner_identifier_for_customer": null,
    "state": "created",
    "redemption_code": "TFPQUVAXA5",
    "created_at": "2020-04-24T19:19:45.000Z",
    "updated_at": "2020-04-24T19:19:45.000Z",
    "area_name": null,
    "possible_areas": null,
    "customer_id": 1,
    "site_id": 1,
    "site_partner_identifier": null,
    "customer_name": "Any Customer",
    "customer_car_type": "Sedan",
    "customer_car_color": "Blue",
    "customer_license_plate": "ABC-123",
    "customer_rating_value": null,
    "customer_rating_value_string": "",
    "customer_rating_comments": null,
    "pickup_window": null,
    "pickup_type": null,
    "push_token": null,
    "tag_ids": [

    ]
  }
}
```

### <span id="claim-an-order-using-a-claim-code-curl-example">Curl Example</span>

```sh
curl http://www.example.com/api/v1/claim_orders/TFPQUVAXA5 \
  -is \
  -X PUT \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"' \
  -d '{
    "data": {
      "customer_id": 1
    }
  }'
```
