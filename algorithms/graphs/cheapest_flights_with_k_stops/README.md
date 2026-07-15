# Cheapest Flights Within K Stops

You are given n cities, numbered from 0 to n−1 connected by several flights. You are also given an array flights, where
each flight is represented as `flights[i]=[fromi ,toi, pricei]` meaning there is a direct flight from city 
`fromᵢ` to city `toᵢ` with a cost of `priceᵢ`.

You are also given three integers:

- src: The starting city.
- dst: The destination city.
- k: The maximum number of stops allowed on the route (i.e., intermediate cities between src and dst).

Your task is to find the minimum possible cost to travel from src to dst using at most k stops (i.e., the route may
contain up to k + 1 flights). If there is no valid route from src to dst that uses at most k stops, return −1.

## Constraints

- 2 <= n <= 100
- 0 <= flights.length <= (n * (n - 1) / 2)
- flights[i].length == 3
- 0 <= `fromi`, `toi` < n
- `fromi` != `toi`
- 1 <= `pricei` <= 10^4
- There will not be any multiple flights between two cities.
- 0 <= src, dst, k < n
- src != dst

## Examples

Example 1
```text
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
```

Example 2
```text
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
```

Example 3
```text
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
```

## Topics

- Dynamic Programming
- Depth-First Search
- Breadth-First Search
- Graph Theory
- Heap (Priority Queue)
- Shortest Path

## Solution

The core intuition behind this solution is to treat the problem as a shortest path in a directed, weighted graph with a
strict limit on the number of edges (flights), i.e., we are only allowed to use at most k stops, meaning at most k + 1
flights (edges). Traditional algorithms, such as Standard Dijkstra with a single dist[node], doesn’t enforce the stop
bound because they always choose the globally cheapest path so far, even if that path exceeds the allowed number of stops.
To correctly enforce the stop limit, we employ a Bellman–Ford–style dynamic programming approach, which naturally handles
constraints on the number of edges in a path.

The idea is to repeatedly relax all flights, exactly k + 1 times, where iteration t represents allowing routes that use
up to t flights (one more than the previous iteration). After each iteration, we have the cheapest costs using at most r
flights (edges).

To achieve this, we maintain two arrays: `prices`, which stores the best costs found using up to t − 1 flights, and 
`temp_prices`, which stores the best costs for the current iteration t. During iteration t, every update to a path is
made only from values in `prices`, not from updates made earlier in the same iteration. This separation ensures that any
path discovered in iteration t uses at most one more flight than the paths from the previous iteration t − 1, preventing
us from accidentally chaining multiple flights in the same round.

The algorithm builds valid paths layer by layer, only extending shorter paths into longer ones, guaranteeing that when
all k + 1 iterations are done, we have explored all possible routes that use at most k stops. And the cheapest such route
will be stored in prices[dst].

Using the intuition above, we implement the algorithm as follows:

1. Create an array `prices` of length n and initialize all its entries to infinity.
2. Set `prices[src] = 0` because the cost to reach the starting city from itself is 0 and requires no flights.
3. Iterate at most `k + 1` times to model the flight limit:
   - Initialize a new array, `temp_prices`, with a copy of the dist array. Copying ensures we can also keep the best
     older answers (using fewer flights) instead of forcing exactly t flights.
   - For each flight:
     - If `prices[u]` is not equal to infinity, and the candidate cost: `prices[u] + w` is less than the current
       `temp_prices[v]`:
       - Set `temp_prices[v]` to `prices[u] + w`.
   - After processing all flights in this iteration, set `prices` to `temp_prices`.
4. After completing all `k + 1` iterations, check `prices[dst]`. If `prices[dst]` is still inf, it means there is no
   valid route from `src` to `dst` that uses at most `k` stops, so we return -1. Otherwise, return `prices[dst]`.

### Time Complexity

The time complexity of this algorithm is O((k+1)×m) because we perform k+1 relaxation rounds, and in each round, we
iterate over all m flights once. Asymptotically, this simplifies to O(k×m).

### Space Complexity

The space complexity of this algorithm is O(n) because we maintain two arrays, dist and new_dist, each of size n (the
number of cities). These arrays are reused across iterations, and no other auxiliary data structure grows with the input
size.
