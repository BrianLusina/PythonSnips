# Minimum Cost to Hire K Workers

There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker
and wage[i] is the minimum wage expectation for the ith worker.

We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the
following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions.
Answers within 10-5 of the actual answer will be accepted.

```plain
Example 1:

Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0th worker and 35 to 2nd worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667
Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.
```

## Related Topics

- Array
- Greedy
- Sorting
- Heap(Priority Queue)

## Solution

This solution uses the top k elements pattern, commonly used when selecting the top k items based on a certain criterion.
Here, we need to form a group of exactly k workers and minimize the total cost while ensuring fair payments based on the
workers’ wage expectations and quality. Below are some key observations that will help us to solve the problem:

1. **Proportionality condition**: All workers in the group must be paid proportionally to their quality. If one worker’s
   quality is twice that of another, they must be paid twice as much.
2. **Wage-to-quality ratio**: For each worker, we calculate a ratio that indicates how much we need to pay per unit of
   quality. This ratio is defined as: `ratio[i] = wage[i]/quality[i]`
3. **Greedy approach:** To minimize the total wage, we process workers based on their wage-to-quality ratios in ascending
   order. Once we select k workers, we fix the highest wage-to-quality ratio among them. All workers are paid according
   to this ratio, ensuring proportionality.
4. **Optimization using a heap**: We can use a max heap to efficiently manage the total quality of selected workers. This
   allows us to keep track of the workers with the smallest total quality, which is important for minimizing the total
   wage. The max heap allows us to quickly access the largest quality (at the top of the heap) and remove it in constant
   time, ensuring that only k workers remain.

The steps of the algorithm are as below:

1. Creates a list of tuple workers for each worker. Sort these tuples based on the ratios in ascending order to process
   workers with the lowest ratio first. Each tuple contains:
   - The worker’s wage-to-quality ratio (w/q)
   - The worker’s quality (q)
2. Create a max heap `heap` to store the qualities of the selected workers.
3. Initialize the below variables:
   - A variable total_quality is used to track the total quality of the workers in the heap
   - A variable min_cost to store the minimum cost encountered during the process
4. Iterate through the sorted list of workers based on their ratios. For each worker:
   - Add their quality (as a negative value to simulate max heap behavior) to the heap.
   - Update the total_quality by adding the current worker’s quality.
5. After adding a worker, check if the heap contains more than k workers. If so, remove the worker with the highest
   quality (i.e., the smallest negative value) to minimize the total quality used in cost calculations.
6. Once the heap contains exactly k workers, compute the cost of hiring them. This is done by multiplying the highest
   wage-to-quality ratio (of the current worker) by the total_quality of the selected group. Update the min_cost if the
   current one is lower than the previously recorded minimum.
7. After processing all workers, return the min_cost calculated.

### Time Complexity

Sorting the workers takes `O(nlog(n))` time, and maintaining the heap takes `O(klog(k))` time where n is the total number
of elements in workers and k is the number of workers we want to hire. Hence, the overall time complexity is `O(nlog(n))`

### Space Complexity

We use additional space for the list of all workers (`O(n)`) and for the heap, which contains at most k workers (`O(k)`).
Since `k≤n`, the overall space complexity is `O(n)`.
