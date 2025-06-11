api='6fbdad1e-04fe-43ce-8625-c69815f175c5'
secret='8fozwteft7'
redirect_uri='https://fessorpro.com/'
state='sunil'


url=f"https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id={api}&redirect_uri={redirect_uri}&state={state}"


print(url)

import webbrowser
import upstox_client

webbrowser.open(url, new=1)
newurl = input("Enter the url: ")

auth_code = newurl[newurl.index('code=')+5:newurl.index('&state')]
print(newurl)
print(auth_code)
auth=auth_code
access_token=0

# create an instance of the API class
api_instance = upstox_client.LoginApi()
api_version = '2.0' # str | API Version Header
code = auth
client_id = api # str |  (optional)
client_secret = secret # str |  (optional)
redirect_uri = redirect_uri # str |  (optional)
grant_type = 'authorization_code' # str |  (optional)


# Get token API
api_response = api_instance.token(api_version, code=code, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, grant_type=grant_type)
print(api_response)
access_token=api_response.access_token



# Print the access token
print('access token:', access_token)
with open(f'access.txt', 'w') as k:
    k.write(access_token)
