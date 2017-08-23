# Uses python3
def edit_distance(s, t):
    length_of_s = len(s)
    length_of_t = len(t)
    distance = [[0 for x in range(length_of_s+1)] for y in range(1+length_of_t)]
    distance[0] = [i for i in range(length_of_s+1)]
    for i in range(length_of_t +1):
                distance[i][0] = i
    #print(distance)   
    for i in range(1, length_of_t + 1):
        for j in range(1, length_of_s + 1):
            #print(i,j)
            if t[i-1] != s[j-1]:
                distance[i][j] = min(distance[i-1][j-1]+1, \
                               distance[i-1][j]+1, \
                               distance[i][j-1]+1,)
            else:
                distance[i][j] = min(distance[i-1][j-1], \
                               distance[i-1][j]+1, \
                               distance[i][j-1]+1,)    
    return distance[length_of_t][length_of_s]
if __name__ == "__main__":
    print(edit_distance(input(), input()))
