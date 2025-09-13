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

# Graphs

Graphs are a fundamental non-linear data structure used to represent relationships between objects.  They consist of nodes (vertices) connected by edges.  Graphs are incredibly versatile and are used to model a wide range of problems, from social networks to transportation networks to course schedules.

## Key Concepts

* **Node (Vertex):**  A fundamental unit of a graph, representing an object or entity.
* **Edge:** A connection between two nodes, representing a relationship.
* **Directed Graph (Digraph):**  Edges have a direction, indicating a one-way relationship (e.g., course prerequisites).
* **Undirected Graph:** Edges have no direction, indicating a two-way relationship (e.g., friendship on a social network).
* **Weighted Graph:** Edges have associated weights (costs, distances, etc.).
* **Unweighted Graph:** Edges have no weights.
* **Cycle:** A path that starts and ends at the same node.
* **Path:** A sequence of nodes connected by edges.
* **Connected Graph:**  There is a path between any two nodes in the graph.
* **Disconnected Graph:**  There are at least two nodes with no path between them.
* **Strongly Connected Graph (for directed graphs):**  There is a directed path between any two nodes.
* **Weakly Connected Graph (for directed graphs):**  If we ignore the direction of the edges, there is a path between any two nodes.
* **Adjacency Matrix:** A 2D array representation of a graph, where `matrix[i][j]` indicates whether there is an edge between node `i` and node `j`.
* **Adjacency List:**  A list-based representation where each node stores a list of its adjacent nodes.

## Common Graph Operations

* **Add Node:**  Adding a new node to the graph.
* **Add Edge:** Adding a new edge between two nodes.
* **Remove Node:** Removing a node and its associated edges.
* **Remove Edge:** Removing an edge between two nodes.
* **Check if Edge Exists:**  Determining if there is an edge between two nodes.
* **Get Neighbors:** Retrieving the list of nodes adjacent to a given node.

## Common Graph Algorithms

* **Depth-First Search (DFS):**  A traversal algorithm that explores as deeply as possible along each branch before backtracking.  Uses a stack (often implicitly via recursion).
* **Breadth-First Search (BFS):** A traversal algorithm that explores nodes level by level.  Uses a queue.
* **Topological Sort (for Directed Acyclic Graphs - DAGs):**  A linear ordering of nodes such that for every directed edge from node A to node B, node A comes before node B in the ordering.
* **Shortest Path Algorithms:**
  * **Dijkstra's Algorithm:** Finds the shortest path from a source node to all other nodes in a weighted graph with non-negative edge weights.
  * **Bellman-Ford Algorithm:**  Finds the shortest path from a source node to all other nodes in a weighted graph that may contain negative edge weights (but no negative cycles).
  * **Floyd-Warshall Algorithm:**  Finds the shortest paths between all pairs of nodes in a weighted graph.
* **Minimum Spanning Tree (MST) Algorithms:**
  * **Prim's Algorithm:**  Finds a minimum spanning tree for a weighted, undirected graph.
  * **Kruskal's Algorithm:** Finds a minimum spanning tree for a weighted, undirected graph.
* **Cycle Detection:** Determining if a graph contains cycles (important for many applications).

## Related LeetCode Problems

* [207. Course Schedule](./0207-course-schedule)
* [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
* [127. Word Ladder](https://leetcode.com/problems/word-ladder/)
* [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)
* [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)
* [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
