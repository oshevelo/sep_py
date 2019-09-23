import home_work_3.calculator_interface as calc
from home_work_3.calculations.date_calculator import cal_date_incr_from_today
from home_work_3.calculations.str_calculator import calculate_str_expresion


def my_str_calculator():
    str_expression = calc.get_str_expression_to_calc()
    result = calculate_str_expresion(str_expression)
    calc.print_calcul_result(result)


def my_value_calculator():
    value1 = calc.get_value_to_calculate()
    op1 = calc.get_math_operation()
    value2 = calc.get_value_to_calculate()
    op2 = calc.get_dditinal_math()
    if op2:
        value3 = calc.get_value_to_calculate()
        str_expresion = value1 + op1 + value2 + op2 + value3
    else:
        str_expresion = value1 + op1 + value2

    result = calculate_str_expresion(str_expresion)
    calc.print_calcul_result(result)


def my_date_calculator():
    calc.date_calculator_greeting()
    date_from_now = {}
    date_from_now['days'] = calc.get_date_value('days')
    date_from_now['months'] = calc.get_date_value('months')
    date_from_now['years'] = calc.get_date_value('years')

    date_from_now = {k: v for k, v in date_from_now.items() if v}
    r = cal_date_incr_from_today(**date_from_now)
    calc.print_calcul_result(r)

# my_str_calculator()
# my_value_calculator()
# my_date_calculator()
