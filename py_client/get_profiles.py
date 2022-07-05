import requests
from pprint import pprint
from getpass import getpass

list_profiles_endpoint = "http://localhost:8000/api/v1/profiles/"
get_token_enpoint = "http://localhost:8000/api-token-auth/"


email = input("Pleas input your email: ")
password = getpass("Your password plss...: ")

auth_data = {"username": email, "password": password}


token = requests.post(get_token_enpoint, data=auth_data)

print(token.status_code)

if token.status_code == 200:

    headers = {"Authorization": f"Token {token.json()['token']}"}

    profiles = requests.get(list_profiles_endpoint, headers=headers)

    pprint(profiles.json())

else:
    print(token.json())
