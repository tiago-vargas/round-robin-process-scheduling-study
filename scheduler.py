# For type annotations
from process import Process


class RoundRobinScheduler:
    def __init__(self, quantum: int, context_switching_duration: int):
        self.context_switching_duration = context_switching_duration
        self.clock = 0
        self.quantum = quantum
        self.queue: list[Process] = []
        self.current_process: Process = None

    def simulate_scheduling(self):
        self.clock += 5

    def initialize(self):
        self.current_process = self.queue[0]

    def execute_current_process(self):
        self._decrease_process_remaining_duration()
        self.clock += self.quantum

    def _decrease_process_remaining_duration(self):
        current_process = self.current_process
        if current_process.remaining_duration > self.quantum:
            current_process.remaining_duration -= self.quantum
        else:
            current_process.remaining_duration = 0
            current_process.is_finished = True

    def switch_context(self):
        process_just_executed = self.current_process

        self.current_process = self.queue[1]
        self.queue = self.queue[1:] + [process_just_executed]

        self.clock += self.context_switching_duration
