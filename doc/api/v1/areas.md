# Areas API

- [API Specs](#api-specs)
- [Get A List Of All Areas Under A Site](#get-a-list-of-all-areas-under-a-site)

The FlyBuy Areas API enables partners to fetch information about site pickup areas and associations between FlyBuy pickup area identifiers and site identifiers.

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


## <span id="get-a-list-of-all-areas-under-a-site">Get A List Of All Areas Under A Site</span>

```http
GET /api/v1/sites/1/areas
```

This returns a paginated response of all areas for any site that the owner of the API key has access to.

Use the `pages.next` URL provided in the response body for the next page of results.

Coordinates are in [lng, lat] order.

### <span id="get-a-list-of-all-areas-under-a-site-parameters">Parameters</span>

Include any desired query parameters.

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `site_id` | `integer` | _Required_. Areas can be fetched with a site id. In the merchant portal, this is the `Site Id`. |
| `page` | `integer` | _Optional_. Allows retrieving a specific page of the results. Defaults to 1. |
| `per` | `integer` | _Optional_. Specifies how many sites should be included in a page of results. Defaults to 50. Max of 100. |

### <span id="get-a-list-of-all-areas-under-a-site-response">Response</span>

```http
Status: 200 OK
Content-Type: application/json; charset=utf-8
```
```json
{
  "data": [
    {
      "type": "area",
      "id": 1,
      "site_id": 1,
      "name": "Any Area",
      "color": "#FFCC00",
      "beacon_uuid": null,
      "beacon_major": null,
      "beacon_minor": null,
      "coordinates": [
        [
          -77.06524762003255,
          38.90409207159311
        ],
        [
          -77.06525298445058,
          38.90395952852339
        ],
        [
          -77.0650772997601,
          38.90395431028724
        ],
        [
          -77.06504645435643,
          38.903993968872385
        ],
        [
          -77.06498476354909,
          38.90400336169194
        ],
        [
          -77.06498476354909,
          38.90410772627007
        ],
        [
          -77.06524762003255,
          38.90409207159311
        ]
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

### <span id="get-a-list-of-all-areas-under-a-site-curl-example">Curl Example</span>

```sh
curl https://flybuy.radiusnetworks.com/api/v1/sites/1/areas \
  -is \
  -X GET \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token token="0123456789abcdef"'
```
