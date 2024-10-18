from plasgate.rest import Client

private = "PLASGATE_PRIVATE_KEY_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
secret = "PLASGATE_SECRET_KEY_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = Client(private, secret)

test = client.messages.create(
    to="855972432661",
    sender="PlasGate",
    content="TestAPI",
    dlr="yes",
    dlr_url="https://webhook-test.com/273e777973dc8334bbaa2ef63f3d9cf6",
)
