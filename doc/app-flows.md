# App Flows

## Documentation

iOS
- [orders][1]
- [customer][2]
- [universal links][3]

Android
- [orders][3]
- [customer][4]
- [app links][6]

[1]: https://github.com/RadiusNetworks/flybuy-ios/blob/master/doc/orders.md
[2]: https://github.com/RadiusNetworks/flybuy-ios/blob/master/doc/customer.md
[3]: https://github.com/RadiusNetworks/flybuy-ios/blob/master/doc/universal_links.md
[4]: https://github.com/RadiusNetworks/flybuy-android/blob/master/doc/orders.md
[5]: https://github.com/RadiusNetworks/flybuy-android/blob/master/doc/customer.md
[6]: https://github.com/RadiusNetworks/flybuy-android/blob/master/doc/app_links.md

## Main App Flow

1. User receives a text with a redemption link. If you have a white-label domain set up with FlyBuy, see the `iOS Universal Links`/`Android App Links` documentation on how to set up the deep link.

2. Check if the customer is logged in with `Get Current Customer`.

3. Use `Fetch Unclaimed Orders` to get information about the order.

4. Check in your system if a customer API token exists for that customer.
     - If the token does not exist, follow [New Customers](#new-customers).
     - If the token does exist, follow [Existing Customers](#existing-customers).

5. Claim the order with the redemption code using `Claim Orders`. If the customer is not logged in, a headless customer account will be created, and that customer will be automatically logged in.

6. Provide failsafe options for order events. At a minimum, have a prompt for `arrived`. Use `Update Orders` to provide these event updates to FlyBuy. This section also lists the possible state changes.

7. Order history can be shown using `Fetch Claimed Orders`.

### <span id="new-customers">New Customers</span>

1. Prompt the user to provide vehicle information.

2. Create a customer using `Create Customer` with the vehicle attributes. This will return a customer API token and automatically log the user into FlyBuy. Save this token.

3. Ask for location permissions, including the “ask to ask” screen that provides information on why and when location data is used.

### <span id="existing-customers">Existing Customers</span>

1. Log the customer in with a token using `Log In`.

2. If the customer provides updates to vehicle information, use `Update Customer` to update FlyBuy.