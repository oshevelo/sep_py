from datetime import date

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


def cal_date_incr_from_today(today=None, **kwargs):
    if not today:
        today = date.today()
    else:
        today = parse(today).date()
    r = today + relativedelta(**kwargs)
    return r


if __name__ == '__main__':
    # TESTS
    assert cal_date_incr_from_today(today="9-23-2019", months=2) == parse("11-23-2019").date()
    assert cal_date_incr_from_today(today="9-23-2019", days=1) == parse("9-24-2019").date()
    assert cal_date_incr_from_today(today="9-23-2019", days=32) == parse("10-25-2019").date()
    assert cal_date_incr_from_today(today="9-23-2019", years=1) == parse("9-23-2020").date()
    assert cal_date_incr_from_today(today="9-23-2019", days=1, years=1, months=1) == parse("10-24-2020").date()
    print('Tests passed')
