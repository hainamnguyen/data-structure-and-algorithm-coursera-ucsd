#Uses python3
def largest_number(in_put):
    #write your code here
    #print(in_put)
    a = [[in_put[x], x] for x in range(len(in_put))]
    print(a)
    for x in range(len(a)):
        if len(str(a[x][0])) == 3:
            a[x][0] = a[x][0]*10 + int(str(a[x][0])[0])
        elif len(str(a[x][0])) == 2:
            a[x][0] = a[x][0]*100 + int(str(a[x][0])[0])*11
        elif len(str(a[x][0])) == 1:
            a[x][0] = a[x][0]*1111
    
    a.sort(reverse=True)
    print(a)
    order = [number_order[1] for number_order in a]
    out_put = "".join([str(in_put[k]) for k in order])
    
    return out_put

if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    data = list(map(int, '3 234 235 23 39 92'.split()))
    a = data[1:]
    print(largest_number(a))
    
