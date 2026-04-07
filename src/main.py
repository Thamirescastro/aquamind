from logic import SelfCareManager

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