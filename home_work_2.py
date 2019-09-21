'''
Calculator operates only with integer numbers
Can do: addition, subtraction, division, multiplication
Aplication modes: simple, count3, string_mode
'''

# value1 = int(input('please enter value1: '))
# value2 = int(input('please enter value2: '))
# operation = input('please enter operation: ')
import ast


def my_calc_simple(value1, value2, operation):
    value1 = int(value1)
    value2 = int(value2)
    if operation == '+':
        result = value1 + value2
    elif operation == '-':
        result = value1 - value2
    elif operation == '*':
        result = value1 * value2
    elif operation == '**':
        result = value1 ** value2
    elif operation == '/':
        result = value1 / value2
    else:
        ValueError('Unknown math operational')
    return result


def count3(value1, value2, value3, operation1, operation2):
    if operation2 in ['*', '/']:
        calculated_value = my_calc_simple(value2, value3, operation2)
        result = my_calc_simple(value1, calculated_value, operation1)
    else:
        calculated_value = my_calc_simple(value1, value2, operation1)
        result = my_calc_simple(calculated_value, value3, operation2)
    return result


def string_calculation(calc_str):
    def get_math_op(op):
        if type(op) is ast.Add:
            operatin = '+'
        elif type(op) is ast.Mult:
            operatin = '*'
        elif type(op) is ast.Div:
            operatin = '/'
        elif type(op) is ast.Sub:
            operatin = '-'
        else:
            ValueError('Unknown math operational')
        return operatin

    try:
        ast.literal_eval(calc_str)
    except ValueError:
        code = ast.parse(calc_str)
        if hasattr(code.body[0].value.left, 'n'):
            value1 = code.body[0].value.left.n
            value2 = code.body[0].value.right.left.n
            value3 = code.body[0].value.right.right.n
            operatin2 = code.body[0].value.op
            operatin1 = code.body[0].value.right.op
        else:
            value1 = code.body[0].value.left.left.n
            value2 = code.body[0].value.left.right.n
            value3 = code.body[0].value.right.n
            operatin2 = code.body[0].value.op
            operatin1 = code.body[0].value.left.op

        operatin1 = get_math_op(operatin1)
        operatin2 = get_math_op(operatin2)
        result = count3(value1, value2, value3, operatin1, operatin2)
        return result


# result = my_calc(value1, value2, operation)
# print('The result is: ', result)

# tests
# simple
assert my_calc_simple('2', '2', '+') == 4
assert my_calc_simple('3', '1', '-') == 2
assert my_calc_simple('2', '3', '*') == 6
assert my_calc_simple('6', '2', '/') == 3
assert my_calc_simple('3', '2', '**') == 9
# count 3
assert count3('1', '2', '3', '+', '+')==6
assert count3('10', '20', '30', '+', '-')==0
assert count3('10', '1', '2', '-', '*')==8
# string_mode
assert string_calculation('2+2*2') == 6
assert string_calculation('4/2+1') == 3
