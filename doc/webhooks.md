# Webhooks

Use Webhooks to be notified about events that happen in a FlyBuy project. FlyBuy can send webhook events that notify your application any time an event occurs for an order associated with any of your sites.

## When to use Webhooks

Webhooks are useful for consuming customer and order event updates.

You might use webhooks as the basis to:

- Send a push notification alert to a customer-facing application when the customer arrives on site
- Send a push notification alert to a staff-facing application when a customer is 10 minutes out
- Build your own Dashboard in your commerce platform
- Begin staging an order when the customer is nearby
- Begin cooking an order through an integration with the point of sale system

## Setting up Webhooks

You can register a webhook URLs for FlyBuy to notify any time an event happens within a project.

The Webhook data contains all the relevant data about what happened, including the type of event and data associated with that event.

FlyBuy then sends the event, via an HTTP POST request, to the endpoint URL that you have defined in your project's Webhook settings. There is a single webhook that can be configured per project.

Once you have added a webhook, you should test that your endpoint is working properly. Press the **Send** to deliver an example payload to the defined webhook.

### Respond to Webhook Events

To acknowledge receipt of a event, your endpoint must return a 2xx HTTP status code. Acknowledge events prior to any logic that needs to take place to prevent timeouts. Your endpoint is disabled if it fails to acknowledge events over consecutive days.

All response codes outside this range, including 3xx codes, indicate to FlyBuy that you did not receive the event. This does mean that a URL redirection or a “Not Modified” response is treated as a failure. FlyBuy ignores any other information returned in the request headers or request body.

### Example Post

Header

```http
Accept: application/json
Content-Type: application/json
Authorization: Token token="FFCPUG2A"
```

Body

```json
{
  "data": {
    "type": "order",
    "order_id": 187,
    "order_state": "created",
    "redemption_url": "https://flyb.uy/m/o?r=E9CY648TVK",
    "id": 187,
    "arrived_at": "2020-09-03T17:41:28.190Z",
    "customer_state": "waiting",
    "eta_at": "2020-09-03T17:40:22.645Z",
    "partner_identifier": "12345",
    "partner_display_identifier": null,
    "partner_identifier_for_crew": null,
    "partner_identifier_for_customer": null,
    "state": "created",
    "redemption_code": "E9CY648TVK",
    "created_at": "2020-09-03T17:41:17.709Z",
    "updated_at": "2020-09-03T18:12:16.716Z",
    "area_name": "Front",
    "possible_areas": [
      {
        "area_id": 1,
        "area_name": "Front",
        "probability": 0.45
      },
      {
        "area_id": 2,
        "area_name": "Side",
        "probability": 0.01
      }
    ],
    "customer_id": 1,
    "site_id": 1,
    "site_partner_identifier": "123",
    "customer_name": "Brian Johnson",
    "customer_car_type": "Ford Fiesta",
    "customer_car_color": "Red",
    "customer_license_plate": "KLF-9104",
    "customer_rating_value": null,
    "customer_rating_value_string": "",
    "customer_rating_comments": null,
    "pickup_window": null,
    "pickup_type": "curbside",
    "push_token": null,
    "tag_ids": [],
    "event": "order_updated",
    "customer_state_changed": false,
    "state_changed": false
  }
}
```

## Security

### Token

FlyBuy optionally supports the use of an Authorization Token to secure access to your Webhook URL. The Authorization Token can be created or edited through your projects Webhook settings.

### HMAC Signature

There is also an option to have webhooks be signed using an HMAC-SHA256 algorithm by adding an "HMAC Key"
to the webhook configuration. Once the key is added, the `Authorization` header will look like this:

```http
Authorization: Token token="FFCPUG2A" signature="pUPEUsnisEDwc8u5f3oEoSi6dNubKjIxv/QKCwSZhWI="
```

In order to verify the signature, you must first construct the message to be signed. The message is made
up of the `Date` header value and the webhook's HTTP body joined together with a newline character between.
Then you compute the HMAC-SHA256 digest of the message and convert it to the Base64 encoding. This should
match the signature that was given.

Here's some psuedocode demonstrating the process:
```rb
message = [headers['date'], body].join('\n')
expected_signature = Base64(HMAC_SHA256(hmac_key, message))
if signature == expected_signature
  # the webhook is valid!
else
  # invalid signature!
end
```
