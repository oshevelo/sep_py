def get_value_to_calculate():
    num = input('Please enter a value: ')
    return num


def get_math_operation():
    op = input('Please enter a math operation: ')
    return op


def print_calcul_result(result):
    print('RESULT = ', result)


def get_dditinal_math():
    op_or_skip = input(
        'Please enter more math operation or ENTER to calulate: ')
    return op_or_skip


def get_str_expression_to_calc():
    str_expression = input(
        'Please enter expresion to calculate: ')
    return str_expression


def get_date_value(date_value):
    date_value = input(f'Please enter "{date_value}" from now: ')
    return int(date_value) if date_value != '' else date_value


def date_calculator_greeting():
    print('Enter day month year to calculate or skip')
