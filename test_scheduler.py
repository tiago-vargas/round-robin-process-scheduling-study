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

        def test_switching_context_to_the_next_in_queue(self):
            scheduler = RoundRobinScheduler(quantum=20, context_switching_duration=1)
            process_1 = Process(burst_duration=50)
            process_2 = Process(burst_duration=50)
            scheduler.queue = [process_1, process_2]
            scheduler.initialize()
            scheduler.execute_current_process()  # Executes `process_1`

            scheduler.switch_context()

            assert scheduler.current_process == process_2

        def test_advancing_clock_as_context_switches(self):
            scheduler = RoundRobinScheduler(quantum=20, context_switching_duration=1)
            process_1 = Process(burst_duration=50)
            process_2 = Process(burst_duration=50)
            scheduler.queue = [process_1, process_2]
            scheduler.initialize()
            scheduler.execute_current_process()
            time = scheduler.clock

            scheduler.switch_context()

            assert scheduler.clock == time + scheduler.context_switching_duration

        def test_moving_executed_process_to_the_end_of_the_queue(self):
            scheduler = RoundRobinScheduler(quantum=20, context_switching_duration=1)
            process_1 = Process(burst_duration=50)
            process_2 = Process(burst_duration=50)
            process_3 = Process(burst_duration=50)
            scheduler.queue = [process_1, process_2, process_3]
            scheduler.initialize()
            scheduler.execute_current_process()  # Executes `process_1`

            scheduler.switch_context()

            assert scheduler.queue == [process_2, process_3, process_1]
