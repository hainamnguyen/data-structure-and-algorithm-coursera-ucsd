# python3
import sys


def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  lengthOfText = len(text)
  trie = [[] for i in range(lengthOfText)]
  for i in range(lengthOfText):
    brandEnd = i
    k = 0
    while k < i and text[i] != text[k]:
      k += 1
    if k == i:
      trie[i].append([i, lengthOfText - i, i])
      continue
    else:
      brandStart = k
      while text[k] == text[brandEnd]:
        brandEnd += 1
        k += 1
    #print(i,k, brandStart, brandEnd)
    #print(trie)
    for j in range(k,lengthOfText):
      m = 0
      if [brandStart, k - brandStart] in trie[j] and trie[j].index([brandStart, k - brandStart]) == m:
        m += 1
        #print(trie[j], brandStart, k - brandStart, j)
        k = j + k
        while text[brandEnd] == text[k] and brandEnd != k:
          #print(brandEnd, k)
          brandEnd += 1
          k += 1
          brandStart = j - brandStart
          #print(brandEnd, k)

    for check in range(len(trie[brandStart])):
      if trie[brandStart][check][0] <  k:
        if trie[brandStart][check][1] <= k - trie[brandStart][check][0] :
          trie[i].append(trie[brandStart][check])
        else:
          t= k - trie[brandStart][check][0]
          if len(trie[brandStart][check]) == 3:
            trie[brandStart].append([k, trie[brandStart][check][1] - t, trie[brandStart][check].pop(2)])
            
          else:
            trie[brandStart].append([k, trie[brandStart][check][1] - t])
          trie[brandStart][check][1] = t
          trie[i].append(trie[brandStart][check])
          
    trie[i].append([brandEnd, lengthOfText - brandEnd, i])
  for i in trie:
    print(i)
  setOfResult = set()
  result = []
  for i in trie:
    for j in range(len(i)):
      if len(i[j]) == 2:
        setOfResult.add((i[j][0],i[j][1],j))
      else:
        setOfResult.add((i[j][0],i[j][1],i[j][2],j))
  #print(setOfResult)
  for i in setOfResult:
    result.append(text[i[0]:i[1] + i[0]])
  # Implement this function yourself
  return result

if __name__ == '__main__':
  #text = sys.stdin.readline().strip()
  text = input().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))
