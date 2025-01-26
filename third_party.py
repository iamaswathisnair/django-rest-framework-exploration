import requests

def check_api_status(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print("API is working correctly!")
            print("Response Data:", response.json())  # you make a request to an API and get back a JSON response ,and convert that JSON data from the response into Python objects
        else:
            print(f"API returned an error. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Error while checking the API:", e)

# Replace with your actual API URL
api_url = "http://127.0.0.1:8000/all_student/"
check_api_status(api_url)