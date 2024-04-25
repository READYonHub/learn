import webbrowser
from msal import ConfidentialClientApplication, PublicClientApplication

client_secret = 'titkos code'
app_id = 'ide az id'
SCOPES = ['User.Read']

client = ConfidentialClientApplication(client_id=app_id,client_credential=client_secret)
authorization_url = client.get_authorization_request_url(SCOPES)

print(authorization_url)

webbrowser.open(authorization_url)

authorization_code ='ide a code'
access_token = client.acquire_token_by_authorization_code(code=authorization_code, scopes=SCOPES)
print(access_token)
access_id = access_token['access_token']