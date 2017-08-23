# Uses python3
def GCD(a,b):
    if b > a:
        print(a,b)
        return GCD(b,a)
    r = a%b
    if r == 0:
        return b
    
    return GCD(b,r)

if __name__ == "__main__":
    print(GCD(239,749))
