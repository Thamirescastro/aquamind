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

class SelfCareManager:
    def __init__(self):
        self.water_cups = 0
        self.tasks = {
            "meditação": False,
            "alongamento": False,
        }

    def add_water(self):
        self.water_cups += 1
        return self.water_cups

    def complete_task(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name] = True
            return True
        return False

    def get_status(self):
        return {
            "copos_agua": self.water_cups,
            "tarefas": self.tasks,
        }
main
