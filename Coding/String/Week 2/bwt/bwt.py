# python3
import sys

def BWT(text):
    lenOfText = len(text)
    bwtMatrix = []
    result = str()
    for i in range(lenOfText):
        bwtMatrix.append(text[i:] + text[:i])
    bwtMatrix.sort()
    for i in range(lenOfText):
        #print(bwtMatrix[i][lenOfText-1])
        result += bwtMatrix[i][lenOfText-1]
    return result

if __name__ == '__main__':
    #text = sys.stdin.readline().strip()
    text = input()
    print(BWT(text))
