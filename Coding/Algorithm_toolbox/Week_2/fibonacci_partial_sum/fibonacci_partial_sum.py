# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    b = fibonacci_sum_naive(to)  
    if from_ == 0:
        return b
    a = fibonacci_sum_naive(from_ - 1)
    if b >= a:
        return b - a
    else:
        return b + 10 - a
def fibonacci_sum_naive(n):
    if n <= 1:
        return n
        
    n = (n + 2) % 60
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10
    if current == 0:
        return 9
    return (current - 1)

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))

