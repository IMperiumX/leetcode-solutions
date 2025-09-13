# Topological Sort

Topological sorting is an algorithm for ordering the nodes of a **directed acyclic graph (DAG)** such that for every directed edge from node A to node B, node A appears before node B in the ordering. In simpler terms, it's a way to linearly order the vertices of a DAG so that all dependencies are respected.

## Key Concepts

* **Directed Acyclic Graph (DAG):**  A directed graph with no cycles.  Topological sort is only possible on DAGs.
* **Dependency:**  A directed edge from node A to node B indicates that A is a dependency of B (B depends on A).  In the context of course scheduling, this means course A must be taken before course B.
* **Linear Ordering:**  The result of a topological sort is a linear sequence of the nodes.
* **Not Unique:**  A DAG may have multiple valid topological orderings.

## Algorithms for Topological Sorting

There are two primary algorithms for topological sorting:

1. **Kahn's Algorithm (BFS-based):**
    * **In-degree:**  The number of incoming edges to a node.
    * **Algorithm:**
        1. Compute the in-degree of all nodes.
        2. Enqueue all nodes with an in-degree of 0 (nodes with no dependencies).
        3. While the queue is not empty:
            * Dequeue a node.
            * Add the dequeued node to the topological ordering.
            * For each neighbor of the dequeued node:
                * Decrement its in-degree.
                * If the neighbor's in-degree becomes 0, enqueue it.
        4. If all nodes have been added to the ordering, the topological sort is successful.  Otherwise, the graph contains a cycle.

2. **DFS-based:**
    * **Algorithm:**
        1. Perform DFS on the graph.
        2. As each node finishes (all its descendants have been visited), add it to the *beginning* of a list (or the end, and then reverse).  This ensures that a node is added to the list only after all its dependencies have been added.

## Applications of Topological Sorting

* **Course Scheduling:** Determining a valid order to take courses with prerequisites.
* **Task Scheduling:**  Scheduling tasks with dependencies (e.g., in project management).
* **Build Systems:**  Determining the order to compile files in a software project.
* **Dependency Resolution:**  Resolving dependencies between software packages.
* **Dataflow Analysis:**  Analyzing the flow of data in a program.

## Related LeetCode Problems

* [207. Course Schedule](./0207-course-schedule)
* [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
* [444. Sequence Reconstruction](https://leetcode.com/problems/sequence-reconstruction/)
* [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) (Hard)
