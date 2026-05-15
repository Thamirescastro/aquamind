from flask import Flask, render_template, request
from src.api import buscar_clima
from src.hidratacao import calcular_agua

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None
    erro = None

    if request.method == "POST":
        cidade = request.form.get("cidade")

        if cidade:
            clima = buscar_clima(cidade)

            if clima:
                recomendacao = calcular_agua(clima["temperatura"])
                resultado = {
                    "cidade": clima["cidade"],
                    "temperatura": clima["temperatura"],
                    "descricao": clima["descricao"],
                    "agua": recomendacao,
                }
            else:
                erro = "Não consegui buscar o clima dessa cidade. Tente novamente."

    return render_template("index.html", resultado=resultado, erro=erro)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)