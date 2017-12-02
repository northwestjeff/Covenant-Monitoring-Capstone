from quickbooks import Oauth2SessionManager

client_id = "Q0AaC7Zk5JlBRJqGjBkLthuJ7RV8Jpdg8xab0vtviZAYJWF16g"
client_secret = "s5I3D2Wn22tsbcXcUwkdrVV5d1LGcH7bTimWD6Bb"

session_manager = Oauth2SessionManager(
    sandbox=True,
    client_id=client_id,
    client_secret=client_secret,
    base_url='http://localhost:8001'
)

callback_url = 'http://localhost:8000'
authorize_url = client.get_authorization_url(callback_url)
request_token = client.request_token
request_token_secret = client.request_token_secret
