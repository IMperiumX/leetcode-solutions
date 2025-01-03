import math


def find_the_city(n: int, edges: list[list[int]], distance_threshold: int) -> int:
    """
    Finds the city with the smallest number of reachable cities within a distance threshold.

    Args:
        n: The number of cities.
        edges: A list of edges, where each edge is represented as [from, to, weight].
        distance_threshold: The distance threshold.

    Returns:
        The city with the smallest number of reachable cities within the distance threshold.
    """

    # Initialize the distance matrix with infinity for all pairs except self-loops, which are 0.
    dist = [[math.inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    # Populate the distance matrix with the given edge weights.
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w  # Since the graph is undirected

    # Floyd-Warshall algorithm to compute shortest paths between all pairs of cities.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Count the number of reachable cities within the distance threshold for each city.
    reachable_cities_count = []
    for i in range(n):
        count = 0
        for j in range(n):
            if dist[i][j] <= distance_threshold:
                count += 1
        reachable_cities_count.append(count)

    # Find the city with the smallest number of reachable cities.
    min_cities = math.inf
    city = -1
    for i, count in enumerate(reachable_cities_count):
        if count <= min_cities:
            min_cities = count
            city = i

    return city
