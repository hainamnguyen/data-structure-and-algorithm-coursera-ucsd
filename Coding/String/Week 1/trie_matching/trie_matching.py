# python3
import sys

#NA = -1

#class Node:
        #def __init__ (self):
		#self.next = [NA] * 4
def build_trie(patterns):
    #print(patterns)
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
                    #if i == len(pattern)-1:
                            #print(i)
                            #try:
                                    #tree[currentNode]['leaf'] = 1
                            #except:
                                    #continue
                    #print(currentNode)
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
            if i == len(pattern) - 1:
                    try:
                        tree[currentNode]['leaf'] = 1
                    except:
                        tree[currentNode] = dict()
                        tree[currentNode]['leaf'] = 1
                        continue
                #print(currentNode)
    # write your code here
    #print(tree)
    return tree

def solve (text, n, patterns):
        result = list()
        trie = build_trie(patterns)
        #print(trie)
        for i in range(len(text)):
                #print(text[i])
                symbol = text[i]
                j = i
                v = 0
                while i >= 0:
                        #print(v)
                        if 'leaf' in trie[v]:
                                #print(v, 0)
                                result.append(i)
                                break
                        elif symbol in trie[v]:
                                #print(symbol, trie[v])
                                v = trie[v][symbol]
                                j += 1
                                if j > len(text) -1:
                                        if v not in trie or 'leaf' in trie[v]:
                                                result.append(i)
                                        break
                                symbol = text[j]
                                
                                #print(v, 1)
                        else:
                                #print(v, 2)
                                break
        return result
        #print(result)

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = sys.stdin.read().split()
#text = input()
#n = int(input())
#patterns = input().split(' ')
ans = solve (text, n, patterns)
#print(ans)
sys.stdout.write (' '.join (map (str, ans)) + '\n')
