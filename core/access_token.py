import requests
from requests.auth import HTTPBasicAuth
import keys

def generate_token():

    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    response = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    
    json_response = response.json()
    my_access_token = json_response['access_token']

    access_token = my_access_token

    return access_token
