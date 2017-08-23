#Uses python3
def max_dot_product(a, b):
    #write your code here
    return sum(sorted(a)[i] * sorted(b)[i] for i in range(len(a)))
if __name__ == '__main__':
    #data = list(map(int, input().split()))
    print(max_dot_product([1, 3, -5], [-2, 4, 1]))
    
