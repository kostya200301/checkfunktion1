def in_sale(i):
    return True


def goods_analysis(*args, in_sale=in_sale):
    milk = 0
    if in_sale != 0:
        milk = 1
    prises = []
    for_viviod = []
    for i in args:
        if milk == 1:
            if in_sale(i):
                prises.append(i["цена"])
        else:
            if "молоко" in i['название'].lower():
                prises.append(i["цена"])
    prises.sort()
    prises = prises[-3::]
    three = 0
    for i in args:
        if i["цена"] in prises and three != 3:
            prises.remove(i["цена"])
            three += 1
            for_viviod.append(i)
    return for_viviod
