# Uses python3
import sys
def msort4(x):
    number_of_inversions = 0
    result = []
    if len(x) <= 1:
        return [0] + x
    mid = int(len(x)/2)
    y = msort4(x[:mid])
    z = msort4(x[mid:])
    i = 1
    j = 1
    while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                number_of_inversions += (len(y)-i)
                j += 1
            else:
                result.append(y[i])
                i += 1
    result += y[i:]
    result += z[j:]
    #print(result)
    number_of_inversions = number_of_inversions + y[0] + z[0]
    result = [number_of_inversions] + result
    #print(result)
    return result
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #n, *a = list(map(int, input().split()))
    print(msort4(a)[0])
