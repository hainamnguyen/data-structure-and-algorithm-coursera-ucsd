# python3

class HeapBuilder:
  def __init__(self):
    self.swaps = []
    self.data = []
    self.size = 0

  def ReadData(self):
    n = int(input())
    self.data = [int(s) for s in input().split()]
    assert n == len(self.data)

  def WriteResponse(self):
    print(len(self.swaps))
    for swap in self.swaps:
      print(swap[0], swap[1])
      #a = 2

  def shift_Down(self,i):
    minIndex = i
    l = self.leftChild(i)
    if l <= self.size - 1 and self.data[l] < self.data[minIndex]:
      minIndex = l
    r = self.rightChild(i)
    #print(r)
    if r <= self.size - 1 and self.data[r] < self.data[minIndex]:
      minIndex = r
    if i != minIndex:
      self.data[i], self.data[minIndex] = self.data[minIndex],self.data[i]
      self.shift_Down(minIndex)
  def leftChild(self,i):
    return 2*i + 1
  def rightChild(self,i):
    return 2*i + 2

  def GenerateSwaps(self):
    self.size = len(self.data)
    loop = int(self.size/2) - 1 
    while loop >= 0:
      #print(loop)
      self.shift_Down(loop)
      loop -= 1
    #print(self.data)  
  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
