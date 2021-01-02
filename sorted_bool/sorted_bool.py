# Put your code here
def sorty(lIst, n):
    if n == len(lIst) - 1:
        return True
    elif lIst[n] > lIst[n+1]:
        return False
    else:
        return sorty(lIst, n+1)

def isSorted(l1st):
    if len(l1st) <2:
        return True
    else:
        return sorty(l1st , 0)
    
        
        
# A main for testing your code
def main():
    lyst = []
    print(isSorted(lyst))
    lyst = [1]
    print(isSorted(lyst))
    lyst = list(range(10))
    print(isSorted(lyst))
    lyst[9] = 3
    print(isSorted(lyst))

if __name__ == "__main__":
    main()