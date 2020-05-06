# Sites API

- [API Specs](#api-specs)
- [Getting A List Of All Sites](#getting-a-list-of-all-sites)
- [Getting Sites With A Given Partner Identifier](#getting-sites-with-a-given-partner-identifier)

The FlyBuy Sites API enables partners to fetch information about sites.

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


## <span id="getting-a-list-of-all-sites">Getting A List Of All Sites</span>

```http
GET /api/v1/sites
```

This returns a paginated response of all sites, across all projects, accessible
by the account associated with the API key authorizing the request.

### <span id="getting-a-list-of-all-sites-parameters">Parameters</span>



| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `partner_identifier` | `string` | _Optional_. If given, the API returns only sites with a partner_identifier that matches the provided value. |
| `page` | `integer` | _Optional_. Allows retrieving a specific page of the results. Defaults to 1. |
| `per` | `integer` | _Optional_. Specifies how many sites should be included in a page of results. Defaults to 50. |

### <span id="getting-a-list-of-all-sites-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "data": [
    {
      "type": "site",
      "id": 1,
      "partner_identifier": "12345",
      "name": "A Site",
      "full_address": "123 Any Street, Any Locality, Any Region, 12345",
      "timezone": null,
      "latitude": "0.0",
      "longitude": "0.0",
      "instructions": null,
      "description": null,
      "phone": "555-367-8309",
      "project_id": 593363184,
      "project_name": "Any Project"
    }
  ],
  "pages": {
    "current": 1,
    "count": 1,
    "per": 50
  }
}
```

### <span id="getting-a-list-of-all-sites-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/sites \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```

## <span id="getting-sites-with-a-given-partner-identifier">Getting Sites With A Given Partner Identifier</span>

```http
GET /api/v1/sites?partner_identifier=12345
```

Sites can be fetched with a partner site identifier (12345 in the example above).
This value can be optionally passed in as partner_identifier.

FlyBuy does not guarantee uniqueness for a partner site identifier.
For a unique identifier, use the FlyBuy site identifier (site_id) instead.

### <span id="getting-sites-with-a-given-partner-identifier-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "data": [
    {
      "type": "site",
      "id": 1,
      "partner_identifier": "12345",
      "name": "A Site",
      "full_address": "123 Any Street, Any Locality, Any Region, 12345",
      "timezone": null,
      "latitude": "0.0",
      "longitude": "0.0",
      "instructions": null,
      "description": null,
      "phone": "555-367-8309",
      "project_id": 593363185,
      "project_name": "Any Project"
    }
  ],
  "pages": {
    "current": 1,
    "count": 1,
    "per": 50
  }
}
```

### <span id="getting-sites-with-a-given-partner-identifier-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/sites?partner_identifier=12345 \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```
