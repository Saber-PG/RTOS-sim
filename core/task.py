# Save task information here

# Task states
READY = 0
RUNNING = 1
SUSPEND = 2 # RN I will assume that SUSPEND == BLOCK
COMPLETE = 3 

# TASK types
PERIODIC  = -1
INTERRUPT = -2 # answer instantly (really important)

class Task:
    def __init__(self, name: str, state: int, type: int, act_time: int, deadline: int, period: int, wcet: int) -> None:
        self.name = name
        self.state = state
        self.type = type
        self.act_time = act_time # clock time
        self.deadline = deadline # relative deadline
        self.period = period # clock time
        self.wcet = wcet # worst case execution time in clock time
        self.instance_num = 0 # add one when one is created!

    # an instance of a task
    def create_job(self):
        pass
