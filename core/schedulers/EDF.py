# implementing EDF here

from core.taskset import TaskSet
from core.task import RUNNING, READY
from core.job import Job
from core.schedulers.Scheduler import Scheduler

class EDF(Scheduler):
    def __init__(self) -> None:
        super().__init__()

    def schedule(self, taskset: TaskSet, cpu_time: int) -> Job:
        taskset.update_jobs(cpu_time, self.abort_on_miss)
        self.last_executing_job = None # we need to reset it here - not using this var in its real meaning purpose here
        # decide what task must be done right now!
        # we have to choose earliest absolute deadline first
        # what should we do with missed deadline (abort job or finish it?)
        for item in taskset.executing_jobs:
            job : Job = item
            if job.state != RUNNING and job.state != READY:
                continue
            job.state = READY
            if job.Deadline >= cpu_time and self.abort_on_miss:
                continue # do not think about missed deadlines
            if self.last_executing_job == None:
                self.last_executing_job = job
            elif self.last_executing_job.Deadline > job.Deadline:
                self.last_executing_job = job
            self.last_executing_job.state = RUNNING
            
        return self.last_executing_job
            