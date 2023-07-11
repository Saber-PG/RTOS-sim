# Save task information here
from core.job import Job

# Task states
READY = 0
RUNNING = 1
SUSPEND = 2 # RN I will assume that SUSPEND == BLOCK
COMPLETED = 3 

# TASK types
PERIODIC  = -1
INTERRUPT = -2 # answer instantly (really important)

class Task:
    def __init__(self, name: str, state: int, type: int, act_time: int, deadline: int, period: int, wcet: int) -> None:
        self.name = name
        self.state = state
        self.type = type
        self.act_time = act_time # first clock time that our task first instance is created
        self.deadline = deadline # relative deadline
        self.period = period # clock time
        self.wcet = wcet # worst case execution time in clock time
        self.instance_num = 0 # add one when one is created!

    # an instance of a task
    def create_job(self) -> Job:
        if self.state == COMPLETED:
            return None # task is done - no more instance is allowed
        elif self.type != PERIODIC and self.instance_num > 1:
            return None # task is done once - no more instance is allowed
        self.instance_num += 1
        job = Job(self.name, READY, self.type, self.act_time, self.deadline, self.instance_num, self.wcet)
        return job
