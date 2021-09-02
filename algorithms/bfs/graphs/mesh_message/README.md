## MeshMessage (Mesh Network)

Instead of routing texts through cell towers, your app sends messages via the phones of nearby users, passing each
message along from one phone to the next until it reaches the intended recipient. (Don't worry—the messages are
encrypted while they're in transit.)

Some friends have been using your service, and they're complaining that it takes a long time for messages to get
delivered. After some preliminary debugging, you suspect messages might not be taking the most direct route from the
sender to the recipient.

Given information about active users on the network, find the shortest route for a message from one user (the sender) to
another (the recipient). Return a list of users that make up this route.

There might be a few shortest delivery routes, all with the same length. For now, let's just return any shortest route.

Your network information takes the form of a dictionary mapping username strings to a list of other users nearby:

network = {
'Min'     : ['William', 'Jayden', 'Omar'],
'William' : ['Min', 'Noam'],
'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
'Ren'     : ['Jayden', 'Omar'],
'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'], ... }

For the network above, a message from Jayden to Adam should have this route:

['Jayden', 'Amelia', 'Adam']

Gotchas We can find the shortest route in O(N+M) time, where N is the number of users and M is the number of connections
between them.

It's easy to write code that can get caught in an infinite loop for some inputs!

What happens if there's no way for messages to get to the recipient?

What happens if the sender tries to send a message to themselves?

### Breakdown

Users? Connections? Routes? What data structures can we build out of that? Let's run through some common ones and see if
anything fits here.

Lists? Nope—those are a bit too simple to express our network of users. Dictionaries? Maybeee. Graphs? Yeah, that seems
like it could work!
Let's run with graphs for a bit and see how things go. Users will be nodes in our graph, and we'll draw edges between
users who are close enough to message each other.

Our input dictionary already represents the graph we want in adjacency list format. Each key in the dictionary is a
node, and the associated value—a list of connected nodes—is an adjacency list.

> Adjacency list
> In this format, every node has a list of connected neighbors: an adjacency list. We could store these lists in a dictionary where the keys represent the node and the values are the adjacency lists.
> For instance, here's one graph:
> ![adjacency_list](https://www.interviewcake.com/images/svgs/graph_coloring__example_graph.svg?bust=155)
> And, here's how we'd represent it using a dictionary:
graph = { 0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2], } Since node 3 has edges to nodes 1 and 2, graph[3] has the adjacency list [1, 2].

Each key in the dictionary is a node, and the associated value—a list of connected nodes—is an adjacency list.

Is our graph directed or undirected? ↴ Weighted or unweighted? ↴

