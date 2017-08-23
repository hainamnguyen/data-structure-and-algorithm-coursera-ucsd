# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  sufiixList = []
  for i in range(len(text)):
    sufiixList.append([text[i::],i])
  #print(sufiixList)
  sufiixList.sort()
  result = [i[1] for i in sufiixList]
  # Implement this function yourself
  return result


if __name__ == '__main__':
  text = input()
  print(" ".join(map(str, build_suffix_array(text))))
