from src.api import buscar_clima
from src.hidratacao import calcular_agua


def main():
    print(" AquaMind Inteligente 🌿 ")

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

entrega-intermediaria
from src.logic import SelfCareManager
from logic import SelfCareManager
main

def main():
    manager = SelfCareManager()
    print("=== AquaMind: Seu Assistente de Autocuidado ===")
    
    while True:
        print(f"\nStatus Atual: {manager.get_status()['water']}ml de água")
        print("1. Adicionar Água (250ml)")
        print("2. Ver Checklist")
        print("3. Sair")
        
        opcao = input("Escolha: ")
        
        if opcao == "1":
            manager.add_water(250)
            print("Água registrada!")
        elif opcao == "2":
            for task, status in manager.tasks.items():
                status_str = "✅" if status else "❌"
                print(f"{status_str} {task}")
        elif opcao == "3":
            break

if __name__ == "__main__":
    main()
