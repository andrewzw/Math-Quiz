def calculateanswer(lhs,rhs,operator):
    if (operator == '-'):
        return lhs - rhs
    if (operator == '*'):
        return lhs * rhs
    if (operator == '/'):
        return lhs / rhs
    if (operator == '+'):
        return lhs + rhs
    if (operator == '^'):
        return lhs ** rhs
    raise Exception('Unknown Operator')

print(calculateanswer(8,2,'+'))
print(calculateanswer(8,2,'-'))
print(calculateanswer(8,2,'*'))
print(calculateanswer(8,2,'/'))
print(calculateanswer(8,2,'^'))

from random import randint
def generatequestion():
    ops = '/*+-'
    opindex = randint(0,len(ops)-1)
    operator = ops[opindex]
    lhs = randint(0,10)
    rhs = randint(0,10)
    while(rhs == 0 and operator == '/'):
        rhs = randint(0,10)
    return lhs,rhs,operator

for i in range(10):
    results = generatequestion()
    answer = calculateanswer(results[0],results[1],results[2])
    print('{0}{1}{2}{3}'.format(results[0],results[1],results[2],answer))