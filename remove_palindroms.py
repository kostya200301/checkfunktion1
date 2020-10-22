new_list = []
def remove_palindroms(spells):
    spells = new_list
    for i in range(len(spells)):
        for i in spells:
            if i.lower() == i[::-1].lower():
                spells.remove(i)
