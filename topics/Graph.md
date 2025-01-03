# Graph

## Definition

A graph is a data structure that consists of a set of vertices (or nodes) and a set of edges that connect pairs of vertices. Graphs are used to represent relationships or connections between objects.

## Types of Graphs

* **Undirected Graph:** Edges have no direction. If there's an edge between vertex A and B, you can traverse from A to B and from B to A.
* **Directed Graph:** Edges have a direction. An edge from vertex A to B doesn't imply an edge from B to A.
* **Weighted Graph:** Edges have weights or costs associated with them.
* **Unweighted Graph:** Edges have no weights.
* **Cyclic Graph:** Contains at least one cycle (a path that starts and ends at the same vertex).
* **Acyclic Graph:** Contains no cycles.

## Representations

* **Adjacency Matrix:** A 2D array where `matrix[i][j]` represents the presence or absence (or weight) of an edge between vertex `i` and vertex `j`.
* **Adjacency List:** An array of lists where each index `i` represents a vertex, and the list at that index contains the neighbors of vertex `i`.

## Common Algorithms

* **Depth-First Search (DFS):** Traverses a graph by exploring as far as possible along each branch before backtracking.
* **Breadth-First Search (BFS):** Traverses a graph level by level, visiting all neighbors of a vertex before moving to their neighbors.
* **Dijkstra's Algorithm:** Finds the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative edge weights.
* **Bellman-Ford Algorithm:** Finds the shortest path from a single source vertex to all other vertices in a weighted graph, even if it contains negative edge weights (but no negative cycles).
* **Floyd-Warshall Algorithm:** Finds the shortest paths between all pairs of vertices in a weighted graph.
* **Kruskal's Algorithm:** Finds the minimum spanning tree of a weighted, undirected graph.
* **Prim's Algorithm:** Another algorithm to find the minimum spanning tree of a weighted, undirected graph.

## Applications

* Social networks (representing connections between users)
* Maps and navigation (representing roads and intersections)
* Network routing (representing connections between routers)
* Recommendation systems
* Dependency resolution
* Many more...

## Related LeetCode Problems

* [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
* [133. Clone Graph](https://leetcode.com/problems/clone-graph/)
* [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
* [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)
* [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)
* [997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)
* [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
