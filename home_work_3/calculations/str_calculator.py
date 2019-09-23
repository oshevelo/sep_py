from simpleeval import simple_eval


def calculate_str_expresion(str_expresion):
    if type(str_expresion) is not str:
        raise ValueError('Please string expression')

    result = simple_eval(str_expresion)
    return result


if __name__ == '__main__':
    # Tests
    assert calculate_str_expresion('2+2') == 4
    assert calculate_str_expresion('2 +    2') == 4
    assert calculate_str_expresion('10+20+30') == 60
    assert calculate_str_expresion('2+2*2') == 6
    assert calculate_str_expresion('2*2/2') == 2
    assert calculate_str_expresion('2**2-4') == 0
    assert calculate_str_expresion('0.5+0.5') == 1
    try:
        calculate_str_expresion(1)
    except ValueError as e:
        assert e.args[0] == 'Please string expression'
    print('Tests passed')
