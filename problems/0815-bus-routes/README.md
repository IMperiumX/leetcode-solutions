```python
# 815. Bus Routes - BFS Approach
from collections import deque, defaultdict

def numBusesToDestination(routes: list[list[int]], source: int, target: int) -> int:
    """
    Calculates the minimum number of buses needed to travel from source to target.
    """
    if source == target:
        return 0

    # Create a graph where keys are bus stops and values are lists of bus routes that stop there.
    stop_to_routes = defaultdict(list)
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].append(i)  # i is the bus route index

    queue = deque()
    visited_stops = set()
    visited_routes = set()

    # Initialize the queue with all routes that stop at the source
    for route_index in stop_to_routes[source]:
        queue.append((route_index, 1))  # (route_index, num_buses)
        visited_routes.add(route_index)
    visited_stops.add(source)


    while queue:
        route_index, num_buses = queue.popleft()

        # Iterate through the stops on the current route
        for stop in routes[route_index]:
            if stop == target:
                return num_buses
            if stop not in visited_stops:
                visited_stops.add(stop)
            # Add all routes that stop at this 'stop' to the queue (if not visited)
            for next_route_index in stop_to_routes[stop]:
                if next_route_index not in visited_routes:
                    visited_routes.add(next_route_index)
                    queue.append((next_route_index, num_buses + 1))

    return -1  # Target not reachable
```

```markdown
# 815. Bus Routes, Difficulty: Hard

## Problem Description

You are given an array `routes` representing bus routes where `routes[i]` is a bus route that the ith bus repeats forever.

For example, if `routes[0] = [1, 5, 7]`, this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop `source` (You are not on any bus initially), and you want to go to the bus stop `target`. You can travel between bus stops by buses only.

Return the *least number of buses* you must take to travel from `source` to `target`. Return `-1` if it is not possible.

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106

## Approach(es)

### Breadth-First Search (BFS)

Algorithm:

1.  **Build a Graph:**
    *   Create a graph `stop_to_routes` where keys are bus stops (integers) and values are lists of bus route indices (integers) that stop at that stop.  This allows us to quickly find all buses that go through a particular stop.

2.  **Initialization:**
    *   If `source == target`, return 0 (already at the destination).
    *   Create a queue `queue` (using `collections.deque` for efficient FIFO operations).
    *   Create a `visited_stops` set to keep track of visited bus stops.
    * Create a `visited_routes` set to keep track of visited bus routes.
    *   Find all bus routes that stop at the `source` stop.  Add these routes to the `queue` as tuples `(route_index, 1)`, where `route_index` is the index of the bus route and `1` represents the initial number of buses taken. Add `source` to `visited_stops` and initial `route_index` to `visited_routes`.

3.  **BFS Traversal:**
    *   While the `queue` is not empty:
        *   Dequeue a `(route_index, num_buses)` pair from the `queue`.
        *   Iterate through all the stops in the current `route` (i.e., `routes[route_index]`):
            *   If the current `stop` is the `target`, return `num_buses`.
            * Add current `stop` to `visited_stops`.
            *   Find all other bus routes (`next_route_index`) that also stop at the current `stop` using the `stop_to_routes` graph.
            *   For each `next_route_index` that hasn't been visited yet:
                *   Add `next_route_index` to `visited_routes`.
                *   Enqueue `(next_route_index, num_buses + 1)` to the `queue`, indicating that we've taken one more bus.

4.  **Not Reachable:** If the queue becomes empty and the target is not found, return `-1`.

Data Structures:

*   Hash Table (Dictionary in Python): `stop_to_routes` (to represent the graph)
*   Queue (Deque in Python): for BFS traversal
*   Set: `visited_stops`, `visited_routes` (to avoid cycles and redundant processing)

Time Complexity:

*   O(R * S + R^2), where R is the number of routes and S is the average number of stops per route.
    *   Building the `stop_to_routes` graph takes O(R * S) time in the worst case (iterating through all routes and stops).
    *  In the worst case, we process each route and for each stop on the route, find other connected routes. So, time complexity is O(R * S + R^2), it can be also written as O(N), where N is the number of nodes in graph (number of bus routes).

Space Complexity:

*   O(R * S + R), where R is the number of bus routes and S is the average number of stops per route
*   `stop_to_routes` can store up to R * S entries.
* The queue and visited sets can, in the worst case, store information related to all stops, leading to a space complexity of O(R * S + R).
* In general, space complexity can be considered as O(N) where N is number of bus routes.

Trade-offs:
* BFS guarantees to find the shortest path.

## Code

```python
from collections import deque, defaultdict

