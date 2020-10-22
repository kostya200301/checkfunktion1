def date_autumn(dates):
    minn = 9999999
    itoe = ""
    nuy = 2020 * 365 + 10 * 30 + 22
    for i in dates:
        h = i.split("-")
        date = int(h[-1]) * 356 + int(h[-2]) + int(h[-3]) * 30
        if abs(nuy - date) < minn and 9 <= int(h[-3]) <= 11:
            minn = abs(nuy - date)
            itoe = h
    return "-".join(itoe)
