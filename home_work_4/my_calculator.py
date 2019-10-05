from home_work_4.calculations.date_calculator import DateCalculator
from home_work_4.calculations.str_calculator import StrCalculator
from home_work_4.calculator_interface import CalculatorInterface


class MyCalculator(StrCalculator, DateCalculator):
    interface = CalculatorInterface()

    def __init__(self, calculator_mode):

        if calculator_mode == 'str_calculator':
            self.my_str_calculator()
        elif calculator_mode == 'value_calculator':
            self.my_value_calculator()
        elif calculator_mode == 'date_calculator':
            self.my_date_calculator()
        else:
            raise ValueError('calculator mode unknown')

    def my_value_calculator(self):
        value1 = self.interface.get_value_to_calculate()
        op1 = self.interface.get_math_operation()
        value2 = self.interface.get_value_to_calculate()
        op2 = self.interface.get_dditinal_math()
        if op2:
            value3 = self.interface.get_value_to_calculate()
            str_expresion = value1 + op1 + value2 + op2 + value3
        else:
            str_expresion = value1 + op1 + value2

        result = self.calculate_str_expresion(str_expresion)
        self.interface.print_calcul_result(result)

    def my_str_calculator(self):
        str_expression = self.interface.get_str_expression_to_calc()
        result = self.calculate_str_expresion(str_expression)
        self.interface.print_calcul_result(result)

    def my_date_calculator(self):
        self.interface.date_calculator_greeting()
        date_from_now = {}
        date_from_now['days'] = self.interface.get_date_value('days')
        date_from_now['months'] = self.interface.get_date_value('months')
        date_from_now['years'] = self.interface.get_date_value('years')

        date_from_now = {k: v for k, v in date_from_now.items() if v}
        r = self.cal_date_incr_from_today(**date_from_now)
        self.interface.print_calcul_result(r)


calc_1 = MyCalculator(calculator_mode='str_calculator')
calc_2 = MyCalculator(calculator_mode='value_calculator')
calc_3 = MyCalculator(calculator_mode='date_calculator')
