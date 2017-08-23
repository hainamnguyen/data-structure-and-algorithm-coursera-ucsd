# python3

# It's to find out max flow in a flow network
# It's similar to Ford-Fulkerson algorithm,
# but defines search order for augmenting path
# The path found must be a shortest path that has available capacity.

def EdmondsKarp(capacity, neighbors, start, end):
  flow = 0
  length = len(capacity)
  flows = [[0 for i in range(length)] for j in range(length)]
  #print('Flows before:', flows)
  
  while True:
    max, parent = BreadthFirstSearch(capacity, neighbors, flows, start, end)
    #print('max:', max)
    print(parent)
    if max == 0:
      break
    flow = flow + max
    v = end
    while v != start:
      u = parent[v]
      flows[u][v] = flows[u][v] + max
      flows[v][u] = flows[v][u] - max
      v = u
  #print(flow)
      
  return flow

def BreadthFirstSearch(capacity, neighbors, flows, start, end):
  length = len(capacity)
  parents = [-1 for i in range(length)] # parent table
  parents[start] = -2 # make sure source is not rediscovered
  M = [0 for i in range(length)] # Capacity of path to vertex i
  M[start] = float('inf') # this is necessary!
  queue = []
  queue.append(start)
  
  while queue:
    u = queue.pop(0)
    for v in neighbors[u]:
      # if there is available capacity and v is is not seen before in search
      if capacity[u][v] - flows[u][v] > 0 and parents[v] == -1:
        parents[v] = u
        #print('v', v)
        # it will work because at the beginning M[u] is Infinity
        M[v] = min(M[u], capacity[u][v] - flows[u][v]) # try to get smallest
        #print(v, M[v], M[u], capacity[u][v] - flows[u][v])
        #print('u', u)
        #print(M)
        if v != end:
          queue.append(v)
        else:
          return M[end], parents
        
  return 0, parents

def read_data():
  vertex_count, edge_count = map(int, input().split())
  neighbors = {} # neighbors include reverse direction neighbors
  
  for i in range(vertex_count):
      neighbors[i] = []
  capacity = [[0 for i in range(vertex_count)] for j in range(vertex_count)]
  for i in range(edge_count):
    a, b, capa = map(int, input().split())
    neighbors[a - 1].append(b - 1)
    neighbors[b - 1].append(a - 1) # reverse path may be used
    capacity[a-1][b-1] += capa
  #print('c', capacity)
  #print('n', neighbors)
    
  return capacity, neighbors
if __name__ == "__main__":
  capacity, neighbors = read_data()
  #for line in capacity:
    #print(line)
  #print(neighbors)
  
  print(EdmondsKarp(capacity, neighbors, 0, len(capacity) - 1))
  #print('Flow matrix:')
  #for line in flows:
    #print (line)
