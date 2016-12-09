from twilio.rest import TwilioRestClient

account_sid = "AC5e0687ae0f5f9a9913a4a2de367a126a"  # Your Account SID from www.twilio.com/console
auth_token = "85accf2a31aa1833cba65d27acf2e5f3"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
                                 to="+254723704120",  # Replace with your phone number
                                 from_="+12345678901")  # Replace with your Twilio number

print(message.sid)
