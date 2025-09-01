import requests, json, os
from dotenv import load_dotenv

load_dotenv()
CG_API_KEY = os.getenv("CG_API_KEY")

api_url = 'https://dataapi.callgear.com/v2.0'

def start_call():
    request_data = {
        "jsonrpc": "2.0",
        "method": "start.employee_call",
        "id": "req1",
        "params": {
            "access_token": CG_API_KEY,
            "first_call": "employee",
            "virtual_phone_number": "74993720692",
            "direction": "in",
            "contact": "79260000000",
            "employee": {
                "id": 25,
                "phone_number": "79260000001"
            }
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

