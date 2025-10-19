import requests

BASE_URL = "https://rxnav.nlm.nih.gov/REST"

def get_rxcui(drug_name):
    try:
        url = f"{BASE_URL}/rxcui.json?name={drug_name}"
        print(f"Fetching URL: {url}")  
        response = requests.get(url, timeout=10)
        print(f"Status code: {response.status_code}")

        if response.status_code != 200:
            print(f"Non-200 response: {response.text}")
            return None


        try:
            data = response.json()
        except ValueError:
            print(f"Non-JSON response: {response.text[:200]}")
            return None

        return data.get("idGroup", {}).get("rxnormId", [None])[0]

    except requests.exceptions.RequestException as e:
        print(f"Network error fetching RxCUI: {e}")
        return None

def check_drug_interactions(rxcui_list):
    rxcuis = ",".join(rxcui_list)
    url = f"{BASE_URL}/interaction/list.json?rxcuis={rxcuis}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch interaction data"}
