def createCombinations(n):
    if n==0:
        return []
    if n==1:
        return [[1], [0]]
    lst = createCombinations(n-1)
    tmpLst = []
    for comb in lst:
        tmpLst.append(comb + [1])
        tmpLst.append(comb + [0])
    return tmpLst

def getSize(lst1):
    return sum(lst1)

n = input("Enter an exponent: ")

print("Computing (x+y)^" + n)

lstComb = createCombinations(int(n))

print(lstComb)

sumLst = [sum(lst) for lst in lstComb]

print(sumLst)

coeffLst = []

for i in range(int(n)+1):
    coeffLst.append(sumLst.count(i))

termsLst = []

for i in range(int(n)+1):
    termsLst.append(str(coeffLst[i]) + "x^" + str(int(n)-i) + "y^" + str(i))

print(" + ".join(termsLst))