def remove_palindroms(spells):
    for i2 in range(len(spells)):
        for i in spells:
            if i.replace(" ", "").lower() == i.replace(" ", "")[::-1].lower():
                spells.remove(i)
    return spells
