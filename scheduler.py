class RoundRobinScheduler:
    def __init__(self, quantum: int, context_switching_duration: int):
        self.clock = 0
        self.queue = None
        self.current_process = None

    def simulate_scheduling(self):
        self.clock += 5

    def initialize(self):
        self.current_process = self.queue[0]

    def execute_current_process(self):
        pass

    def switch_context(self):
        self.current_process = self.queue[1]
