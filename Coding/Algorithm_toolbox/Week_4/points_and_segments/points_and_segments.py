# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    new_starts = [[i, 1] for i in starts]
    new_ends = [[i, 3] for i in ends]
    new_points = [[points[i],2, i] for i in range(len(points))]
    sequences = sorted(new_starts + new_ends + new_points)
    number = 0
    
    for i in sequences:
        if i[1] == 1:
            number += 1
        elif i[1] == 3:
            number -= 1
        else:
            cnt[i[2]] = number
    return cnt
def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = list(map(int, input().split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #print(starts)
    #print(ends)
    #print(points)
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    #print(cnt)
    for x in cnt:
        print(x, end=' ')
