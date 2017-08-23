# python3
import sys

class SuffixTreeNode:
    def __init__(self, children, parent, stringDepth, edgeStart, edgeEnd):
        self.parent = parent
        self.children = children
        self.stringDepth = stringDepth
        self.edgeStart = edgeStart
        self.edgeEnd = edgeEnd
def CreateNewLeaf(node, S, suffix):
    leaf = SuffixTreeNode({}, node, len(S) - suffix, suffix + node.stringDepth, len(S) - 1)
    node.children[S[node.edgeStart]] = leaf
    return leaf
def BreakEdge(node, S, start, offset):
    startChar = S[start]
    #print(startChar, node.children)
    midChar = S[start + offset]
    midNode = SuffixTreeNode({}, node, node.stringDepth + offset, start, start + offset - 1)
    try:
        midNode.chilren[midChar] =  node.children[startChar]
        node.children[startChar].parent = midNode
        node.children[startChar].edgeStart = start + offet
        node.children[startChar] = midNode
    except:
        return midNode
    return midNode
def suffix_array_to_suffix_tree(S, order, lcpArray):
    tree = []
    root = SuffixTreeNode({}, None, 0, -1, -1)
    lcpPrev = 0
    curNode = root
    temp = [[]*2]
    for i in range(len(S)):
        suffix = order[i]
        #print('suffix, lcpPrev',suffix, lcpPrev )
        while curNode.stringDepth > lcpPrev:
            curNode = curNode.parent
        if curNode.stringDepth == lcpPrev:
            curNode = CreateNewLeaf(curNode , S , suffix)
            #print(len(S)-suffix)
            #print(curNode.stringDepth, curNode.edgeStart, curNode.edgeEnd + 1)
            if i > 0:
                tree.append(temp)
                #print('if 1', temp)
            temp = [curNode.edgeStart, curNode.edgeEnd + 1]
            #print('thu 1', temp)
            if i == len(S) - 1:
                tree.append(temp)
        else:
            edgeStart = order[i - 1] + curNode.stringDepth
            #print(edgeStart)
            offset = lcpPrev - curNode.stringDepth
            midNode = BreakEdge(curNode , S , edgeStart , offset)
            #print(midNode.stringDepth, midNode.edgeStart,  midNode.edgeEnd + 1)
            tree.append([midNode.edgeStart,  midNode.edgeEnd + 1])
            temp[0] =  midNode.edgeEnd + 1
            tree.append(temp)
            #print('if2' ,temp)
            curNode = CreateNewLeaf(midNode , S , suffix)
            #print(curNode.stringDepth, curNode.edgeStart, curNode.edgeEnd + 1)
            temp = [curNode.edgeStart, curNode.edgeEnd + 1]
            if i == len(S) - 1:
                tree.append(temp)
        if i < len(S) - 1:
            lcpPrev = lcpArray[i]
    #print(tree)
    

    
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in the
    list must be sorted in the ascending order by the first character of the edge label.
    Root must have node ID = 0, and all other node IDs must be different
    nonnegative integers. Each edge must be represented by a tuple (node, start, end), where
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of text corresponding to the edge label
        * end is the first position (0-based) after the end of the substring corresponding to the edge label

    For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
    must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the list (because
    it has the smallest first character of all edges outgoing from the root).
    """
    
    # Implement this function yourself
    return tree


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    #print(sa)
    #print(lcp)
    # Build the suffix tree and get a mapping from 
    # suffix tree node ID to the list of outgoing Edges.
    tree = suffix_array_to_suffix_tree(text, sa, lcp)
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.
    
    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of 
    
        OutputEdges(tree, 0);
    
    for the following _recursive_ function OutputEdges:
    
    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);
    
    """
    for i in tree:
        print(*i, sep=' ')
