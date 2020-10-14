# Customers API

- [Get Customer Details](#get-customer-details)
- [List The Customers](#list-the-customers)
- [Create A Customer](#create-a-customer)
- [Update A Customer](#update-a-customer)

The FlyBuy Customers API enables partners to create, update, and list customers

## <span id="get-customer-details">Get Customer Details</span>

```http
GET /api/v1/customers/1
```

### <span id="get-customer-details-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "data": {
    "id": 1,
    "api_token": "FraqWCqZNwYdQeUb1dZg1Cpj",
    "car_color": "white",
    "car_type": "sedan",
    "license_plate": "ABC-123",
    "name": "John Doe",
    "phone": "555-555-5555",
    "partner_identifier": "98765",
    "created_at": "2020-04-24T19:19:45.000Z",
    "updated_at": "2020-04-24T19:19:45.000Z"
  }
}
```

### <span id="get-customer-details-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/customers/1 \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```

## <span id="list-the-customers">List The Customers</span>

```http
GET /api/v1/customers
```

### <span id="list-the-customers-parameters">Parameters</span>



| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `partner_identifier` | `string` | _Optional._ If given, the API returns only customers with a `partner_identifier` that matches the provided value. |
| `page` | `integer` | _Optional._ Allows retrieving a specific page of the results. Defaults to 1. |
| `per` | `integer` | _Optional._ Specifies how many customers should be included in a page of results. Defaults to 50. |

### <span id="list-the-customers-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "data": [
    {
      "id": 1,
      "api_token": "FraqWCqZNwYdQeUb1dZg1Cpj",
      "car_color": "white",
      "car_type": "sedan",
      "license_plate": "ABC-123",
      "name": "John Doe",
      "phone": "555-555-5555",
      "partner_identifier": "98765",
      "created_at": "2020-04-24T19:19:45.000Z",
      "updated_at": "2020-04-24T19:19:45.000Z"
    },
    {
      "id": 2,
      "api_token": "re7RryjRoH5Wyebcr99n9oQZ",
      "car_color": "blue",
      "car_type": "SUV",
      "license_plate": "ABC-123",
      "name": "Jane Doe",
      "phone": "555-555-4444",
      "partner_identifier": "CUSTOMER2",
      "created_at": "2020-04-24T19:19:45.000Z",
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

### <span id="list-the-customers-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/customers \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```

## <span id="create-a-customer">Create A Customer</span>

```http
POST /api/v1/customers
```

### <span id="create-a-customer-parameters">Parameters</span>

When creating and updating customers, the body payload should be a JSON object. All items must be sent under a top-level `data` object. 

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `name` | `string` | **Required.** The customer's name |
| `phone` | `string` | The customer's phone number |
| `car_color` | `string` | The color of the customer's car. |
| `car_type` | `string` | A type or model of car |
| `license_plate` | `string` | license plate |
| `partner_identifier` | `string` | an identifier that can be used to lookup a customer later |
| `terms_of_service` | `boolean` | **Required.** Set to true to indicate the customer agrees to the TOS |
| `age_verification` | `boolean` | **Required.** Set to true to indicate the customer's age has been verified |

### <span id="create-a-customer-example">Example</span>

```json
{
  "data": {
    "name": "John Doe",
    "phone": "555-555-5555",
    "car_color": "white",
    "car_type": "sedan",
    "license_plate": "ABC-123",
    "partner_identifier": "98765",
    "terms_of_service": true,
    "age_verification": true
  }
}
```

### <span id="create-a-customer-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "data": {
    "id": 1,
    "api_token": "FraqWCqZNwYdQeUb1dZg1Cpj",
    "car_color": "white",
    "car_type": "sedan",
    "license_plate": "ABC-123",
    "name": "John Doe",
    "phone": "555-555-5555",
    "partner_identifier": "98765",
    "created_at": "2020-04-24T19:19:45.000Z",
    "updated_at": "2020-04-24T19:19:45.000Z"
  }
}
```

### <span id="create-a-customer-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/customers \
  -is \
  -X POST \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"' \
  -d '{
    "data": {
      "name": "John Doe",
      "phone": "555-555-5555",
      "car_color": "white",
      "car_type": "sedan",
      "license_plate": "ABC-123",
      "partner_identifier": "98765",
      "terms_of_service": true,
      "age_verification": true
    }
  }'
```

## <span id="update-a-customer">Update A Customer</span>

```http
PUT /api/v1/customers/1
```

### <span id="update-a-customer-parameters">Parameters</span>

When creating and updating customers, the body payload should be a JSON object. All items must be sent under a top-level `data` object. 

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `name` | `string` | The customer's name |
| `phone` | `string` | The customer's phone number |
| `car_color` | `string` | The color of the customer's car. |
| `car_type` | `string` | A type or model of car |
| `license_plate` | `string` | license plate |
| `partner_identifier` | `string` | an identifier that can be used to lookup a customer later |

### <span id="update-a-customer-example">Example</span>

```json
{
  "data": {
    "name": "John A. Doe",
    "phone": "555-555-5555",
    "car_color": "silver",
    "car_type": "truck"
  }
}
```

### <span id="update-a-customer-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "data": {
    "id": 1,
    "api_token": "FraqWCqZNwYdQeUb1dZg1Cpj",
    "car_color": "silver",
    "car_type": "truck",
    "license_plate": "ABC-123",
    "name": "John A. Doe",
    "phone": "555-555-5555",
    "partner_identifier": "98765",
    "created_at": "2020-04-24T19:19:45.000Z",
    "updated_at": "2020-04-24T19:19:45.000Z"
  }
}
```

### <span id="update-a-customer-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/customers/1 \
  -is \
  -X PUT \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"' \
  -d '{
    "data": {
      "name": "John A. Doe",
      "phone": "555-555-5555",
      "car_color": "silver",
      "car_type": "truck"
    }
  }'
```
