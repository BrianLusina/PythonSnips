from typing import List
from bisect import bisect_right


def job_scheduling(
    start_time: List[int], end_time: List[int], profit: List[int]
) -> int:
    # Combine the start and end times for jobs to their profits and sort them by the end time in ascending order.
    # This will incur a time complexity cost of O(n log(n)) due to sorting and space complexity of O(n) due to the use
    # of the jobs array to store the jobs
    jobs = sorted(zip(start_time, end_time, profit), key=lambda x: x[1])
    job_len = len(jobs)
    dp = [0] * (job_len + 1)

    for i in range(1, job_len + 1):
        start, end, profit = jobs[i - 1]
        # find number of jobs to finish before start of current job
        num_jobs = bisect_right([job[1] for job in jobs], start)

        dp[i] = max(dp[i - 1], dp[num_jobs] + profit)

    return dp[-1]
