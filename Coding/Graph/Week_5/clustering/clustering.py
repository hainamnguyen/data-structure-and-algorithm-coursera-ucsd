#Uses python3
import sys
import math

rank = list()
parent = list()

def weight_caculation(x1,y1,x2,y2):
    return math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
    

def find(i):
    global parent
    if i != parent[i]:
        #print(i, parent[i])
        i = parent[i]
    return parent[i]
def Union(i,j):
    #print(i,j)
    global rank
    global parent
    i_id = find(i)
    j_id = find(j)
    #print(i_id,j_id)
    if i_id == j_id:
        return
    if rank[i_id] > rank[j_id]:
        temp = parent[j_id]
        for t in range(len(parent)):
            if parent[t] == temp:
                parent[t] = i_id
    else:
        temp = parent[i_id]
        for t in range(len(parent)):
            #print(t,parent[t],parent[i_id] )
            if parent[t] == temp:
                #print('wow')
                parent[t] = j_id
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1
def clustering(x, y, k):
    #write your code here
    global rank
    global parent
    numOfVer = len(x)
    infinity = float('inf')
    distance = []
    for i in range(numOfVer):
        for j in range(numOfVer):
            if i < j:
                distance.append([weight_caculation(x[i],y[i],x[j],y[j]), i , j])
            elif i == j:
                continue
            else:
                continue
    distance.sort()
    #print(distance)
    for i in distance:
        #print(parent)
        if find(i[1]) != find(i[2]):
            #print(i[0],i[1],i[2])
            if len(set(parent)) == k:
                return i[0]
            Union(i[1],i[2])
        
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = list(map(int, input().split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    rank = [0 for i in range(len(x))]
    parent = list(range(len(x)))
    print("{0:.9f}".format(clustering(x, y, k)))



    

    
