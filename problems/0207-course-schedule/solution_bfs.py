# 207. Course Schedule - Topological Sort (Kahn's Algorithm - BFS)
from collections import deque


def canFinish(numCourses, prerequisites):
    """
       Determines if it is possible to finish all courses. (Topological Sort)
    Args:
        numCourses (int): The number of courses
        prerequisites (List[List[int]]): prerequisites[i] = [ai, bi] indicates that you must take course bi first

    Returns:
        bool: True if you can finish all courses. Otherwise, return false.
    """
    in_degree = [0] * numCourses
    adj = [[] for _ in range(numCourses)]

    for course, pre in prerequisites:
        adj[pre].append(course)
        in_degree[course] += 1

    queue = deque()

    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    count = 0
    while queue:
        course = queue.popleft()
        count += 1

        for neighbor in adj[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return count == numCourses
