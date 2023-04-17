from scheduler import RoundRobinScheduler
from process import Process


class TestRoundRobinScheduler:
    class TestWithOnlyOneProcess:
        # def test_not_switching_context_with_single_process(self):
        #     scheduler = RoundRobinScheduler(quantum=20, context_switch_duration=1)
        #     process = Process(burst_duration=40)
        #     scheduler.queue = [process]

        #     # scheduler.execute_current_process()
        #     scheduler.execute_queue_once()

        #     assert scheduler.clock == 20 + 20

        class TestProcessEndingInSingleQuantum:
            def test_clock_advancing(self):
                scheduler = RoundRobinScheduler(quantum=20, context_switch_duration=1)
                process = Process(burst_duration=5)
                scheduler.queue = [process]

                scheduler.simulate_scheduling()

                assert scheduler.clock == 5

    class TestMoreProcess:
        def test_first_process_in_queue_to_be_the_one_to_execute_now(self):
            scheduler = RoundRobinScheduler(quantum=20, context_switch_duration=1)
            process_1 = Process(burst_duration=50)
            dummy_process = Process(burst_duration=50)

            scheduler.queue = [process_1, dummy_process]

            assert scheduler.current_process == process_1

        def test_switching_context_to_the_next_in_queue(self):
            scheduler = RoundRobinScheduler(quantum=20, context_switch_duration=1)
            process_1 = Process(burst_duration=50)
            process_2 = Process(burst_duration=50)
            scheduler.queue = [process_1, process_2]
            scheduler.execute_current_process()  # Executes `process_1`

            scheduler.switch_context()

            assert scheduler.current_process == process_2

        def test_moving_executed_process_to_the_end_of_the_queue(self):
            scheduler = RoundRobinScheduler(quantum=20, context_switch_duration=1)
            process_1 = Process(burst_duration=50)
            process_2 = Process(burst_duration=50)
            process_3 = Process(burst_duration=50)
            scheduler.queue = [process_1, process_2, process_3]
            scheduler.execute_current_process()  # Executes `process_1`

            scheduler.switch_context()

            assert scheduler.queue == [process_2, process_3, process_1]

        def test_advancing_clock_as_context_switches(self):
            scheduler = RoundRobinScheduler(quantum=20, context_switch_duration=1)
            process_1 = Process(burst_duration=50)
            dummy_process = Process(burst_duration=50)
            scheduler.queue = [process_1, dummy_process]
            scheduler.execute_current_process()
            time = scheduler.clock

            scheduler.switch_context()

            assert scheduler.clock == time + scheduler.context_switching_duration

        def test_switching_context_sooner_as_process_finishes_before_its_quantum_ends(self):
            scheduler = RoundRobinScheduler(quantum=20, context_switch_duration=1)
            process_1 = Process(burst_duration=7)
            dummy_process = Process(burst_duration=50)
            scheduler.queue = [process_1, dummy_process]
            scheduler.execute_current_process()  # Executes `process_1`, which finishes

            scheduler.switch_context()

            assert scheduler.clock == 7 + scheduler.context_switching_duration

        def test_removing_completed_processes_from_queue_after_a_cycling_it(self):
            scheduler = RoundRobinScheduler(quantum=20, context_switch_duration=1)
            process_1 = Process(burst_duration=50)
            process_2 = Process(burst_duration=2)
            process_3 = Process(burst_duration=50)
            scheduler.queue = [process_1, process_2, process_3]
            # [process_1, process_2, process_3, ]

            scheduler.execute_queue_once()

            assert scheduler.queue == [process_1, process_3]

        # def test_not_switching_context_after_executing_last_process(self):
        #     scheduler = RoundRobinScheduler(quantum=20, context_switch_duration=1)
        #     process_1 = Process(burst_duration=50)
        #     dummy_process = Process(burst_duration=30)
        #     scheduler.queue = [process_1, dummy_process]

        #     scheduler.execute_queue_once()

        #     assert scheduler.clock == 20 + 1 + 20

    class TestTrackingProcessProgress:
        def test_decreasing_process_completion_time_as_it_executes(self):
            scheduler = RoundRobinScheduler(quantum=20, context_switch_duration=1)
            process_1 = Process(burst_duration=50)
            dummy_process = Process(burst_duration=50)
            scheduler.queue = [process_1, dummy_process]

            scheduler.execute_current_process()  # Executes `process_1`

            assert process_1.remaining_duration == 50 - 20

        def test_remaining_duration_being_less_than_quantum(self):
            scheduler = RoundRobinScheduler(quantum=20, context_switch_duration=1)
            process_1 = Process(burst_duration=5)
            dummy_process = Process(burst_duration=50)
            scheduler.queue = [process_1, dummy_process]

            scheduler.execute_current_process()  # Executes `process_1` completely

            assert process_1.remaining_duration == 0

        def test_marking_process_as_finished(self):
            scheduler = RoundRobinScheduler(quantum=20, context_switch_duration=1)
            process = Process(burst_duration=20)
            scheduler.queue = [process]

            scheduler.execute_current_process()  # Executes `process` completely

            assert process.is_finished is True
