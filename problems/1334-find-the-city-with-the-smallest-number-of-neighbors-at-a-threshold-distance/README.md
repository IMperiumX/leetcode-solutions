# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance, Difficulty: Medium

## Problem Description

There are `n` cities numbered from 0 to `n-1`. Given the array `edges` where `edges[i] = [from_i, to_i, weight_i]` represents a bidirectional and weighted edge between cities `from_i` and `to_i`, and given the integer `distanceThreshold`.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most `distanceThreshold`. If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities `i` and `j` is equal to the sum of the edges' weights along that path.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/01/16/find_the_city_01.png" width="600"  />

**Input:** `n = 4`, `edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]`, `distanceThreshold = 4`

**Output:** `3`

**Explanation:** The figure above describes the graph.

The neighboring cities at a `distanceThreshold = 4` for each city are:

* City 0 -> \[City 1, City 2]
* City 1 -> \[City 0, City 2, City 3]
* City 2 -> \[City 0, City 1, City 3]
* City 3 -> \[City 1, City 2]

Cities 0 and 3 have 2 neighboring cities at a `distanceThreshold = 4`, but we have to return city 3 since it has the greatest number.

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/01/16/find_the_city_02.png" width="600" />

**Input:** `n = 5`, `edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]`, `distanceThreshold = 2`

**Output:** `0`

**Explanation:** The figure above describes the graph.

The neighboring cities at a `distanceThreshold = 2` for each city are:

* City 0 -> \[City 1]
* City 1 -> \[City 0, City 4]
* City 2 -> \[City 3, City 4]
* City 3 -> \[City 2, City 4]
* City 4 -> \[City 1, City 2, City 3]

The city 0 has 1 neighboring city at a `distanceThreshold = 2`.

**Constraints:**

* `2 <= n <= 100`
* `1 <= edges.length <= n * (n - 1) / 2`
* `edges[i].length == 3`
* `0 <= from_i < to_i < n`
* `1 <= weight_i, distanceThreshold <= 10^4`
* All pairs `(from_i, to_i)` are distinct.

## Approach(es)

### Floyd-Warshall Algorithm

#### Algorithm

1. Initialize a distance matrix `dist` of size `n x n` with infinity, representing that initially, no city is reachable from any other city except itself (distance 0).
2. Populate the `dist` matrix with the given edge weights. For each edge `(u, v, w)`, set `dist[u][v] = w` and `dist[v][u] = w` (since it's an undirected graph).
3. Apply the Floyd-Warshall algorithm:
    * Iterate through all possible intermediate vertices `k` (from 0 to `n-1`).
    * For each pair of vertices `i` and `j`, check if going from `i` to `j` through `k` results in a shorter path than the currently known shortest path. If so, update `dist[i][j]` with the shorter distance.
4. After the Floyd-Warshall algorithm, `dist[i][j]` will contain the shortest distance between city `i` and city `j`.
5. For each city `i`, count the number of cities reachable within the `distanceThreshold`.
6. Find the city with the minimum number of reachable cities. If there's a tie, choose the city with the largest index.

#### Data Structures

* A 2D array (matrix) `dist` of size `n x n` to store the shortest distances between all pairs of cities.

#### Time Complexity

* O(n^3) due to the three nested loops in the Floyd-Warshall algorithm.

#### Space Complexity

* O(n^2) to store the distance matrix.

#### Trade-offs

* **Pros:** Relatively simple to implement, computes all-pairs shortest paths, which might be useful for other queries.
* **Cons:** Can be less efficient than Dijkstra's algorithm for sparse graphs.

### Dijkstra's Algorithm

#### Algorithm

1. Build an adjacency list representation of the graph from the given edges.
2. For each city `i`, run Dijkstra's algorithm to find the shortest distances from city `i` to all other cities.
    * Initialize a `distances` array with infinity for all cities except the starting city `i`, which has a distance of 0.
    * Use a priority queue (min-heap) to store (distance, city) pairs, prioritizing cities with smaller distances.
    * While the priority queue is not empty:
        * Extract the city `u` with the minimum distance.
        * For each neighbor `v` of `u`:
            * Calculate the distance to `v` through `u`.
            * If this distance is shorter than the current distance to `v`, update the distance in the `distances` array and add `(distance, v)` to the priority queue.
3. After running Dijkstra's algorithm for each city, count the number of cities reachable within the `distanceThreshold`.
4. Find the city with the minimum number of reachable cities. If there's a tie, choose the city with the largest index.

#### Data Structures

* An adjacency list to represent the graph.
* A `distances` array to store the shortest distances from the starting city.
* A priority queue (min-heap) for Dijkstra's algorithm.

#### Time Complexity

* O(n \* (E + V log V)) where V is the number of vertices (cities) and E is the number of edges. Since we run Dijkstra's algorithm for each city, it's multiplied by `n`.

#### Space Complexity

* O(V + E) for the adjacency list and distances array. The priority queue can have at most O(E) elements in the worst case.

#### Trade-offs

* **Pros:** More efficient than Floyd-Warshall for sparse graphs.
* **Cons:** More complex to implement than Floyd-Warshall.

## Code

* [Floyd-Warshall Approach](./solution_floyd_warshall.py)
* [Floyd-Warshall Approach](./solution_dijkstra.py)

## Notes

* The problem can also be solved using the Bellman-Ford algorithm, but it would be less efficient than Floyd-Warshall or Dijkstra's in this case because we need to find shortest paths from multiple sources.
* Floyd-Warshall is generally preferred when the graph is dense (many edges), while Dijkstra's is preferred for sparse graphs.
* The choice between Floyd-Warshall and Dijkstra's can also depend on whether you need all-pairs shortest paths (Floyd-Warshall) or just single-source shortest paths from multiple sources (Dijkstra's).
