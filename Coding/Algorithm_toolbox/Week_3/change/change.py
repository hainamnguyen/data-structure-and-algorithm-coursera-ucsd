# Uses python3
import sys

def get_change(m):
    #write your code here
    sub_number = [10, 5, 1]
    quantumn = 0
    for i in sub_number:
        while m >= i:
            m -= i
            quantumn += 1
            
    return quantumn

if __name__ == '__main__':
    #m = int(input())
    m = int(sys.stdin.read())
    print(get_change(m))
