class Process:
    pid = 1

    def __init__(self, burst_duration: int):
        self.pid = Process.pid
        Process.pid += 1
        self.remaining_duration = burst_duration
        # For the notebook
        self.burst_duration = burst_duration

    @property
    def is_finished(self):
        return self.remaining_duration == 0

    def __repr__(self):
        return f'Process #{self.pid}'
