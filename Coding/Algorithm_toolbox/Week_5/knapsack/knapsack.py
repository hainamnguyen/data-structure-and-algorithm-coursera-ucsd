# Uses python3
import sys

def optimal_weight(W, w):
    number_of_items = len(w)
    # write your code here
    result = [[0 for x in range(W +1)] for y in range(number_of_items + 1)]
    #print(result)
    
    for i in range(1, number_of_items+1):
        for j in range(1, W + 1):
            result[i][j] = result[i -1][j]
            if w[i-1] <= j:
                val_temp = result[i-1][j-w[i-1]] + w[i-1]
                if val_temp > result[i][j]:
                    result[i][j] = val_temp
            #print(i,j,result[i][j])
    return result[number_of_items][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    #W, n, *w = list(map(int, input().split()))
    print(optimal_weight(W, w))
