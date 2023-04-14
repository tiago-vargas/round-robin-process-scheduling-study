class Process:
    def __init__(self, burst_duration: int):
        self.is_finished = False
        self.remaining_duration = burst_duration
