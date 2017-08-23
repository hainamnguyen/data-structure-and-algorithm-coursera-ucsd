#Uses python3
import sys
import math

def weight_caculation(x1,y1,x2,y2):
    return math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))

def minimum_distance(x, y):
    numOfVer = len(x)
    infinity = float('inf')
    cost = [infinity for i in range(numOfVer)]
    cost[0] = 0
    distance = [[] for i in range(numOfVer)]
    #print(distance)
    for i in range(numOfVer):
        for j in range(numOfVer):
            if i < j:
                distance[i].append(weight_caculation(x[i],y[i],x[j],y[j]))
            elif i == j:
                distance[i].append(infinity)
            else:
                distance[i].append(distance[j][i])
    prioQ = {i:cost[i] for i in range(numOfVer)}
    #print(prioQ)
    while prioQ != {}:
        v = min(prioQ, key = prioQ.get)
        prioQ.pop(v)
        for i in range(numOfVer):
            if i in prioQ and cost[i] > distance[v][i]:
                cost[i] = distance[v][i]
                prioQ[i] = distance[v][i]
    return sum(cost)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = list(map(int, input().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