> Directed and undirected graphs
> Graphs can be directed or undirected. In directed graphs, edges point from the node at one end to the node at the other end. In undirected graphs, the edges simply connect the nodes at each end.
> ![](https://www.interviewcake.com/images/svgs/graph_coloring__undirected_and_directed_graphs.svg?bust=155)

> Weighted or unweighted
> if a graph is weighted, each edge has a "weight." The weights could, for example, represent the distance between two locations, or the cost or time it takes to travel between the locations.
> ![](https://www.interviewcake.com/images/svgs/graph_coloring__weighted_graph.svg?bust=155)

For directed vs. undirected, we'll assume that if Min can transmit a message to Jayden, then Jayden can also transmit a
message to Min. Our sample input definitely suggests this is the case. And it makes sense—they're the same distance from
each other, after all. That means our graph is undirected.

What about weighted? We're not given any information suggesting that some transmissions are more expensive than others,
so let's say our graph is unweighted.

These assumptions seem pretty reasonable, so we'll go with them here. But, this is a great place to step back and check
in with your interviewer to make sure they agree with what you've decided so far.

Here's what our user network looks like as a graph:

![network](https://www.interviewcake.com/images/svgs/mesh_message__example_graph.svg?bust=155)

An unweighted graph of a user network for our messaging app. Each node is labeled with a name and connected to at least
one other node. Okay, how do we start looking around our graph to find the shortest route from one user to another?

Or, more generally, how do we find the shortest path from a start node to an end node in an unweighted, undirected
graph?

There are two common ways to explore undirected graphs: depth-first search (DFS) ↴ and breadth-first search (BFS). ↴

> Depth-first search (DFS) is a method for exploring a tree or graph. In a DFS, you go as deep as possible down one path before backing up and trying a different one.
> Depth-first search is like walking through a corn maze. You explore one path, hit a dead end, and go back and try a different one.
> Here's a how a DFS would traverse this tree, starting with the root:
> ![](https://www.interviewcake.com/images/svgs/depth_first_search_root.svg?bust=155)
> We'd go down the first path we find until we hit a dead end:
> ![](https://www.interviewcake.com/images/svgs/depth_first_search_dead_end_one.svg?bust=155)
> Then we do the same thing again: head down the next leftmost path until we reach a dead end.
> And again:
> ![](https://www.interviewcake.com/images/svgs/depth_first_search_dead_end_two.svg?bust=155)
> And again.
> ![](https://www.interviewcake.com/images/svgs/depth_first_search_dead_end_four.svg?bust=155)
> Until we've visited every node in the tree.
> Depth-first search is often compared with breadth-first search.
> Advantages:
> Depth-first search on a binary tree generally requires less memory than breadth-first.
> Depth-first search can be easily implemented with recursion.
>
> Disadvantages
> A DFS doesn't necessarily find the shortest path to a node, while breadth-first search does.


> Breadth-first search (BFS) is a method for exploring a tree or graph. In a BFS, you first explore all the nodes one step away, then all the nodes two steps away, etc.
> Breadth-first search is like throwing a stone in the center of a pond. The nodes you explore "ripple out" from the starting point.
> Here's a how a BFS would traverse this tree, starting with the root:
> ![](https://www.interviewcake.com/images/svgs/breadth_first_search_root.svg?bust=155)
> We'd visit all the immediate children (all the nodes that're one step away from our starting node):
> ![](https://www.interviewcake.com/images/svgs/breadth_first_search_first_level.svg?bust=155)
> Then we'd move on to all those nodes' children (all the nodes that're two steps away from our starting node):
> ![](https://www.interviewcake.com/images/svgs/breadth_first_search_second_level.svg?bust=155)
> And so on:
> ![](https://www.interviewcake.com/images/svgs/breadth_first_search_third_level.svg?bust=155)
> Breadth-first search is often compared with depth-first search.
> Advantages:
> A BFS will find the shortest path between the starting point and any other reachable node. A depth-first search will not necessarily find the shortest path.
> Disadvantages
> A BFS on a binary tree generally requires more memory than a DFS.

Which do we want here?

Since we're interested in finding the shortest path, BFS is the way to go.

Remember: both BFS and DFS will eventually find a path if one exists. The difference between the two is:
BFS always finds the shortest path. DFS usually uses less space.

Okay, so let's do a breadth-first search of our graph starting from the sender and stopping when we find the recipient.
Since we're using breadth-first search, we know that the first time we see the recipient, we'll have traveled to them
along the shortest path.

To code this up, let's start with a standard implementation of breadth-first search:

It's a good idea to know breadth-first and depth-first search well enough to quickly write them out. They show up in a
lot of graph problems.

### Complexity

Our solution has two main steps. First, we do a breadth-first search of the user network starting from the sender. Then,
we use the results of our search to backtrack and find the shortest path.

How much work is a breadth-first search?

In the worst case, we'll go through the BFS loop once for every node in the graph, since we only ever add each node to
nodes_to_visit once (we check how_we_reached_nodes to see if we've already added a node before). Each loop iteration
involves a constant amount of work to dequeue the node and check if it's our end node. If we have nn nodes, then this
portion of the loop is O(N).

But there's more to each loop iteration: we also look at the current node's neighbors. Over all of the nodes in the
graph, checking the neighbors is O(M), since it involves crossing each edge twice: once for each node at either end.

Putting this together, the complexity of the breadth-first search is O(N+M).

BFS and DFS are common enough that it's often acceptable to just state their complexity as O(N+M). Some interviewers
might want you to derive it though, so definitely be ready in case they ask.

What about backtracking to determine the shortest path? Handling each node in the path is O(1), and we could have at
most NN nodes in our shortest path. So, that's O(N) for building up the path. Then, it's another O(N) to reverse it. So,
the total time complexity of our backtracking step is O(N).

Putting these together, the time complexity of our entire algorithm is O(N+M)

What about space complexity? The queue of nodes to visit, the mapping of nodes to previous nodes, and the final path ...
they all store a constant amount of information per node. So, each data structure could take up to O(N) space if it
stored information about all of our nodes. That means our overall space complexity is O(N).

Our app's design has a formal name: a mesh network. In a mesh network, data is sent from one node (here, a phone) to
another directly, rather than through intermediate devices (here, cell towers). Assuming enough devices are in range,
mesh networks provide multiple possible transmission paths, making them reliable even if some devices have failed.

