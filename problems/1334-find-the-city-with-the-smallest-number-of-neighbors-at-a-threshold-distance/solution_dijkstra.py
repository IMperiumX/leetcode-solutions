import heapq


def find_the_city(n: int, edges: list[list[int]], distance_threshold: int) -> int:
    """
    Finds the city with the smallest number of reachable cities within a distance threshold using Dijkstra's algorithm.

    Args:
        n: The number of cities.
        edges: A list of edges, where each edge is represented as [from, to, weight].
        distance_threshold: The distance threshold.

    Returns:
        The city with the smallest number of reachable cities within the distance threshold.
    """

    # Build the adjacency list representation of the graph.
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # Since the graph is undirected

    def dijkstra(start_node):
        """
        Computes the shortest distances from a start node to all other nodes using Dijkstra's algorithm.
        """
        distances = {i: float("inf") for i in range(n)}
        distances[start_node] = 0
        priority_queue = [(0, start_node)]  # (distance, node)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # If we've found a shorter path, skip this one.
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances

    # Count the number of reachable cities within the distance threshold for each city.
    reachable_cities_count = []
    for i in range(n):
        distances = dijkstra(i)
        count = sum(1 for d in distances.values() if d <= distance_threshold)
        reachable_cities_count.append(count)

    # Find the city with the smallest number of reachable cities.
    min_cities = float("inf")
    city = -1
    for i, count in enumerate(reachable_cities_count):
        if count <= min_cities:
            min_cities = count
            city = i

    return city
