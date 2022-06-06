import tweepy
  
consumer_key = "XY9wxt3VBA6XpjH3HAFlEEe5D"
consumer_secret = "Uh1bbVVhSnmzGrUQbsGWzjqHoHfzcR5zsWgZ3EMTTDKMxshdbC"
access_token = "1225331522720288768-1Wud8hB6gboTla5PsssiwiQ0YBERU4"
access_token_secret = "iQHzvlRfNYgQfqSd5q9yjVQYTNeWwkYe9lrx178rw5lhU"
  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
auth.set_access_token(access_token, access_token_secret)
  
api = tweepy.API(auth)
  
recipient_id =1225331522720288768

text = "Emergency"
  
direct_message = api.send_direct_message(recipient_id, text)
  
# printing the text of the sent direct message
print(direct_message.message_create['message_data']['text'])