# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeDepth(object):
    def __init__(self, parents):
        self._parents = parents
        self._n = len(parents)
        self._max_depth = 0
        self._depths = [None] * self._n

    def max_depth(self):
        if self._max_depth == 0:
            for idx, parent in enumerate(self._parents):
                depth = self.get_depth(idx)
                if self._max_depth < depth:
                    self._max_depth = depth
        return self._max_depth

    def get_depth(self, idx):
        depth = self._depths[idx]
        if depth is not None:
            return depth
        parent = self._parents[idx]
        if parent == -1:
            depth = 1
        else:
            depth = self.get_depth(parent) + 1
        self._depths[idx] = depth
        return depth
def main():
  tree = int(sys.stdin.readline())
  parent = list(map(int, sys.stdin.readline().split()))
  print(TreeDepth(parent).max_depth())

threading.Thread(target=main).start()
