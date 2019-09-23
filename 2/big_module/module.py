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

if __name__=='__main__':
    a=10
    price = 100
    rate = 25
    res = usd_in_uah(
        a=a,
        orig_price=price
    )

    print(res)
