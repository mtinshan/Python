def thesaurus(*names):
    our_dict = dict()
    for n in names:
        our_dict.setdefault(n[0], [])
        our_dict[n[0]].append(n)
    return our_dict
print(thesaurus("Иван", "Мария", "Петр", "Илья"))