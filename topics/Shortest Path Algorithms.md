# Shortest Path Algorithms

## Introduction

Shortest path algorithms are used to find the shortest path between two vertices in a graph. The "shortest" path can be defined in terms of distance, time, cost, or any other relevant metric.

## Types of Shortest Path Problems

* **Single-Source Shortest Path:** Find the shortest path from a single source vertex to all other vertices in the graph.
* **All-Pairs Shortest Path:** Find the shortest paths between all pairs of vertices in the graph.

## Common Algorithms

### 1. Dijkstra's Algorithm

* **Type:** Single-Source Shortest Path
* **Graph Type:** Weighted, directed or undirected graphs with **non-negative edge weights**.
* **Approach:** Uses a greedy approach and a priority queue (often implemented as a min-heap) to iteratively find the shortest path to each vertex.
* **Time Complexity:** O(E + V log V) using a Fibonacci heap, where V is the number of vertices and E is the number of edges. O(V^2) using a simple array-based priority queue.
* **Space Complexity:** O(V)

### 2. Bellman-Ford Algorithm

* **Type:** Single-Source Shortest Path
* **Graph Type:** Weighted, directed or undirected graphs. Can handle **negative edge weights** but cannot handle **negative cycles** (cycles where the sum of edge weights is negative).
* **Approach:** Iteratively relaxes edges, updating the shortest distance to each vertex until no further improvements can be made.
* **Time Complexity:** O(V \* E), where V is the number of vertices and E is the number of edges.
* **Space Complexity:** O(V)

### 3. Floyd-Warshall Algorithm

* **Type:** All-Pairs Shortest Path
* **Graph Type:** Weighted, directed or undirected graphs. Can handle **negative edge weights** but cannot handle **negative cycles**.
* **Approach:** Uses dynamic programming to consider all possible intermediate vertices between each pair of vertices and updates the shortest distance if a shorter path is found.
* **Time Complexity:** O(V^3), where V is the number of vertices.
* **Space Complexity:** O(V^2)

### 4. Breadth-First Search (BFS)

* **Type:** Single-Source Shortest Path
* **Graph Type:** Unweighted, directed or undirected graphs.
* **Approach:** Traverses the graph level by level, finding the shortest path in terms of the number of edges.
* **Time Complexity:** O(V + E), where V is the number of vertices and E is the number of edges.
* **Space Complexity:** O(V)

## Applications

* **GPS Navigation:** Finding the shortest route between two locations.
* **Network Routing:** Determining the optimal path for data packets to travel across a network.
* **Resource Allocation:** Finding the most efficient way to allocate resources.
* **Robotics:** Planning the shortest path for a robot to move from one point to another.

## Related LeetCode Problems

* [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) (Dijkstra's)
* [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) (Bellman-Ford variation)
* [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) (Floyd-Warshall or multiple Dijkstra's)
