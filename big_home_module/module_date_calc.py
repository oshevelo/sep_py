#FIXME: datetime good no checks bad
from datetime import datetime

def calc(a, b):

    if operation == '+':
        return a + b

    elif operation == '-':
        return a - b

    else:
        print('Error, будь ласка введіть правильно операцію (+,-)')


date1 = input('Введіть першу дату в такому форматі (дд/мм/рррр): ')
try:
    dt_object1 = datetime.strptime(date1,'%d/%m/%Y')
except Exception as e:
    print('error {}'.format(e))
    exit()

operation = input('enter operation: (+,-)')

date2 = input('Введіть другу дату в такому форматі (дд/мм/рррр): ')

try:
    dt_object2 = datetime.strptime(date2,'%d/%m/%Y')
except Exception as e:
    print('error {}'.format(e))
    exit()

result = calc(a = dt_object1 , b = dt_object2)
print(result)











