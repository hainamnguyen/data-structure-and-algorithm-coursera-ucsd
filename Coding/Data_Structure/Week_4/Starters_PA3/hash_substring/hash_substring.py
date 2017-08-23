# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    result = []
    pHash = _hash_func(pattern)
    #print(pHash)
    P = len(pattern)
    H = _pre_hash(text,P)
    #print(H)
    for i in range(0, len(text) - P + 1):
        if pHash != H[i]:
            continue
        #print(text[i:i + P],pattern)
        if text[i:i + P ] == pattern:
            result.append(i)
    return result
def _hash_func(s):
    multiplier = 263
    prime = 10000019
    ans = 0
    for c in reversed(s):
         #print(c,s)
        ans = (ans * multiplier + ord(c)) % prime
    return ans
def _pre_hash(text,lenOfWord):
    multiplier = 263
    prime = 10000019
    lenOfText = len(text)
    H = [0]*(lenOfText - lenOfWord + 1)
    H[lenOfText - lenOfWord] = _hash_func(text[lenOfText - lenOfWord:])
    y = 1
    for i in range(1, lenOfWord +1):
        y = (y*multiplier)%prime
    for i in range(lenOfText - lenOfWord - 1, -1, -1):
        H[i] = ((multiplier *H[i+1] + ord(text[i]) - y*ord(text[i+lenOfWord]))% prime)
    return H
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

