# Instance of tasks
from core.task import *

class Job:
    def __init__(self, name: str, state: int, type: int, act_time: int, deadline: int, instance_num: int, wcet: int) -> None:
        self.name = name + ' - ' + str(instance_num)
        self.state = state
        self.type = type
        self.act_time = act_time # clock time
        self.Deadline = act_time + deadline # absolute deadline in clock
        self.instance_num = instance_num # add one when one is created!
        self.wcet = wcet # worst case execution time 
        self.uptime = 0 # clocks for this task

    # increase task uptime (executing in cpu)
    def increase_uptime(self):
        if self.wcet >= self.uptime:
            self.state = COMPLETED
            return -2 # task is done
        if self.state != RUNNING:
            return -1
        else:
            self.uptime += 1
        if self.wcet == self.uptime:
            self.state = COMPLETED
        return 1

    def is_done(self):
        if self.state == COMPLETED:
            return True
        return False