import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random", verify=False)
        data = response.json()[0]
        print(f'\n"{data["q"]}"\n— {data["a"]}')
    except Exception as e:
        print("Error:", e)

get_quote()
