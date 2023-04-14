class Process:
    pid = 1

    def __init__(self, burst_duration: int):
        self.pid = Process.pid
        Process.pid += 1
        self.is_finished = False
        self.remaining_duration = burst_duration

    def __repr__(self):
        return f'Process #{self.pid}'
