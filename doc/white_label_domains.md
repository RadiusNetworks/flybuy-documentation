# White-Label Domains

Creating a white-label domain that points to a branded FlyBuy customer portal only requires a single DNS CNAME record to be set up on your domain. In the DNS settings for your domain (e.g., example.com) add a new CNAME record where the name is the white-label URL you want your customers to use when picking up their curbside orders with FlyBuy (e.g., pickup.example.com). The value of this CNAME record should be whitelabel.flybuypickup.com. After setting this up the CNAME record should look like this:

```
NAME                    TYPE   VALUE
----------------------------------------------------------
pickup.example.com      CNAME  whitelabel.flybuypickup.com
```

Once this is set up, provide us with the name of the CNAME record you created so we can make sure that an SSL cert can be generated for this domain. This domain is also used to configure iOS Universal Links and Android App Links in your mobile apps.
