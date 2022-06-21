# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC331ccd98e15725baae87a2efa3a39ab5'
auth_token = 'f22a0fc87e8ec3a689e84ffe996ad0a4'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="파이썬 개꿀잼?",
                     from_='+12408984967',
                     to='+821051310355'
                 )

print(message.sid)