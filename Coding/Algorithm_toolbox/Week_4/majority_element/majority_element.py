# Uses python3
from collections import Counter
def get_majority_element(a, left, right):
    t = Counter(a).most_common()
    if t[0][1] > right/2:
        return 0
    else:
        return -1
if __name__ == '__main__':
    n = 5
    a = [2, 3, 9, 2, 2]
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
