A task execution slot is defined by it starting time and end time, given a 2 dimensional array of such task where the 0
index is the task start time and the 1 index is the task end time,

Find the max number of tasks that execucted together (Together here means that they had a time window that all tasks
were still running i.e. between there start and end time)

E.g.

Input: arr = [[5,6], [5,7], [1,3], [4,10]]
Answer: 3

Input: arr = [[1,2], [3,4], [5,6]]
Answer: 1

Input: arr = [[5,6], [5,7], [4,10], [4,10]]
Answer: 4
