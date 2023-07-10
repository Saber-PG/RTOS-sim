from core.RTOS import RTOS
from core.taskset import TaskSet
from core.schedulers.EDF import EDF
# Launch application in this file

# Defaults:
DEBUG = False
SCHEDULER = 'EDF'
TASKSET = 'taskset1'

# build and attack main program modules
edf = EDF()
ts = TaskSet()
ts.load_tasks_from_json(TASKSET)
rtos = RTOS(ts, edf)
