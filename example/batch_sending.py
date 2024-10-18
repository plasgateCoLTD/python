from plasgate.rest import Client

private = "PLASGATE_PRIVATE_KEY_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
secret = "PLASGATE_SECRET_KEY_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = Client(private, secret, batch_sending=True)

test = client.messages.create(
    messages=[
        {"to": ["85581848677", "855972432661"], "content": "Test plasgate client"}
    ],
    globals={
        "sender": "PlasGate",
        "dlr": "yes",
        "dlr_level": 3,
        "dlr_url": "webhook-test.com/273e777973dc8334bbaa2ef63f3d9cf6",
    },
)
