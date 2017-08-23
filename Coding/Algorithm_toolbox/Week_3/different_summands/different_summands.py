# Uses python3
def optimal_summands(n):
    number = 1
    while number*(number+1)/2 <= n:
        number += 1
    summands = [i for i in range(1, number -1)]
    summands.append(int(n - (number-1)*(number-2)/2))

    return summands

if __name__ == '__main__':
    summands = optimal_summands(16)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
