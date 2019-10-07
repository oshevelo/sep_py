def calc (a, b, operat):

    if operat == '+':
        return a + b

    elif operat == '-':
        return a - b

    elif operat == '*':
        return a * b

    elif operat == '/':
        if b == 0:
            print('Error, ділити на 0 не можна')
            exit()

        return a / b

    else:
        print('Error, будь ласка введіть правильно операцію (+,-,*,/)')
        exit()

print('ready')

