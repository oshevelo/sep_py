a = 10

def usd_in_uah(orig_price, a, ex=10):   
    if isinstance(orig_price, str):
        return None
    if type(orig_price) == str:
        return None
    orig_price = float(orig_price)

    print(a)
    a += 1
    res = orig_price * ex

        

    return a, res

#print('asdasdasd')

#print('before call')
price = 100
rate = 25
res = usd_in_uah(
    a=a,
    orig_price=price
)
print(res)

res = usd_in_uah(
    a=a,
    orig_price=str(price)
)
print(res)
print(a)
#print(result)
#print(created)
#print(type(result))

'''
def test_args(*args, **kwargs):
    print(args)
    print(kwargs)

test_args()
test_args(1,2,3,4,5)
test_args('4.com',5 ,host='4.com',port=5)
'''
