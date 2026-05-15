from src.logic import SelfCareManager


def main():
    manager = SelfCareManager()

    while True:
        print("\n=== AquaMind 💧 - Entrega Inicial ===")
        print("1. Registrar copo de água")
        print("2. Concluir meditação")
        print("3. Concluir alongamento")
        print("4. Ver status")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            total = manager.add_water()
            print(f"💧 Copo registrado! Total: {total}")

        elif opcao == "2":
            manager.complete_task("meditação")
            print("🧘 Meditação concluída!")

        elif opcao == "3":
            manager.complete_task("alongamento")
            print("🤸 Alongamento concluído!")

        elif opcao == "4":
            status = manager.get_status()
            print(f"Copos de água: {status['copos_agua']}")
            print(f"Tarefas: {status['tarefas']}")

        elif opcao == "0":
            print("Saindo do AquaMind...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()