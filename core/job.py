# Instance of tasks
class Job:
    def __init__(self, name: str, state: int, type: int, act_time: int, deadline: int, instance_num: int, wcet: int) -> None:
        self.name = name + ' - ' + str(instance_num)
        self.state = state
        self.type = type
        self.act_time = act_time # clock time
        self.Deadline = act_time + deadline # real deadline in clock
        self.instance_num = instance_num # add one when one is created!
        self.wcet = wcet