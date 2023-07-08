# Handles my task set information
class TaskSet:
    def __init__(self) -> None:
        self.tasks = list()
        self.executing_jobs = list()

    def update_jobs(self, cpu_time):
        pass
    
    def load_tasks_from_json(self):
        pass