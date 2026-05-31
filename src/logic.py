class SelfCareManager:
    def __init__(self):
        self.water_ml = 0
        self.water_goal_ml = 2000  # Meta padrão inicial: 2000ml (2L)
        self.tasks = {"Meditar": False, "Alongar": False}

    def add_water(self, amount: int):
        if amount < 0:
            raise ValueError("Quantidade deve ser positiva")
        self.water_ml += amount
        return self.water_ml

    def set_water_goal(self, goal_amount: int):
        if goal_amount <= 0:
            raise ValueError("A meta deve ser maior que zero")
        self.water_goal_ml = goal_amount
        return self.water_goal_ml

    def complete_task(self, task_name: str):
        if task_name in self.tasks:
            self.tasks[task_name] = True
            return True
        return False

    def get_status(self):
        # Calcula a porcentagem do progresso (limitando em 100% no máximo)
        progress_pct = min(100, int((self.water_ml / self.water_goal_ml) * 100)) if self.water_goal_ml > 0 else 0
        
        return {
            "water": self.water_ml,
            "goal": self.water_goal_ml,
            "progress": progress_pct,
            "tasks": self.tasks
        }