from flask import Flask, render_template, request
from src.api import buscar_clima
from src.hidratacao import calcular_agua
from src.logic import SelfCareManager

app = Flask(__name__)

manager = SelfCareManager()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/inicial", methods=["GET", "POST"])
def inicial():
    mensagem = None
    status = manager.get_status()

    if request.method == "POST":
        acao = request.form.get("acao")

        if acao == "agua":
            total = manager.add_water(1)
            mensagem = f"Copo registrado! Total: {total}"

        elif acao == "meditar":
            manager.complete_task("Meditar")
            mensagem = "Meditação concluída!"

        elif acao == "alongar":
            manager.complete_task("Alongar")
            mensagem = "Alongamento concluído!"

        status = manager.get_status()

    return render_template("inicial.html", status=status, mensagem=mensagem)


@app.route("/intermediaria", methods=["GET", "POST"])
def intermediaria():
    resultado = None
    erro = None

    if request.method == "POST":
        cidade = request.form.get("cidade")

        if cidade:
            clima = buscar_clima(cidade)

            if clima:
                agua = calcular_agua(clima["temperatura"])
                resultado = {
                    "cidade": clima["cidade"],
                    "temperatura": clima["temperatura"],
                    "descricao": clima["descricao"],
                    "agua": agua,
                }
            else:
                erro = "Não consegui buscar o clima dessa cidade."

    return render_template(
        "intermediaria.html",
        resultado=resultado,
        erro=erro
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)