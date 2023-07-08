# Abstract class for my schedulers

from taskset import TaskSet
from job import Job

class Scheduler:
    def __init__(self) -> None:
        pass

    def schedule(taskset: TaskSet, cpu_time: int) -> Job:
        pass
