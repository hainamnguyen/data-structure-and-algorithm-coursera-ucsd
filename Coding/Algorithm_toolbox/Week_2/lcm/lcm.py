# Uses python3
import sys

# Uses python3
def GCD(a,b):
    if b > a:
        print(a,b)
        return GCD(b,a)
    r = a%b
    if r == 0:
        return b
    
    return GCD(b,r)

def LCM(x, y):
    if x >= y:
        return int(x*y/GCD(y,x))
    else:
        return int(x*y/GCD(x,y))
        
if __name__ == '__main__':
    a, b = map(int, input().split())
    print(LCM(a, b))