def numBusesToDestination(routes: list[list[int]], source: int, target: int) -> int:
    """
    Calculates the minimum number of buses needed to travel from source to target.
    """
    if source == target:
        return 0

    # Create a graph where keys are bus stops and values are lists of bus routes that stop there.
    stop_to_routes = defaultdict(list)
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].append(i)  # i is the bus route index

    queue = deque()
    visited_stops = set()
    visited_routes = set()

    # Initialize the queue with all routes that stop at the source
    for route_index in stop_to_routes[source]:
        queue.append((route_index, 1))  # (route_index, num_buses)
        visited_routes.add(route_index)
    visited_stops.add(source)


    while queue:
        route_index, num_buses = queue.popleft()

        # Iterate through the stops on the current route
        for stop in routes[route_index]:
            if stop == target:
                return num_buses
            if stop not in visited_stops:
                visited_stops.add(stop)
            # Add all routes that stop at this 'stop' to the queue (if not visited)
            for next_route_index in stop_to_routes[stop]:
                if next_route_index not in visited_routes:
                    visited_routes.add(next_route_index)
                    queue.append((next_route_index, num_buses + 1))

    return -1  # Target not reachable
```

## Notes

* This problem is a classic graph traversal problem, and BFS is the most appropriate algorithm to find the shortest path (minimum number of buses).
* The key to solving this problem efficiently is to build the `stop_to_routes` graph, which allows us to quickly find all buses that serve a particular stop.
* Using sets (`visited_stops`, `visited_routes`) prevents cycles and ensures we don't revisit the same bus stops or routes unnecessarily.
* It is important to understand why we use a queue of *routes*, not a queue of *stops*. We're trying to minimize the number of *buses* (routes), not the number of stops.

```

**Step 5: Topic Extraction and Files**

*Prompt:* Topic extraction.
*Analysis:* Relevant topics are "Breadth-First Search (BFS)", "Hash Table", "Graph", and "Array".

* `Breadth-First Search (BFS).md`: (already exists, reuse)
* `Hash Table.md`: (already exists, reuse)
* `Graph.md`

```markdown
# Graph

A graph is a data structure that consists of a set of vertices (nodes) and a set of edges that connect pairs of vertices. Graphs are used to model relationships between objects.

## Key Terminology

*   **Vertex (Node):** A fundamental unit of a graph.
*   **Edge:** A connection between two vertices.
*   **Directed Graph (Digraph):**  Edges have a direction (from one vertex to another).
*   **Undirected Graph:** Edges have no direction (connections are bidirectional).
*   **Weighted Graph:** Edges have associated weights (costs, distances, etc.).
*   **Unweighted Graph:** Edges have no weights.
*   **Path:** A sequence of vertices connected by edges.
*   **Cycle:** A path that starts and ends at the same vertex.
*   **Connected Graph:** There is a path between every pair of vertices.
*   **Disconnected Graph:** There are vertices that are not reachable from each other.
*   **Strongly Connected Graph (Directed Graph):** There is a directed path between every pair of vertices.
*   **Weakly Connected Graph (Directed Graph):**  If we ignore the direction of the edges, the graph is connected.
* **Adjacent vertices:** two vertices connected by an edge.
*   **Degree (of a vertex):** The number of edges connected to the vertex. In a directed graph, we have *in-degree* (number of incoming edges) and *out-degree* (number of outgoing edges).

## Graph Representations

*   **Adjacency Matrix:** A 2D array where `matrix[i][j]` indicates whether there is an edge between vertex `i` and vertex `j`.  Good for dense graphs (many edges).
*   **Adjacency List:**  An array (or hash table) of lists.  Each element in the array represents a vertex, and the corresponding list stores the neighbors (adjacent vertices) of that vertex.  Good for sparse graphs (few edges).

## Common Graph Algorithms

*   **Breadth-First Search (BFS):**  Visits vertices level by level, finding the shortest path in unweighted graphs.
*   **Depth-First Search (DFS):**  Visits vertices by exploring as far as possible along each branch before backtracking.
*   **Dijkstra's Algorithm:**  Finds the shortest paths from a source vertex to all other vertices in a weighted graph (with non-negative edge weights).
*   **Bellman-Ford Algorithm:**  Finds the shortest paths from a source vertex to all other vertices in a weighted graph (can handle negative edge weights).
*   **Floyd-Warshall Algorithm:**  Finds the shortest paths between all pairs of vertices in a weighted graph.
*   **Topological Sort:**  Orders the vertices of a directed acyclic graph (DAG) such that for every directed edge from vertex A to vertex B, vertex A comes before vertex B in the ordering.
*   **Minimum Spanning Tree (MST) Algorithms (Kruskal's, Prim's):** Find a tree that connects all vertices of a weighted, undirected graph with the minimum total edge weight.

## LeetCode problems related to Graph

*   [815. Bus Routes](0815-bus-routes/README.md)
*   [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) (can be seen as a graph problem)
*   [133. Clone Graph](https://leetcode.com/problems/clone-graph/)
*   [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)
*   [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
* [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
* [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)
* [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)
* [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)

```
* `Arrays.md`: (already exists, we reuse it).

This completes the repository, containing a well-documented BFS solution, a comprehensive README explaining the algorithm and its complexity, and links to all relevant topic files, including a newly created "Graph.md" file. It addresses all instructions and adheres to best practices.
