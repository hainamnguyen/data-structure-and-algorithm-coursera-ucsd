# python3
import sys


def build_suffix_array(S):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  order = SortCharacters(S)
  class_ = ComputeCharClasses(S, order)
  L = 1
  while L < len(S):
    order = SortDoubled(S , L , order , class_)
    class_ = UpdateClasses(order , class_ , L)
    L = 2*L
  return order

def SortCharacters(S):
  sufiixList = []
  
  for i in range(len(S)):
    sufiixList.append([S[i],i])
  #print(sufiixList)
  sufiixList.sort()
  
  return [i[1] for i in sufiixList]

def ComputeCharClasses(S, order):
  lenOfS = len(S)
  class_ = [[]] * lenOfS
  class_[order[0]] = 0
  
  for i in range(1,lenOfS):
    if S[order[i]] != S[order[i-1]]:
      class_[order[i]] = class_[order[i - 1]] + 1
    else:
      class_[order[i]] = class_[order[i-1]]
      
  return class_
def SortDoubled(S, L, order, class_):
  lenOfS = len(S)
  count = [0 for i in range(lenOfS)]
  newOrder = [[] for i in range(lenOfS)]

  for i in range(0, lenOfS):
    count[class_[i]] = count[class_[i]] + 1
  #print(count)
  for j in range(1, lenOfS):
    count[j] = count[j] + count[j - 1]
  #print(count)
  for i in range(lenOfS - 1, -1, -1):
    start = (order[i] - L + lenOfS) % lenOfS
    cl = class_[start]
    count[cl] = count[cl] - 1
    newOrder[count[cl]] = start
    
  return newOrder

def UpdateClasses(newOrder, class_, L):
  n = len(newOrder)
  newClass= [[] for i in range(n)]
  newClass[newOrder[0]] = 0
  #print(newClass)
  for i in range(1, n):
    cur = newOrder[i]
    prev = newOrder[i - 1]
    mid = (cur + L) % n
    midPrev = (prev + L) % n
    if class_[cur] != class_[prev] or class_[mid] != class_[midPrev]:
      temp = newClass[prev] + 1
      newClass[cur] = temp
    else:
      newClass[cur] = newClass[prev]
  return newClass
  
if __name__ == '__main__':
  text = input()
  print(" ".join(map(str, build_suffix_array(text))))
  #order = SortCharacters(text)
  #print(" ".join(map(str, order)))
  #class_ = ComputeCharClasses(text, order)
  #print(" ".join(map(str, class_)))
  #newOrder = SortDoubled(text, 1, order, class_)
  #print(" ".join(map(str, newOrder)))
