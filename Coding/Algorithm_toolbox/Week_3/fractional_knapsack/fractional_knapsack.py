# Uses python3
def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    worth = [[values[i]/weights[i], values[i], weights[i]] for i in range(len(values))]
    worth.sort(reverse = True)
    #print(worth)
    for i in range(len(worth)+1):
        if capacity == 0 or i == len(worth):
            return value
        value_tmp = min(capacity, worth[i][2])
        capacity -= value_tmp
        value += worth[i][0]*value_tmp
        

if __name__ == "__main__":
    #data = list(map(int, input().split()))
    data = [3, 50, 60, 20, 100, 50, 120, 30]
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
