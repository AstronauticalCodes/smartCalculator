brackDict = {'(':[], ')':[]}

expr = list(input().replace(' ', ''))
print(expr)

def bracketFinder():
    global expr
    global brackDict

    for index, char in enumerate(expr):
        if char == '(':
            brackDict['('].append(index)
        elif char == ')':
            brackDict[')'].append(index)

    print(brackDict)

bracketFinder()

brackSolverDict = {}

print(len(brackDict['(']), len(brackDict[')']))
if len(brackDict['(']) != len(brackDict[')']):
    print('Error')

if len(brackDict['(']) == 1:
    dels = ''.join(expr[brackDict['('][0]:(brackDict[')'][0] + 1)])
    brackSolverDict.update({''.join(expr).index(dels): dels})

    print(brackSolverDict)

elif len(brackDict['(']) >= 1:
    bracCount = 0
    bracCountList = []
    searchBracCloseIndex = 0
    bracSolveDict = {}

    newExpr = expr.copy()
    for x in range(10):
        for index, char in enumerate(newExpr):
            if char == '(':
                print(newExpr)
                bracCount += 1
                searchBracCloseIndex = index
            elif char == ')' and bracCount >= 1:
                print('hello')
                dels = newExpr[searchBracCloseIndex: (index + 1)]
                brackSolverDict.update({(''.join(expr).index(''.join(dels))): dels})
                print('bracketSolverDict:', brackSolverDict)
                del dels
                bracCountList.append(bracCount)
                break
        bracCount = 0

    print('opening brackets:', max(bracCountList))



    lastBrac = -1
    initialBracCount = max(bracCountList)
    extraBrac = 0

    print('expr:', expr)
    print('max of bracCountList:', max(bracCountList))
    if max(bracCountList) > 1:
        for x in range(max(bracCountList)):

            ind = ''.join(expr).find(')', (searchBracCloseIndex + 1))

            if ind != -1:
                print('Start searching close brackets from:', (searchBracCloseIndex + 1))

                print(expr[(searchBracCloseIndex + 1):ind])

                for index, char in enumerate(expr[(searchBracCloseIndex + 1):ind]):
                    if char == '(':
                        bracCount += 1
                        extraBrac += 1

                searchBracCloseIndex = ind
                print(x, bracCount, ind)
                if x == initialBracCount - 1:
                    lastBrac = ind
        print(extraBrac)
        print(lastBrac)
        if extraBrac >= 0:
            for x in range(extraBrac):
                try:
                    closeBracIndex = expr.index(')', (lastBrac + 1))
                    lastBrac = closeBracIndex

                except ValueError:
                    pass
                print('the very last bracket:', closeBracIndex)


        print('last closing bracket:', searchBracCloseIndex)
        print(len(expr))

# elif max()

# if farBrac not closed and another '(' started, then add + 1 to the farBrac count
