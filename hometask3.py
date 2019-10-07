from big_home_module.module_simple_calc import calc
from big_home_module.module_pro_calc import calc as pro_calc

# simple_calc
try:
    value1 = float(input('enter first number'))
except ValueError:
    print('Error, будь ласка переконайтеся, що ви написали коректно цифри і цифри з десятими (1.2) ')
    exit()

operation = input('enter operation: (+,-,*,/)')

try:
    value2 = float(input('enter second number'))

except ValueError:
    print('Error, будь ласка переконайтеся, що ви написали коректно цифри і цифри з десятими (1.2)  ')
    exit()


result = calc(a=value1, b=value2, operat = operation)
print(result)

def check(a):
    if type(a) == float:
        return True
    else:
        return False

print(check(result))

# обчислення виразу
s = 2*3+result
print(s)

# pro_calc
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
    result = pro_calc (a = result, b = value1, operat = operation )
    print(result)
    operation = input('enter operation (+,-,*,/) or result')
    if operation == 'result':
        print(result)
        break