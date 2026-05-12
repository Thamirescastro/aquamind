from unittest.mock import patch
from src.api import buscar_clima


@patch("src.api.requests.get")
def test_buscar_clima(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "name": "Brasilia",
        "main": {
            "temp": 28
        },
        "weather": [
            {
                "description": "céu limpo"
            }
        ]
    }

    resultado = buscar_clima("Brasilia")

    assert resultado is not None
    assert resultado["cidade"] == "Brasilia"
    assert resultado["temperatura"] == 28