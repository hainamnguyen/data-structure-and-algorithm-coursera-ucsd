# Uses python3
def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (right + left)//2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

if __name__ == '__main__':
    data = [5 ,1 ,5 ,8 ,12 ,13 ,5 , 8, 1, 23, 1, 11]
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    a.sort()
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')