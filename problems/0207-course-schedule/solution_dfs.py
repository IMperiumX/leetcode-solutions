# 207. Course Schedule - DFS with Cycle Detection


def canFinish(numCourses, prerequisites):
    """
    Determines if it's possible to finish all courses given prerequisites.

    Args:
        numCourses: The total number of courses.
        prerequisites: A list of prerequisite pairs (e.g., [course, prerequisite]).

    Returns:
        True if all courses can be finished, False otherwise.
    """
    # Build the adjacency list (graph representation)
    adj = [[] for _ in range(numCourses)]
    for course, pre in prerequisites:
        adj[pre].append(course)

    # 0: unvisited, 1: visiting, 2: visited
    visited = [0] * numCourses

    def dfs(course):
        """
        Performs DFS to detect cycles.
        """
        if visited[course] == 1:  # Currently visiting -> Cycle detected
            return False
        if visited[course] == 2:  # Already visited -> No cycle
            return True

        visited[course] = 1  # Mark as currently visiting

        for neighbor in adj[course]:
            if not dfs(neighbor):
                return False

        visited[course] = 2  # Mark as visited
        return True

    # Check for cycles starting from each course
    for course in range(numCourses):
        if not dfs(course):
            return False

    return True
