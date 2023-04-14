from scheduler import RoundRobinScheduler
from process import Process


class TestRoundRobinScheduler:
    class TestWithOnlyOneProcess:
        class TestProcessEndingInSingleQuantum:
            def test_clock_advancing(self):
                scheduler = RoundRobinScheduler(quantum=20, context_switching_duration=1)
                process = Process(burst_duration=5)
                scheduler.queue = [process]

                scheduler.simulate_scheduling()

                assert scheduler.clock == 5
