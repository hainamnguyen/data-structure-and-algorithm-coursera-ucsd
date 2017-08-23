# python3
import sys

def InverseBWT(bwt):
    # write your code here
    lenOfText = len(bwt)
    textEdit = list(enumerate(bwt))
    firstColumn = sorted(textEdit, key=lambda x: x[1], reverse=False)
    result = firstColumn[0][1]
    reference_symbol = firstColumn[0]
    invere_dict = {textEdit[i]: firstColumn[i] for i in range(lenOfText)}
    #print(firstColumn)
    #print(textEdit)
    #print(invere_dict)
    while len(result) < lenOfText:
        reference_symbol = invere_dict[reference_symbol]
        result += reference_symbol[1]
        #print(result)
    #print(result)
    return result[1:] + result[0]

if __name__ == '__main__':
    #bwt = sys.stdin.readline().strip()
    bwt = input()
    print(InverseBWT(bwt))
 
