# Abstract class for my schedulers

from core.taskset import TaskSet
from core.job import Job

class Scheduler:
    def __init__(self) -> None:
        self.last_executing_job : Job = None
        self.abort_on_miss : bool = False

    def schedule(taskset: TaskSet, cpu_time: int) -> Job:
        pass

    def set_abortion_mode(self, value: bool):
        self.abort_on_miss = value
