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
            total = manager.add_water(1)
            print(f"💧 Copo registrado! Total: {total}")

        elif opcao == "2":
            manager.complete_task("Meditar")
            print("🧘 Meditação concluída!")

        elif opcao == "3":
            manager.complete_task("Alongar")
            print("🤸 Alongamento concluído!")

        elif opcao == "4":
            status = manager.get_status()

            print("\nStatus atual:")
            print(f"Copos de água: {status['water']}")

            print("Tarefas:")
            for tarefa, concluida in status["tasks"].items():
                if concluida:
                    print(f"- {tarefa}: concluída")
                else:
                    print(f"- {tarefa}: pendente")

        elif opcao == "0":
            print("Saindo do AquaMind...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()