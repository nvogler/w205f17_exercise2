import tweepy

consumer_key = "Ri50XuGGtjLVsBP1EI8fER5Xh";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "GTGS9NZYBrE6qAf3UXEsDnr3joINoV4tzdZV9Add2SzL6tQkTD";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "934876405313175559-JTWHtME2SlFWHEC1W3auuovuFlTx00t";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "uyLILWftou4EDQIBJ4GzcJeIhRVcyukqTAKwGndhGaxZO";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



