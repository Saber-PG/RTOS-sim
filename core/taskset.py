# Handles my task set information
import json
from core.task import Task

class TaskSet:
    def __init__(self) -> None:
        self.tasks: list = list()
        self.executing_jobs: list = list()

    # check if new job created!
    # remove done jobs
    # abort on miss if abortion is allowed!
    def update_jobs(self, cpu_time: int, abort_on_miss: bool):
        for task in self.tasks:
            if (cpu_time - task.act_time)/task.period == 0:
                new_job = task.create_job()
                if new_job != None:
                    self.executing_jobs.append(new_job)
        new_executing_jobs = []
        for job in self.executing_jobs:
            if not job.is_done():
                if job.Deadline >= cpu_time and abort_on_miss:
                    continue
                new_executing_jobs.append(job)
        self.executing_jobs = new_executing_jobs

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