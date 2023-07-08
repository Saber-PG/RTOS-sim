# Core of my RTOS code
# we manage cpu here

from taskset import TaskSet

class RTOS:
    def __init__(self, taskSet: TaskSet) -> None:
        self.cpu_clock = 0
        self.taskSet = taskSet

    # my RTOS runs - cpu is clocking
    def run(self):
        while True:
            # we do something in one clock

            # go to next clock 
            self.cpu_clock += 1
