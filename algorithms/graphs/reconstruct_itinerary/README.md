# Reconstruct Itinerary

Given a list of airline tickets where tickets[i] = [fromi, toi] represent a departure airport and an arrival airport of
a single flight, reconstruct the itinerary in the correct order and return it.

The person who owns these tickets always starts their journey from "JFK". Therefore, the itinerary must begin with "JFK".
If there are multiple valid itineraries, you should prioritize the one with the smallest lexical order when considering
a single string.

> Lexicographical order is a way of sorting similar to how words are arranged in a dictionary. It compares items 
> character by character, based on their order in the alphabet or numerical value.

- For example, the itinerary ["JFK", "EDU"] has a smaller lexical order than ["JFK", "EDX"].

> Note: You may assume all tickets form at least one valid itinerary. You must use all the tickets exactly once.

## Constraints

- 1 <= `tickets.length` <= 300
- `tickets[i].length` == 2
- `fromi.length` == 3
- `toi.length` == 3
- `fromi` != `toi`
- `fromi` and `toi` consist of upper case English letters

## Examples

![Example 1](./images/examples/reconstruct_itinerary_example_1.png)
![Example 2](./images/examples/reconstruct_itinerary_example_2.png)
![Example 3](./images/examples/reconstruct_itinerary_example_3.png)

## Related Topics

- Depth First Search
- Graph
- Eulerian Circuit

## Solution

The algorithm uses __Hierholzer’s algorithm__ to reconstruct travel itineraries from a list of airline tickets. This 
problem is like finding an __Eulerian path__ but with a fixed starting point, “JFK”. Hierholzer’s algorithm is great for
finding Eulerian paths and cycles, which is why we use it here.

> Hierholzer's algorithm is a method for finding an Eulerian circuit (a cycle that visits every edge exactly once) in a 
> graph. It starts from any vertex and follows edges until it returns to the starting vertex, forming a cycle. If there
> are any unvisited edges, it starts a new cycle from a vertex on the existing cycle that has unvisited edges and merges
> the cycles. The process continues until all edges are visited.

> An Eulerian path is a trail in a graph that visits every edge exactly once. An Eulerian path can exist only if exactly
> zero or two vertices have an odd degree. If there are exactly zero vertices with an odd degree, the path can form a
> circuit (Eulerian circuit), where the starting and ending points are the same. If there are exactly two vertices with
> an odd degree, the path starts at one of these vertices and ends at the other.

The algorithm starts by arranging the destinations in reverse lexicographical order to ensure we always choose the
smallest destination first. It then uses depth-first search (DFS) starting from “JFK” to navigate the flights. As it
explores each flight path, it builds the itinerary by appending each visited airport when there are no more destinations
to visit from that airport. Since the airports are added in reverse order during this process, the final step is to
reverse the list to get the correct itinerary.

The basic algorithm to solve this problem will be:

1. Create a dictionary, `flight_map`, to store the flight information. Each key represents an airport; its corresponding
   value is a list of destinations from that airport.
2. Initialize an empty list, result, to store the reconstructed itinerary.
3. Sort the destinations lexicographically in reverse order to ensure that the smallest destination is chosen first.
4. Perform DFS traversal starting from the airport "JFK".
   - Get the list of destinations for the current airport from flight_map.
   - While there are destinations available:
     - Pop the next_destination from destinations.
     - Recursively explore all available flights starting from the popped next_destination, until all possible flights
       have been considered.
   - Append the current airport to the result list.
5. Return the result list in reverse order to ensure the itinerary starts from the initial airport, "JFK", and proceeds
   through the subsequent airports in the correct order.

Let’s look at the following illustration to get a better understanding of the solution:

![Solution 1](./images/solutions/reconstruct_itinerary_solution_1.png)
![Solution 2](./images/solutions/reconstruct_itinerary_solution_2.png)
![Solution 3](./images/solutions/reconstruct_itinerary_solution_3.png)
![Solution 4](./images/solutions/reconstruct_itinerary_solution_4.png)
![Solution 5](./images/solutions/reconstruct_itinerary_solution_5.png)
![Solution 6](./images/solutions/reconstruct_itinerary_solution_6.png)
![Solution 7](./images/solutions/reconstruct_itinerary_solution_7.png)
![Solution 8](./images/solutions/reconstruct_itinerary_solution_8.png)
![Solution 9](./images/solutions/reconstruct_itinerary_solution_9.png)
![Solution 10](./images/solutions/reconstruct_itinerary_solution_10.png)
![Solution 11](./images/solutions/reconstruct_itinerary_solution_11.png)
![Solution 12](./images/solutions/reconstruct_itinerary_solution_12.png)
![Solution 13](./images/solutions/reconstruct_itinerary_solution_13.png)
![Solution 14](./images/solutions/reconstruct_itinerary_solution_14.png)
![Solution 15](./images/solutions/reconstruct_itinerary_solution_15.png)

### Time Complexity

Each edge (flight) is traversed once during the DFS process in the algorithm, resulting in a complexity proportional to
the number of edges, ∣E∣.
Before DFS, the outgoing edges for each airport must be sorted. The sorting operation’s complexity depends on the input
graph’s structure.
In the worst-case scenario, such as a highly unbalanced graph (e.g., star-shaped), where one airport (e.g., JFK)
dominates the majority of flights, the sorting operation on this airport becomes highly expensive, possibly reaching N log N
complexity where `N = |E|/2` In a more balanced or average scenario, where each airport has a roughly equal number of 
outgoing flights, the sorting operation complexity remains O(N log N) where N represents half of the total number of
edges divided by twice the number of airports O(|E|/2|V|). Thus, the algorithm’s overall complexity is O(|E|log|E/2|),
emphasizing the significance of the sorting operation in determining its performance.

### Space Complexity

The space complexity is O(∣V∣+∣E∣), where ∣V∣ is the number of airports and ∣E∣ is the number of flights.
