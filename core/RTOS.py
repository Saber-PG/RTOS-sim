# Core of my RTOS code
# we manage cpu here

from core.taskset import TaskSet
from core.job import Job
from core.schedulers.Scheduler import Scheduler

class RTOS:
    def __init__(self, taskSet: TaskSet, scheduler: Scheduler) -> None:
        self.cpu_clock : int = 0
        self.taskSet : TaskSet = taskSet
        self.scheduler : Scheduler = scheduler
        self.executing_job : Job = None 

    # my RTOS runs - cpu is clocking
    def run(self):
        while True:
            # decide what to do
            self.executing_job = self.scheduler.schedule(self.taskSet)
            # we do something in one clock
            if self.executing_job != None:
                self.executing_job.increase_uptime()
            # go to next clock 
            self.cpu_clock += 1
