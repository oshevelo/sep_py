from home_work_3.str_calculator import calculate_str_expresion
import home_work_3.calculator_interface as calc


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


my_str_calculator()
my_value_calculator()