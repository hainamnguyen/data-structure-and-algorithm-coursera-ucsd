# Uses python3
def calc_fib(n):
    f = []
    f.append(0)
    f.append(1)
    
    if (n <= 1):
        return n
    for i in range(2,n+1):
        f.append(f[i-1] + f[i-2])
        
    return f[n]

if __name__ == "__main__":
    n = int(input())
    print(calc_fib(n))
