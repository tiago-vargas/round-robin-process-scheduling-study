from copy import copy

quanta = 3
context_switch_time = 1

cpu_scheduling = []
scheduling_starts = []
scheduling_ends = []

colors = []

finalized_processes = []


def scheduler(process_list):
    ready_queue = process_list.copy()
    timeline = 0

    while not is_queue_empty(ready_queue):
        head_process = ready_queue[0]

        scheduling_starts.append(timeline)

        save_process_state_in_scheduling(head_process)

        ready_queue.remove(head_process)
        if head_process.burst_time > quanta:
            head_process.burst_time -= quanta
            ready_queue.append(head_process)
            timeline += quanta
            scheduling_ends.append(timeline)
        elif head_process.burst_time <= quanta:
            timeline += head_process.burst_time
            head_process.burst_time = 0
            scheduling_ends.append(timeline)

            finalized_processes.append((str(head_process), timeline))

        timeline += context_switch_time

    set_all_times(process_list)


def throughput(timelimit):
    thr_list = []
    for tuple in finalized_processes:
        finalization_time = tuple[1]
        if finalization_time > timelimit: break
        thr_list.append(tuple)
    return thr_list

def is_queue_empty(ready_queue):
    return True if len(ready_queue) == 0 else False


def save_process_state_in_scheduling(process):
    actual_state = copy(process)
    cpu_scheduling.append(actual_state)
    colors.append(process.color)


def last_process_occurrence_in_scheduling(pid):
    for i in reversed(range(len(cpu_scheduling))):
        if cpu_scheduling[i].pid == pid:
            return i


def first_process_occurrence_in_scheduling(pid):
    for i in range(len(cpu_scheduling)):
        if cpu_scheduling[i].pid == pid:
            return i


def set_all_times(process_list):
    completion_times(process_list)
    waiting_times(process_list)
    response_times(process_list)
    return_times(process_list)


def completion_times(process_list):
    for process in process_list:
        i = last_process_occurrence_in_scheduling(process.pid)
        ct = scheduling_ends[i]
        process.set_completion_time(ct)
        process.set_turnaround_time(tt=ct)


def waiting_times(process_list):
    for process in process_list:
        wt = process.turnaround_time - process.initial_burst_time
        process.set_waiting_time(wt)


def response_times(process_list):
    for process in process_list:
        i = first_process_occurrence_in_scheduling(process.pid)
        rt = scheduling_starts[i]
        process.set_response_time(rt)


def return_times(process_list):
    for process in process_list:
        rt = process.completion_time - process.response_time
        process.set_return_time(rt)
