import webbrowser
from msal import ConfidentialClientApplication, PublicClientApplication

app_id = 'ide az id'
SCOPES = ['User.Read']

client = PublicClientApplication(client_id=app_id)

flow = client.initiate_device_flow(scopes=SCOPES)
print('user code: '+ flow['user_code'])
webbrowser.open(flow['verification_uri'])

token_response = client.acquire_token_by_device_flow(flow)
print(token_response['access_token'])