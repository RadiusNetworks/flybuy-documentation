# Orders API

- [Getting An Order](#getting-an-order)
- [Creating A Redeemable Order](#creating-a-redeemable-order)
- [Creating An Order For A Customer](#creating-an-order-for-a-customer)
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

```
GET /api/v1/orders/1
```

### Response <a href="#getting-an-order-response" class="header-link"></a>

```
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
    "redemption_code": "WSNF3H",
    "created_at": "2019-03-19T00:53:40.171Z",
    "updated_at": "2019-03-19T00:53:40.171Z",
    "area_name": null,
    "customer_id": null,
    "site_id": 1,
    "site_partner_identifier": null,
    "customer_name": null,
    "customer_car_type": null,
    "customer_car_color": null,
    "customer_license_plate": null,
    "pickup_window": "2019-03-18T22:53:40.099Z/2019-03-18T23:53:40.099Z"
  },
  "included": [
    {
      "type": "site",
      "id": 1,
      "name": "A Site",
      "full_address": "123 Any Street, Any Locality, Any Region, 12345",
      "street_address": "123 Any Street",
      "locality": "Any Locality",
      "region": "Any Region",
      "country": "Any Country",
      "latitude": "0.0",
      "longitude": "0.0"
    }
  ]
}
```

### Curl Example <a href="#getting-an-order-curl-example" class="header-link"></a>

```
curl http://www.example.com/api/v1/orders/1?include=site \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"'
```

## <span id="creating-a-redeemable-order">Creating A Redeemable Order</span>

```
POST /api/v1/orders
```

Create an order

### Response <a href="#creating-a-redeemable-order-response" class="header-link"></a>

```
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
    "partner_identifier": null,
    "state": "created",
    "redemption_code": "GCJMCZ",
    "created_at": "2019-03-19T00:53:40.485Z",
    "updated_at": "2019-03-19T00:53:40.485Z",
    "area_name": null,
    "customer_id": null,
    "site_id": 1,
    "site_partner_identifier": null,
    "customer_name": null,
    "customer_car_type": null,
    "customer_car_color": null,
    "customer_license_plate": null,
    "pickup_window": null
  },
  "included": [

  ]
}
```

### Curl Example <a href="#creating-a-redeemable-order-curl-example" class="header-link"></a>

```
curl http://www.example.com/api/v1/orders \
  -is \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"' \
  -d '{
    "data": {
      "site_id": 1
    }
  }'
```

## <span id="creating-an-order-for-a-customer">Creating An Order For A Customer</span>

```
POST /api/v1/orders
```

### Response <a href="#creating-an-order-for-a-customer-response" class="header-link"></a>

```
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
    "partner_identifier": null,
    "state": "created",
    "redemption_code": null,
    "created_at": "2019-03-19T00:53:40.749Z",
    "updated_at": "2019-03-19T00:53:40.749Z",
    "area_name": null,
    "customer_id": 1,
    "site_id": 1,
    "site_partner_identifier": null,
    "customer_name": "Any Customer",
    "customer_car_type": "Sedan",
    "customer_car_color": "Blue",
    "customer_license_plate": "ABC-123",
    "pickup_window": null
  },
  "included": [

  ]
}
```

### Curl Example <a href="#creating-an-order-for-a-customer-curl-example" class="header-link"></a>

```
curl http://www.example.com/api/v1/orders \
  -is \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"' \
  -d '{
    "data": {
      "site_id": 1,
      "customer_token": "K1S8gV8fkXp4iTAumXAGivF5"
    }
  }'
```

## <span id="updating-an-order">Updating An Order</span>

```
PUT /api/v1/orders/1
```

### Response <a href="#updating-an-order-response" class="header-link"></a>

```
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
    "redemption_code": "5WXCLQ",
    "created_at": "2019-03-19T00:53:40.902Z",
    "updated_at": "2019-03-19T00:53:40.929Z",
    "area_name": null,
    "customer_id": null,
    "site_id": 1,
    "site_partner_identifier": null,
    "customer_name": null,
    "customer_car_type": null,
    "customer_car_color": null,
    "customer_license_plate": null,
    "pickup_window": "2019-03-18T22:53:40.866Z/2019-03-18T23:53:40.866Z"
  },
  "included": [

  ]
}
```

### Curl Example <a href="#updating-an-order-curl-example" class="header-link"></a>

```
curl http://www.example.com/api/v1/orders/1 \
  -is \
  -X PUT \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token="0123456789abcdef"' \
  -d '{
    "data": {
      "site_id": 1,
      "pickup_window": "2019-03-18T22:53:40.866Z/2019-03-18T23:53:40.866Z"
    }
  }'
```
