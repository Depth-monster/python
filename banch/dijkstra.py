import heapq
import math

def dijkstra(graph, start):
    distances = {node: math.inf for node in graph}
    distances[start] = 0
    visited = set()
    heap = [(0, start)]
    
    while heap:
        (dist, node) = heapq.heappop(heap)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbor, weight in graph[node].items():
            new_distance = dist + weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))
                
    return distances
