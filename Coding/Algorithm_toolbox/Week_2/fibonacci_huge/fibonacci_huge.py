# Uses python3
def get_fibonacci_huge(n, m):
    #print(get_pisano(m))
    n = n % get_pisano(m)
    #print(n)
    if n <= 1:
        return n
    
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
    if current == 0:
        return m - 1
    
    return current 

def get_pisano(n):
    c = [1, 1]
    a = []
    while(c in a)<1%n:
        a += [c]
        c = [c[1], sum(c) % n]
    module = (len(a) or 1)
    return module

if __name__ == '__main__':
    #n, m = map(int, input().split())
    print(get_fibonacci_huge(10, 20))

