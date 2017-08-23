#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    print(patterns)
    tree = dict()
    tree[0] = dict()
    tree[0][patterns[0][0]] = 1
    numberOfNode = 1
    for pattern in patterns:
        currentNode = 0
        for i in range(len(pattern)):
            currentSymbol = pattern[i]
            #print(currentSymbol)
            try:
                if currentSymbol in tree[currentNode]:
                    currentNode = tree[currentNode][currentSymbol]
                    print(i, len(pattern))
                    if i == len(pattern) - 1:
                        #print("wow")
                        try:
                            tree[currentNode]['leaf'] = 1
                        except:
                            continue
                    print(currentNode)
                else:
                    numberOfNode += 1
                    tree[currentNode][currentSymbol] = numberOfNode
                    currentNode = numberOfNode
                    #print(currentNode)
            except:
                tree[currentNode] = dict()
                numberOfNode += 1
                tree[currentNode][currentSymbol] = numberOfNode
                currentNode = numberOfNode
                #print(currentNode)
    # write your code here
    print(tree)
    return tree


if __name__ == '__main__':
    #patterns = sys.stdin.read().split()[1:]
    patterns = input().split(' ')
    #print(patterns)
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
