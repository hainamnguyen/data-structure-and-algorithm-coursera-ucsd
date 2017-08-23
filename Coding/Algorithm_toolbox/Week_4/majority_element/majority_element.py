# Uses python3
import sys
from collections import Counter
def get_majority_element(a, left, right):
    t = Counter(a).most_common(n)
    if t[0][1] > right/2:
        return 0
    else:
        return -1
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #n, *a = list(map(int, input().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
