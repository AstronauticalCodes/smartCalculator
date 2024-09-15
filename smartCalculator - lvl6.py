class InvalidExpressionError(Exception):
    def __str__(self):
        return 'Invalid expression'


class UnknownCommandError(Exception):
    def __str__(self):
        return 'Unknown command'


class InvalidAssignmentError(Exception):
    def __str__(self):
        return 'Invalid assignment'


class UnknownVariableError(Exception):
    def __str__(self):
        return 'Unknown variable'


class InvalidIndentifierError(Exception):
    def __str__(self):
        return 'Invalid identifier'


# expr = list(input().replace(' ', ''))
expr = ' '
next = None
varDict = {}
delIndex = [0]


def takeInput():
    global expr

    expr = list(input().replace(' ', ''))

def checkError():
    global expr
    global next
    global joint

    try:
        if len(expr) > 0:
            if expr[-1] in ['+', '-']:
                next = True
                raise InvalidExpressionError
            elif ''.join(expr) not in ['/exit', '/help'] and ''.join(expr)[0] == '/':
                next = True
                raise UnknownCommandError
            elif expr.count('=') > 1:
                next = True
                raise InvalidAssignmentError
            # elif ''.join(expr).isalpha():
            #
            #     next = True
            #     raise InvalidExpressionError
            # else:
            #     if ''.join(expr)[0] != '/':
            #         for char in expr:
            #             if char in 'abcdefghijklmnopqrstuvqxyz':
            #                 next = True
            #                 raise InvalidExpressionError

    except InvalidExpressionError as error:
        print(error)
    except UnknownCommandError as error:
        print(error)
    except InvalidAssignmentError as error:
        print(error)


def variableAssigner():
    global expr
    global varDict

    if expr.count('=') == 1:
        equalIndex = expr.index('=')
        var = ''.join(expr[:equalIndex])
        val = ''.join(expr[(equalIndex + 1):])
        try:
            if var.isalpha():
                if val in varDict:
                    varDict.update({var:varDict[val]})
                elif val.isnumeric():
                    varDict.update({var:val})
                else:
                    del expr[:equalIndex]
                    expr.insert(0, var)
                    del expr[2:]
                    expr.insert(2, val)
                    next = True
                    raise InvalidAssignmentError
            else:
                next = True
                raise InvalidIndentifierError

        except InvalidAssignmentError as error:
            print(error)
        except InvalidIndentifierError as error:
            print(error)


def varFinder():
    global expr

    for x in range(20):
        for index, char in enumerate(expr):
            if index != (len(expr) - 1):
                if char.isalpha() and expr[index + 1].isalpha():
                    var = char + expr[index + 1]
                    del expr[index:(index + 2)]
                    expr.insert(index, var)

def simplifier():
    global expr
    global delIndex

    for x in range(25):
        for index, char in enumerate(expr):
            if index != (len(expr) - 1):
                if char == '-' and expr[index + 1] == '-':
                    del expr[index:(index + 2)]
                    expr.insert(index, '+')
                elif (char == '-' and expr[index + 1] == '+') or (char == '+' and expr[index + 1] == '-'):
                    del expr[index: (index + 2)]
                    expr.insert(index, '-')
                elif char == '+' and expr[index + 1] == '+':
                    del expr[index: (index + 2)]
                    expr.insert(index, '+')
                elif char.isnumeric() and expr[index + 1].isnumeric():
                    newNum = char + expr[index + 1]
                    del expr[index: (index + 2)]
                    expr.insert(index, newNum)


def addition(a, b):
    return str(a + b)


def subtraction(a, b):
    return str(a - b)


def solver():
    global expr

    if expr[0] == '-' and expr[1].isnumeric():
        newInt = expr[0] + expr[1]
        del expr[0: 2]
        expr.insert(0, newInt)
    elif expr[0] == '+':
        del expr[0]

    for x in range(10):
        for index, char in enumerate(expr):
            if index != (len(expr) - 1):
                if char in ['+', '-']:
                    lowVal = expr[index - 1]
                    upVal = expr[index + 1]
                    if lowVal in varDict:
                        lowVal = varDict.get(lowVal)
                    if upVal in varDict:
                        upVal = varDict.get(upVal)
                    if char == '+':
                        result = addition(int(lowVal), int(upVal))
                    else:
                        result = subtraction(int(lowVal), int(upVal))
                    del expr[(index - 1): (index + 2)]
                    expr.insert((index -1), result)
                    break
    # print(expr)
# while True:
#     takeInput()
#     checkError()
#     if not next:
#         if ''.join(expr) not in ['/exit', '/help'] and len(expr) > 0:
#             simplifier()
#             solver()
#             print(''.join(expr))
#         elif ''.join(expr) == '/help':
#             print()
#         elif len(expr) == 0:
#             continue
#         else:
#             print('Bye!')
#             exit()
#     next = None


def calculator():
    global expr
    global varDict
    global next

    if '=' in expr:
        variableAssigner()
    elif '+' in expr or '-' in expr:
        simplifier()
        varFinder()
        solver()
        print(''.join(expr))
    elif ''.join(expr).isalpha():
        try:
            if ''.join(expr) in varDict:
                print(varDict.get(''.join(expr)))
            else:
                raise UnknownVariableError
        except UnknownVariableError as error:
            print(error)
    elif ''.join(expr).isnumeric():
        print(''.join(expr))
    elif ''.join(expr) == '/help':
        print('This is calculator!')
    elif ''.join(expr) == '/exit':
        print('Bye!')
        exit()
    elif ''.join(expr).isalnum():
        print('Invalid identifier')


while True:
    takeInput()
    checkError()
    if not next:
        calculator()
    next = None
# checkError()
