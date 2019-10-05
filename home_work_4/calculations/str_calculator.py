from simpleeval import simple_eval


class StrCalculator:

    def calculate_str_expresion(self, str_expresion):
        if type(str_expresion) is not str:
            raise ValueError('Please string expression')
        self.str_expresion = str_expresion
        result = simple_eval(self.str_expresion)
        return result


if __name__ == '__main__':
    # Tests
    assert StrCalculator().calculate_str_expresion('2+2') == 4
    assert StrCalculator().calculate_str_expresion('2 +    2') == 4
    assert StrCalculator().calculate_str_expresion('10+20+30') == 60
    assert StrCalculator().calculate_str_expresion('2+2*2') == 6
    assert StrCalculator().calculate_str_expresion('2*2/2') == 2
    assert StrCalculator().calculate_str_expresion('2**2-4') == 0
    assert StrCalculator().calculate_str_expresion('0.5+0.5') == 1
    try:
        StrCalculator().calculate_str_expresion(1)
    except ValueError as e:
        assert e.args[0] == 'Please string expression'
    print('Tests passed')
