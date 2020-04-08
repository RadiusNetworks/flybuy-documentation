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
    "id": 187,
    "arrived_at": null,
    "customer_state": "nearby",
    "eta_at": "2019-02-26T17:15:33.645Z",
    "partner_identifier": "24667",
    "state": "completed",
    "redemption_code": "NNSE9J",
    "created_at": "2019-02-26T17:14:50.941Z",
    "updated_at": "2019-02-26T17:55:20.442Z",
    "area_name": null,
    "customer_id": 135,
    "site_id": 43,
    "site_partner_identifier": "",
    "customer_name": "Brian Johnson",
    "customer_car_type": "Ford Fiesta",
    "customer_car_color": "Red",
    "customer_license_plate": "KLW-9104",
    "pickup_window": null,
    "customer_state_changed": false,
    "state_changed": false
  }
}
```

## Security

FlyBuy optionally supports the use of an Authorization Token to secure access to your Webhook URL. The Authorization Token can be created or edited through your projects Webhook settings.
