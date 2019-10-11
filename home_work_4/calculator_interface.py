import math


class CalculatorInterface:

    def __init__(self):
        self.__input_value = ""

    @property
    def input_value(self):
        return self.__input_value

    @input_value.setter
    def input_value(self, value):
        if value.isdigit():
            self.__input_value = value
        elif value.replace(".", "").isdigit():
            self.__input_value = value
        elif value.replace(",", "").isdigit():
            self.__input_value = value.replace(",", ".")
        elif value.lower() == 'pi':
            self.__input_value = str(math.pi)
        else:
            raise ValueError('Value is not a number or math constant')

    def get_value_to_calculate(self):
        self.input_value = input('Please enter a value: ')
        return self.input_value

    @staticmethod
    def get_math_operation():
        op = input('Please enter a math operation: ')
        return op

    @staticmethod
    def print_calcul_result(result):
        print('RESULT = ', result)

    @staticmethod
    def get_dditinal_math():
        op_or_skip = input(
            'Please enter more math operation or ENTER to calulate: ')
        return op_or_skip

    @staticmethod
    def get_str_expression_to_calc():
        str_expression = input(
            'Please enter expresion to calculate: ')
        return str_expression

    @staticmethod
    def get_date_value(date_value):
        date_value = input(f'Please enter "{date_value}" from now: ')
        return int(date_value) if date_value != '' else date_value

    @staticmethod
    def date_calculator_greeting():
        print('Enter day month year to calculate or skip')
