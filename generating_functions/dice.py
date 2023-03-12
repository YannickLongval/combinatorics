# This script was inspired by the Sicherman Dice, and how the values on an n-sided die can be changed,
# but still produce the same probabilities when rolling 2 n-sided dice 
# (https://en.wikipedia.org/wiki/Sicherman_dice for more info on Sicheman Dice).
# The script takes an n-sided die (represents by NUM_SIDES), and determines the different values on each
# die that result in the same probabilities as 2 regular, n-sided dice. The dice are represented as 
# generating functions, when the exponent is the value of the side, and the coefficient is homogeneous_order
# sides have that particular value.

from sympy import *
from itertools import *

NUM_SIDES = 7 # how many sides on the die

def convert_factored_string(lst):
    if(len(lst) == 0):
        return "0"
    lst = [i for i in lst]
    lst[0] = '(' + lst[0]
    lst[-1] = lst[-1] + ')'
    return ")*(".join(lst)

def get_complement(lstBig, lstSmall):
    lstBig = lstBig[:]
    for f in lstSmall:
        lstBig.remove(f)

    return lstBig

def isDup(die, lst):
    for d in lst:
        dup = True
        for e in die:
            if(d.count(e) != die.count(e)):
                dup = False
        for e in d:
            if(die.count(e) != d.count(e)):
                dup = False
        if(dup):
            return True
    return 

x = symbols('x')

lst = [str(x**i) for i in range(1, NUM_SIDES+1, 1)] # initializes the coefficients of the polynomial
p = " + ".join(lst) # join terms with addition 
p = eval(p) # cast string to expression

fact = factor(p) # factor polynolmial

print(fact)

lstFactors = str(fact).replace(")", "").split("*(")
lstVals = [int(eval(f).evalf(subs={x:1})) for f in lstFactors]

lstFactorsNoX = lstFactors[1:] * 2
lstDie = []
for L in range(len(lstFactorsNoX)//2 + 1):
    for subset in combinations(lstFactorsNoX, L):
        if(convert_factored_string(subset) != "0"):
            if(int(eval(convert_factored_string(subset)).evalf(subs={x:1})) == NUM_SIDES):
                lstDie.append(list(subset))

uniqueDie = []
dicePairs = []
for die in lstDie:
    if(not isDup(die, uniqueDie)):
        dicePairs.append((die, get_complement(lstFactorsNoX, die)))
        uniqueDie.append(die)
        uniqueDie.append(get_complement(lstFactorsNoX, die))

validPairs = []

for dice in dicePairs:
    d1 = str(eval("x*" + convert_factored_string(dice[0])).expand())
    d2 = str(eval("x*" + convert_factored_string(dice[1])).expand())
    if(not("-" in d1 or "-" in d2)):
        validPairs.append([d1, d2])


for dice in validPairs:
    print("1st Die: " + dice[0] + "\n2nd Die: " + dice[1] + "\n\n")
