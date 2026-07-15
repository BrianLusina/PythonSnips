# Optimize Water Distribution in a Village

There are n houses in a village, and we want to supply water to every house. To do this, we have two options:
1. Build a well directly at a house: The costs for building wells are given in the wells array, where wells[i - 1] 
   represents the cost to build a well at house i (houses are numbered from 1 to n, but the array is 0-indexed).
2. Lay water pipes to connect two houses: Allowing one to receive water from the other. The costs for building these 
   connections are given in the pipes array. Each pipe entry is written as [house1, house2, cost], meaning it costs to
   construct a pipe connecting house1 and house2. The connection is two-way (water can flow in both directions).

In the given data, multiple pipe entries may connect the same pair of houses, but with different costs. Each entry 
represents an available option; you may choose the most cost-effective one.

Your task is to determine the minimum total cost to ensure every house gets access to water, either by building a well
directly at it or connecting it via pipes to another house with access to water.

## Constraints

- 2 <= n <= 10^4
- `wells.length` == n
- 0 <= `wells[i]` <= 10^5
- 1 <= `pipes.length` <= 10^4
- `pipes[j].length` == 3
- 1 <= `house1j`, `house2j` <= n
- 0 <= `costj` <= 10^5
- `house1j` != `house2j`

## Examples

![Example 1](./images/examples/min_cost_to_supply_example_1.png)
![Example 2](./images/examples/min_cost_to_supply_example_2.png)
![Example 3](./images/examples/min_cost_to_supply_example_3.png)
![Example 4](./images/examples/min_cost_to_supply_example_4.png)
![Example 5](./images/examples/min_cost_to_supply_example_5.png)

## Solution

This problem can be viewed as a graph connectivity problem where each house represents a node, edges represent pipes 
between houses, or the option to build a well. We use the Union-Find (Disjoint Set Union) data structure to construct a 
minimal connection network.

We begin with an extra virtual node (node 0), representing a central water source. For every house i, we add an edge 
from the virtual node to that house with a cost equal to wells[i - 1], representing the option of building a well. All 
the original pipe connections are included as regular edges between houses with their given costs.

Next, we sort all these edges (pipes and virtual edges) by cost in ascending order. This enables a greedy approach where
we always consider the cheapest connection available at each step. We initialize each node (including the virtual node)
in its own set using Union-Find. Then, we iterate through the sorted list of edges. For each edge, we check if the two
endpoints belong to different sets (i.e., they are not yet connected). If they are in different sets, we perform a union
operation to connect them and add the edge’s cost to the total cost.

We continue this process until all houses are connected either directly to the water source or indirectly via pipes to
other connected houses. The total cost accumulated during these union operations gives us the minimum cost to supply water
to all houses.

Here’s the step-by-step explanation of the solution:

1. Create a Union-Find (Disjoint Set Union) structure with n + 1 elements.
2. For each house i from 1 to n, add an edge [0, i, wells[i - 1]] to the edges list.
3. Add all entries from pipes to the edges list.
4. Sort the edges list in ascending order by cost.
5. Initialize totalCost = 0.
6. For each edge [house1, house2, cost] in the sorted list:
   - If find(house1) != find(house2):
     - Perform union(house1, house2).
     - Add cost to totalCost.
7. Return totalCost.

Let’s look at the following illustration to get a better understanding of the solution:

![Solution 1](./images/solutions/min_cost_to_supply_solution_1.png)
![Solution 2](./images/solutions/min_cost_to_supply_solution_2.png)
![Solution 3](./images/solutions/min_cost_to_supply_solution_3.png)
![Solution 4](./images/solutions/min_cost_to_supply_solution_4.png)
![Solution 5](./images/solutions/min_cost_to_supply_solution_5.png)
![Solution 6](./images/solutions/min_cost_to_supply_solution_6.png)
![Solution 7](./images/solutions/min_cost_to_supply_solution_7.png)
![Solution 8](./images/solutions/min_cost_to_supply_solution_8.png)
![Solution 9](./images/solutions/min_cost_to_supply_solution_9.png)

### Time Complexity

We process n wells and m pipes, resulting in an total of E=n+m edges.
- Sorting all edges takes O(E logE) time.
- Each find and union operation in Union-Find takes O(α(n)), leading to a total of O(E*α(n)) for all operations.

As α(n) is nearly constant, the dominant term is the sorting step. Therefore, the overall time complexity is O((n+m)*log(n+m)).

### Space Complexity

We use a Union-Find data structure with n+1 elements, requiring O(n) space for the parent array. The edge list contains 
n well edges and m pipe edges, totaling O(n+m) space. Therefore, the overall space complexity is O(n+m).
