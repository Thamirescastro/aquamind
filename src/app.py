from flask import Flask
from src.api import buscar_clima
from src.hidratacao import calcular_agua

app = Flask(__name__)


@app.route("/")
def home():
    cidade = "Brasilia"

    clima = buscar_clima(cidade)

    if clima is None:
        return "Erro ao buscar clima!"

    temperatura = clima["temperatura"]
    recomendacao = calcular_agua(temperatura)

    return f"""
    <h1>AquaMind 🌿</h1>
    <p><strong>Cidade:</strong> {clima['cidade']}</p>
    <p><strong>Temperatura:</strong> {temperatura}°C</p>
    <p><strong>Clima:</strong> {clima['descricao']}</p>
    <p><strong>Recomendação:</strong> {recomendacao} litros/dia</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)