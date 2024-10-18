from plasgate.rest import Client

account_sid = "PLASGATE_PRIVATE_KEY_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "PLASGATE_SECRET_KEY_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+855972432661", from_="PlasGate", body="Hello from Python!"
)
