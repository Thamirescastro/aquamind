import os
from pathlib import Path

import requests
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    API_KEY = "test_key"


def buscar_clima(cidade):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "cidade": data["name"],
        "temperatura": data["main"]["temp"],
        "descricao": data["weather"][0]["description"],
    }