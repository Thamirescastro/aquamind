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