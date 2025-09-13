# 207. Course Schedule, Difficulty: Medium

## Problem Description

There are a total of `numCourses` courses you have to take, labeled from 0 to `numCourses` - 1. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]`, indicates that to take course 0 you have to first take course 1.

Return `true` if you can finish all courses. Otherwise, return `false`.

- Example 1:

- Input: numCourses = 2, prerequisites = [[1,0]]
- Output: true
- Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

- Example 2:

- Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
- Output: false
- Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

- Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

## Approach(es)

### Depth-First Search (DFS) with Cycle Detection

Algorithm:

1. **Build Adjacency List:** Create an adjacency list to represent the graph, where `adj[i]` is a list of courses that depend on course `i` (courses that have `i` as a prerequisite).
2. **Visited Array:**  Create a `visited` array to track the visitation status of each course during DFS.  Use three states:
    - 0: Unvisited
    - 1: Currently visiting (in the current DFS path)
    - 2: Visited (and all its descendants have been visited)
3. **DFS Function:**  Create a recursive `dfs(course)` function:
    - **Cycle Detection:** If `visited[course]` is 1 (currently visiting), a cycle is detected, so return `False`.
    - **Already Visited:** If `visited[course]` is 2 (already visited), return `True` (no cycle found in this branch).
    - **Mark Visiting:** Mark `visited[course]` as 1 (currently visiting).
    - **Explore Neighbors:** For each `neighbor` in `adj[course]`, recursively call `dfs(neighbor)`.  If any recursive call returns `False` (cycle detected), return `False`.
    - **Mark Visited:** Mark `visited[course]` as 2 (visited).
    - **Return True:** Return `True` (no cycle found in this branch).
4. **Iterate and Check:** Iterate through all courses (from 0 to `numCourses` - 1).  For each course, if it hasn't been visited yet, call `dfs(course)`. If `dfs` returns `False` at any point, return `False` (a cycle exists).
5. **Return True:** If all DFS calls return `True` (no cycles found), return `True`.

Data Structures:

- Adjacency List (list of lists) to represent the graph.
- `visited` array (list) to track node visitation status.

Time Complexity:

- O(V + E), where V is the number of courses (`numCourses`) and E is the number of prerequisites (`len(prerequisites)`).  We visit each node and edge at most once.

Space Complexity:

- O(V + E) in the worst case, for the adjacency list and the recursion stack.  In the worst case, the recursion depth could be V.

Trade-offs:

- The DFS approach is a classic way to detect cycles in a directed graph. It's relatively straightforward to implement.

### Topological Sort using Kahn's Algorithm(BFS)

Algorithm:

- 1. Build Adjacency List and calculate in-degrees: Represent the course dependencies as a directed graph using an adjacency list. Simultaneously, calculate the in-degree of each course (the number of prerequisites it has).
- 2. Initialize Queue: Create a queue and add all courses with an in-degree of 0 (courses with no prerequisites).
- 3. Process Queue: While the queue is not empty.
    Remove a course from the queue.
    Increment a counter that tracks the number of processed courses.
    For each neighbor (course that depends on the current course) in the adjacency list:
        Decrement its in-degree.
        If the neighbor's in-degree becomes 0, add it to the queue.

- 4. Check for Cycle: If the count of processed courses equals numCourses, it means all courses could be taken in a valid order, and there is no cycle. Return true.
Otherwise, there is a cycle, and it's impossible to finish all courses. Return false.

Data Structures:
    *Adjacency List
    *  Queue
    * In-Degree array

Time Complexity:

- O(V + E), where V is the number of courses (`numCourses`) and E is the number of prerequisites (`len(prerequisites)`).

Space Complexity:

- O(V + E) for the adjacency list, in-degree array and the queue.

Trade-offs:
    * The BFS approach usually a good alternative for DFS

## Code

[DFS with Cycle Detection](./solution_dfs.py)
[Topological Sort (Kahn's Algorithm - BFS)](./solution_bfs.py)

## Notes

This problem is a fundamental graph problem that can be solved using either DFS or BFS. The DFS approach directly detects cycles, while the BFS approach (Kahn's Algorithm) performs a topological sort, and the ability to complete the sort implies the absence of cycles. Both methods are efficient and have the same time and space complexity.
