import requests, json, os
from dotenv import load_dotenv

load_dotenv()
CG_API_KEY = os.getenv("CG_API_KEY")

api_url = 'https://dataapi.callgear.com/v2.0'

def get_virtual_numbers():
    request_data = {
        "jsonrpc":"2.0",
        "id":"1",
        "method":"get.virtual_numbers",   
        "params":{
            "access_token": CG_API_KEY
        }
    }

    try:
        response = requests.post(api_url, json=request_data)
        print("Status Code:", response.status_code)
        response.raise_for_status()
        data = response.json()
        print("Response JSON:", json.dumps(data, indent=2))
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return False


    except Exception as e:
        print(e)
        return False



if __name__ == "__main__":
    get_virtual_numbers()

