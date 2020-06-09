# Sites API

- [API Specs](#api-specs)
- [Get A List Of All Sites](#get-a-list-of-all-sites)

The FlyBuy Sites API enables partners to fetch information about sites and associations between FlyBuy site identifiers and partner site identifiers.

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


## <span id="get-a-list-of-all-sites">Get A List Of All Sites</span>

```http
GET /api/v1/sites
```

This returns a paginated response of all sites that the owner of the API key has access to.
This can span multiple projects and sites.

Use the `pages.next` URL provided in the response body for the next page of results.      

### <span id="get-a-list-of-all-sites-parameters">Parameters</span>

Include any desired query parameters.

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `partner_identifier` | `string` | _Optional_. If provided, sites can be fetched with a partner site identifier. In the merchant portal, this is the `Site Number`. |
| `page` | `integer` | _Optional_. Allows retrieving a specific page of the results. Defaults to 1. |
| `per` | `integer` | _Optional_. Specifies how many sites should be included in a page of results. Defaults to 50. Max of 100. |

### <span id="get-a-list-of-all-sites-response">Response</span>

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
      "phone": "+15553678309",
      "operational_status": "live",
      "project_id": 593363181,
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

### <span id="get-a-list-of-all-sites-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/sites \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```
