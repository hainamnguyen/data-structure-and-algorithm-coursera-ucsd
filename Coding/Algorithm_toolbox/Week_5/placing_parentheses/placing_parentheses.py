# Uses python3
import sys

def get_maximum_value(dataset, start, end, Min_matrix, Max_matrix):
    #write your code here
    #print(Min_matrix)
    #print(Max_matrix)
    #print(start, end)
    min_temp = sys.maxsize
    max_temp = -sys.maxsize
    for i in range(start,end):
        #print(Min_matrix)
        #print(Max_matrix)
        #print(i)
        #print(Min_matrix[start][i], Min_matrix[i+1][end],str(Min_matrix[start][i]) + dataset[i+1] + str(Min_matrix[i+2][end]))
        if 2*i+1 < len(dataset):
            midle = dataset[2*i+1]
        else:
            midle = ''
        st = eval(str(Min_matrix[start][i]) + midle + str(Min_matrix[i+1][end]))
        nd = eval(str(Min_matrix[start][i]) + midle + str(Max_matrix[i+1][end]))
        rd = eval(str(Max_matrix[start][i]) + midle + str(Max_matrix[i+1][end]))
        th = eval(str(Max_matrix[start][i]) + midle + str(Min_matrix[i+1][end]))

        #print(min_temp,st, nd, rd, th)
        #print(max_temp,st, nd, rd, th)
        min_temp = min(min_temp,st, nd, rd, th)
        max_temp = max(max_temp,st, nd, rd, th)
        #print(min_temp,max_temp)
    return [min_temp,max_temp]

def placing_parentheses(dataset):
    #print(dataset)
    lenofstring = len(dataset)
    numberofarguments = int((lenofstring + 1)/2)
    min_ = [[0 for x in range(numberofarguments)] for y in range(numberofarguments)]
    max_ = [[0 for x in range(numberofarguments)] for y in range(numberofarguments)]
    for i in range(0, numberofarguments):
        min_[i][i] = int(dataset[2*i])
        max_[i][i] = int(dataset[2*i])
    #print(min_,max_)
    for i in range(1, numberofarguments):
        for j in range(0, numberofarguments - i):
            s = i + j
            [min_[j][s], max_[j][s]] = get_maximum_value(dataset, j, s, min_, max_)
            #print(min_,max_)
    return max_[0][numberofarguments - 1]
    
if __name__ == "__main__":
    print(placing_parentheses(input()))
