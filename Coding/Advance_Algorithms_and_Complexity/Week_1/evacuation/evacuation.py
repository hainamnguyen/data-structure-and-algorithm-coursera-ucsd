# python3

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)
        #print(from_, to)
        #print(self.graph)
        #print(self.edges)
    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        
def distance(edges, s, t, numberofV):
    adj = [[] for i in range(numberofV)]
    #for i in edges:
        #print(i.u, i.v, i.capacity, i.flow)
    for i in range(len(edges)):
        if (edges[i].flow == edges[i].capacity and i%2 == 0) or (edges[i].flow == 0 and i%2 == 1):
            continue
        else:
            #print(edges[i].u, edges[i].v, i)
            adj[edges[i].u].append([edges[i].v, i, edges[i].capacity])
    #print(adj)
    dist = [[-1]for i in range(len(adj))]
    dist[s][0] = 0
    #print(dist)
    Q = [s]
    while len(Q) != 0:
        u = Q.pop(0)
        #print(u)
        for adj_cou in range(len(adj[u])):
            #print(adj[u][adj_cou])
            #print(adj[u][adj_cou][0])
            if dist[adj[u][adj_cou][0]][0] == -1:
                #print('wo')
                Q.append(adj[u][adj_cou][0])
                #print(Q)
                dist[adj[u][adj_cou][0]][0] = dist[u][0] + 1
                #print(dist)
                try:
                    dist[adj[u][adj_cou][0]] += dist[u][1:]
                    dist[adj[u][adj_cou][0]].append([u, adj[u][adj_cou][1], adj[u][adj_cou][2]])
                except:
                    #print('wow')
                    dist[adj[u][adj_cou]].append([u, adj[u][adj_cou][1], adj[u][adj_cou][2]])
                if [adj[u][adj_cou][0]][0] == t:
                    return dist[t]
                #print(dist)
    #write your code here
    return dist[t]


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    #print(graph)
    return graph


def max_flow(graph, from_, to):
    flow = 0
    while True:
        path = distance(graph.edges, from_, to, to + 1)
        if path[0] == -1:
            break
        #print(path)
        path.remove(path[0])
        x = min(c for [a,b,c] in path)
        flow += x
        for i in path:
            graph.add_flow(i[1], x)       
    
    return flow


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
