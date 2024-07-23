import heapq


def dijkstra(graph, start):
  V = len(graph)

  pq = [(0, start)]

  distances = {vertex: float('infinity') for vertex in range(V)}

  distances[start] = 0
  

  while pq:
    current_distance, current_vertex = heapq.heappop(pq)

    if current_distance > distances[current_vertex]:
      continue
    for neighbor, weight in graph[current_vertex].items():
      distance = current_distance + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(pq, (distance, neighbor))
        print(pq)

  return distances


graph = {
    0: {1: 2, 2: 4},
    1: {2: 1, 3: 7},
    2: {4: 3},
    3: {5: 1},
    4: {3: 2, 5: 5},
    5: {}
}

start_node = 0
distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node, "to all other nodes:", distances)
