# python3
import sys


def PreprocessBWT(bwt):
  
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  # Implement this function yourself
  starts = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0, '$': 0}
  occ_count_before = {'A' : [0], 'C' : [0], 'G' : [0], 'T' : [0], '$' : [0]}
  sortedBwt = sorted(bwt)
  for i in starts:
    try:
      starts[i] = sortedBwt.index(i)
    except:
      starts[i] = float('inf')
      continue
    count_before = 0
    for j in range(1, len(bwt) + 1):
      if i == bwt[j-1]:
        count_before += 1
      occ_count_before[i].append(count_before)
  #print(starts)
  #print(occ_count_before)
  return starts, occ_count_before


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  # Implement this function yourself
  pattern = list(pattern[::-1])
  top = 0
  bottom = len(bwt) - 1
  while top <= bottom:
    if len(pattern) != 0:
      symbol = pattern.pop(0)
      #print(symbol)
      if symbol in bwt[top : bottom +1]:
        top = starts[symbol] + occ_counts_before[symbol][top]
        bottom = starts[symbol] + occ_counts_before[symbol][bottom + 1] -1
      else:
        return 0
    else:
      return bottom - top + 1
     


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  #bwt = input()
  #pattern_count = int(input())
  #patterns = input().strip().split()
  
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
