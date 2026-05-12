import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def buscar_clima(cidade):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "cidade": data["name"],
        "temperatura": data["main"]["temp"],
        "descricao": data["weather"][0]["description"]
    }