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

    if clima["temperatura"] >= 30:
        print("🔥 Dia quente! Hidrate-se bastante.")
    elif clima["temperatura"] <= 18:
        print("🥶 Mesmo no frio, não esqueça da água!")


if __name__ == "__main__":
    main()