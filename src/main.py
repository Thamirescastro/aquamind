from src.api import buscar_clima
from src.hidratacao import calcular_agua


def main():
    print("=== AquaMind Inteligente 🌿 ===")

    cidade = input("Digite sua cidade: ")

    clima = buscar_clima(cidade)

    if clima is None:
        print("Erro ao buscar clima!")
        return

    temperatura = clima["temperatura"]
    recomendacao = calcular_agua(temperatura)

    print(f"\n📍 Cidade: {clima['cidade']}")
    print(f"🌡️ Temperatura: {temperatura}°C")
    print(f"☁️ Clima: {clima['descricao']}")
    print(f"\n💧 Recomendação de água: {recomendacao} litros/dia")


if __name__ == "__main__":
    main()