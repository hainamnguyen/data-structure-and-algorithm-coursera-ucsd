# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
    #print(self.key)
    #print(set(i for i in range(self.n)))
    #print(set(self.left).union(set(self.right)))
    #print(set(i for i in range(self.n)).difference(set(self.left).union(set(self.right))))
    self.root = set(i for i in range(self.n)).difference(set(self.left).union(set(self.right))).pop()
    #print(self.root)
  def inOrder(self):
    self.result = []
    def countInOrder(i):
      if i == -1:
        return
      countInOrder(self.left[i])
      self.result.append((self.key[i]))
      #print(self.key[i])
      countInOrder(self.right[i])
    countInOrder(self.root)
    #print(countInOrder(4))
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return self.result

  def preOrder(self):
    self.result = []
    def countPreOrder(i):
      if i == -1:
        return
      self.result.append((self.key[i]))
      countPreOrder(self.left[i])
      countPreOrder(self.right[i])
    countPreOrder(self.root)
    # Finish the implementation
    # You may need to add a new recursive method to do that     
    return self.result

  def postOrder(self):
    self.result = []
    def countPostOrder(i):
      if i == -1:
        return
      countPostOrder(self.left[i])
      countPostOrder(self.right[i])
      self.result.append((self.key[i]))
    countPostOrder(self.root)
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
