class SelfCareManager:
    def __init__(self):
        self.water_ml = 0
        self.tasks = {"Meditar": False, "Alongar": False}

    def add_water(self, amount: int):
        if amount < 0:
            raise ValueError("Quantidade deve ser positiva")
        self.water_ml += amount
        return self.water_ml

    def complete_task(self, task_name: str):
        if task_name in self.tasks:
            self.tasks[task_name] = True
            return True
        return False

    def get_status(self):
        return {"water": self.water_ml, "tasks": self.tasks}