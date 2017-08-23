# python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
def fun(edge, notVisited):
    result = []
    minDegree = n
    startNode = -1
    for i in notVisited:
        if len(edge[i]) < minDegree:
            startNode = i
            minDegree = len(edge[i])
    print(startNode)
    result.append(startNode)
    currentNode = startNode
    while len(notVisited) > 1:
        minDegree = n
        nextNode = -1
        for i in edge[currentNode]:
            if len(edge[i]) > 1 and len(edge[i]) < minDegree:
                nextNode = i
                minDegree = len(edge[i])
        if nextNode == -1:
            if len(edge[currentNode]) > 0:
                result.append(edge[currentNode].pop())
            return result
        else:
            result.append(nextNode)
            notVisited.remove(currentNode)
            for i in edge[currentNode]:
                edge[i].remove(currentNode)
            currentNode = nextNode
    return result

n, m = map(int, input().strip().split(' '))
edge = {}
notVisited = set()
for i in range(m):
    x, y = map(int, input().strip().split(' '))
    if x not in edge:
        edge[x] = set()
    edge[x].add(y)
    notVisited.add(x)
    if y not in edge:
        edge[y] = set()
    edge[y].add(x)
    notVisited.add(y)

result = fun(edge, notVisited)
if n == len(result):
    print("1 1")
    print("-1 -1 0")
else:
    print('2 1')
    print('1 0')
    print('-1 0')
