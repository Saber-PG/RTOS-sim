# Handles my task set information
import json

class TaskSet:
    def __init__(self) -> None:
        self.tasks = list()
        self.executing_jobs = list()

    def update_jobs(self, cpu_time):
        pass

    def load_tasks_from_json(self, name: str) -> int:
        try:
            with open("tasks/" + name + ".json", "r") as json_raw_data:
                json_data = json.load(json_raw_data)
                self.tasks = json_data['tasks']
                print(self.tasks)
                return 0 # success
        except:
            self.tasks = list()
            return -1