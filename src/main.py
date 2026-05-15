from src.api import buscar_clima
from src.hidratacao import calcular_agua


def main():
    print("=== AquaMind Inteligente 🌿 ===")

    cidade = input("Digite sua cidade: ")

    clima = buscar_clima(cidade)

    if not clima:
        print("Erro ao buscar clima!")
        return

    agua = calcular_agua(clima["temperatura"])

    print(f"\n📍 Cidade: {clima['cidade']}")
    print(f"🌡️ Temperatura: {clima['temperatura']}°C")
    print(f"☁️ Clima: {clima['descricao']}")
    print(f"\n💧 Recomendação de água: {agua} litros/dia")


if __name__ == "__main__":
    main()