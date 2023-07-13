# Core of my RTOS code
# we manage cpu here

from core.taskset import TaskSet
from core.job import Job
from core.schedulers.Scheduler import Scheduler

class RTOS:
    def __init__(self, taskSet: TaskSet, scheduler: Scheduler, duration: int) -> None:
        self.cpu_clock : int = 0
        self.taskSet : TaskSet = taskSet
        self.scheduler : Scheduler = scheduler
        self.executing_job : Job = None 
        if duration < 100:
            self.duration = 100
        else:
            self.duration = duration

    # my RTOS runs - cpu is clocking
    def run(self):
        while self.duration >= self.cpu_clock:
            # print("cpu clock: {}".format(self.cpu_clock))
            # decide what to do
            self.executing_job: Job = self.scheduler.schedule(self.taskSet, self.cpu_clock)
            # we do something in one clock
            if self.executing_job != None:
                self.executing_job.increase_uptime()
                # print("CPU CLOCK: {} - with Job: {}".format(self.cpu_clock, self.executing_job.name))
            # go to next clock 
            self.cpu_clock += 1
