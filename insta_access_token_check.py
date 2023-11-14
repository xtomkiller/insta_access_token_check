import requests

def check_access_token_validity(access_token):
    base_url = 'https://graph.instagram.com/v12.0/me'  # Adjust the URL based on the API version and endpoint

    params = {
        'access_token': access_token,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        print("Access token is valid.")
    else:
        print("Access token is not valid.")

# Replace 'your_access_token_here' with the actual access token you want to check

token = input("Enter tour access token : ")
check_access_token_validity(token)
