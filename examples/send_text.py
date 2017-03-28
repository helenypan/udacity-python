from twilio import rest

# Your account Sid and Auth Token from twilio.com/user/account

account_sid = ""
auth_token = ""
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
	body = "My name is helen",
	to = "your phone number here",
	from = "your Twilio number here")
print message.sid
