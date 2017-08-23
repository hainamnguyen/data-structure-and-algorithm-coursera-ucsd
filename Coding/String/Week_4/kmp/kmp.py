# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  # Implement this function yourself
  text = pattern + text
  prefixArray = []
  prefixArray.append(0)
  border = 0
  lenOfPattern = len(pattern)
  for i in range(1, len(text)):
    while border > 0 and text[i] != text[border]:
      print('wow')
      #print(1, border, prefixArray[border - 1])
      border = prefixArray[border - 1]
      #print(2, border, text[border])
      #print(3, text[i], text[border])
    if text[i] == text[border]:
      border = border + 1
    else:
      border = 0
    prefixArray.append(border)
    if i > lenOfPattern and border == lenOfPattern:
      result.append(i - 2*lenOfPattern)
  return result

if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  #pattern = input()
  #text = input()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))


