import heapq
import math

def solution(jobs):
    job_index = 0

    job_list = [
        (request, duration, idx)
        for idx, (request, duration) in enumerate(jobs)
    ]

    job_list.sort(key=lambda x: x[0])

    current_time = 0
    heap = []
    return_times = [0] * len(jobs)

    while job_index < len(jobs) or heap:
        while (
            job_index < len(jobs)
            and job_list[job_index][0] <= current_time
        ):
            request, duration, idx = job_list[job_index]

            heapq.heappush(
                heap,
                (duration, request, idx)
            )

            job_index += 1

        if heap:
            duration, request, idx = heapq.heappop(heap)

            current_time += duration
            return_times[idx] = current_time - request

        else:
            current_time = job_list[job_index][0]

    return math.floor(
        sum(return_times) / len(jobs)
    )