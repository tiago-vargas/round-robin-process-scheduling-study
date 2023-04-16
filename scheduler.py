# For type annotations
from process import Process


class RoundRobinScheduler:
    def __init__(self, quantum: int, context_switch_duration: int):
        self.context_switching_duration = context_switch_duration
        self.clock = 0
        self.quantum = quantum
        self.queue: list[Process] = []

    @property
    def current_process(self):
        return self.queue[0]

    def simulate_scheduling(self):
        self.clock += 5

    def execute_current_process(self):
        self._update_clock()
        self._decrease_process_remaining_duration()

    def _update_clock(self):
        if self.current_process.remaining_duration > self.quantum:
            self.clock += self.quantum
        else:
            self.clock += self.current_process.remaining_duration

    def _decrease_process_remaining_duration(self):
        current_process = self.current_process
        if current_process.remaining_duration > self.quantum:
            current_process.remaining_duration -= self.quantum
        else:
            current_process.remaining_duration = 0
            current_process.is_finished = True

    def switch_context(self):
        process_just_executed = self.current_process
        self.queue = self.queue[1:] + [process_just_executed]
        self.clock += self.context_switching_duration

    def execute_queue_once(self):
        for _ in self.queue:
            self.execute_current_process()
            self.switch_context()

        new_queue = [p for p in self.queue if p.is_finished is False]
        self.queue = new_queue
