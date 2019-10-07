def calc(a, b):
    if operation == '+':
        return value1 + value2

    elif operation == '-':
        return value1 - value2

    elif operation == '*':
        return value1 * value2

    elif operation == '/':

        if value2 == 0:
            print('Error, ділити на 0 неможна')
            exit()

        return value1 / value2

    else:
        print('Error, будь ласка введіть правильно операцію (+,-,*,/)')

try:
    value1 = float(input('enter first number'))
except ValueError:
    print('Error, будь ласка переконайтеся, що ви написали коректно цифри і цифри з десятими (1.2) ')
    exit()

operation = input('enter operation: (+,-,*,/)')

try:
    value2 = float(input('enter second number'))

except ValueError:
    print('Будь ласка переконайтеся, що ви написали коректно цифри і цифри з десятими (1.2) ')
    exit()


result = calc(a=value1, b=value2)
print(result)



def calc (a, b):

    if operation == '+':
        return a + b

    elif operation == '-':
        return a - b

    elif operation == '*':
        return a * b

    elif operation == '/':
        if value1 == 0:
            print('Error, ділити на 0 неможна')
            exit()

        return a / b


    else:
        print('Error, будь ласка введіть правильно операцію (+,-,*,/)')
        exit()

try:
    value = float(input('enter first number'))
except ValueError:
    print('Error, будь ласка переконайтеся, що ви ввели коректно цифри і цифри з десятими (1.2) ')
    exit()
operation = input('enter operation (+,-,*,/)')
result = value

while True:
    try:
        value1 = float(input('enter number'))
    except ValueError:
        print('Error, будь ласка переконайтеся, що ви ввели коректно цифри і цифри з десятими (1.2) ')
        exit()
    result = calc (a = result, b = value1)
    print(result)
    operation = input('enter operation (+,-,*,/) or result')
    if operation == 'result':
        print(result)
        break



s='2+2*1.2'

from simpleeval import simple_eval
c=simple_eval((input('write example')))
print(c)
print(type(c))