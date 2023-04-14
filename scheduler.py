class RoundRobinScheduler:
    def __init__(self, quantum: int, context_switching_duration: int):
        self.clock = 0

    def simulate_scheduling(self):
        self.clock += 5
