import math
# Add any extra import statements you may need here
import heapq

# Add any helper functions you may need here


def minOperations(arr):
  # Write your code here
  graph = {}
  generate_graph(graph, [], sorted(arr))
  for node in graph.keys():
    for i in range(2, len(arr)+1):
      for j in range(0, len(arr)-i+1):
        neighbor = list(node)
        neighbor = neighbor[:j] + neighbor[j:j+i][::-1] + neighbor[j+i:]
        graph[node].append(tuple(neighbor))
        
  return dijkstra(graph,tuple(arr), tuple(sorted(arr)))
        
def generate_graph(result, curr_num, next_num):
  if not next_num:
    result[tuple(curr_num)] = []
    
  for i in range(len(next_num)):
    generate_graph(result, curr_num+[next_num[i]], next_num[:i]+next_num[i+1:])

def dijkstra(graph, source, target):
    
    dist = {}
    prev = {}
    
    q = []
    dist[source] = 0
    for node in graph.keys():
        if node != source:
            dist[node] = float('inf')
        heapq.heappush(q, (dist[node], node))
    
    while q:
        p,node = heapq.heappop(q)
        if p > dist[node]:
            continue
        for neighbor in graph[node]:
            alt = dist[node] + 1
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = node
                heapq.heappush(q, (alt, neighbor))
                
    return dist[target]