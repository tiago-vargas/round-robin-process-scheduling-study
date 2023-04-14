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

    class TestMoreProcess:
        def test_first_process_in_queue_to_be_the_one_to_execute_now(self):
            scheduler = RoundRobinScheduler(quantum=20, context_switching_duration=1)
            process_1 = Process(burst_duration=50)
            process_2 = Process(burst_duration=50)
            scheduler.queue = [process_1, process_2]

            scheduler.initialize()

            assert scheduler.current_process == process_1
