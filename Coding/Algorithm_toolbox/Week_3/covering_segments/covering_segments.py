# Uses python3
from collections import namedtuple
Segment = namedtuple('Segment', 'start end') 
#print(Segment)
def optimal_points(segments):
    points = []
    #write your code here
    for s in segments:
        #print(s[1])
            points.append(s[1])
            att = s[1]
            for i in segments:
                if att >= i[0]:
                    segments.remove(i)
    #print(segments)
    return points

if __name__ == '__main__':
    #input = sys.stdin.read()
    raw_data = '4 4 5 1 3 2 6 5 6'
    n, *data = map(int, raw_data.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    segments = sorted(segments,key=lambda x: x[1])
    print(segments)
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
