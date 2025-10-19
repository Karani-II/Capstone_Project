import requests

BASE_URL = "https://rxnav.nlm.nih.gov/REST"

def get_rxcui(drug_name):
    """Fetch RxCUI (unique ID) for a given drug name."""
    url = f"{BASE_URL}/rxcui.json?name={drug_name}"
    response = requests.get(url)
    data = response.json()
    return data.get("idGroup", {}).get("rxnormId", [None])[0]

def check_drug_interactions(rxcui_list):
    """Check for interactions between multiple RxCUIs."""
    rxcuis = ",".join(rxcui_list)
    url = f"{BASE_URL}/interaction/list.json?rxcuis={rxcuis}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch interaction data"}
