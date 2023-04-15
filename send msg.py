import time
from twilio.rest import Client

account_sid = 'ACd582ecd9d81545b2009458be31e2c7fe'
auth_token = 'a904656802b5006347745b8d597208be'
client = Client(account_sid, auth_token)

def sendmessage():
    message = client.messages.create(
    from_='+18333051470',
    body='orospucocu what picture',
    to='+15162509707'
)

for i in range(10):
    sendmessage()
    time.sleep(5)
