def sum_list_item(value):
    eff = 0
    while value != 0:
        eff += value % 10
        value //= 10
    return eff

rng = [i**3 for i in range(1, 1001, 2)]

eff1 = sum(filter(lambda num: sum_list_item(num) % 7 == 0, rng))
eff2 = sum(filter(lambda num: sum_list_item(num + 17) % 7 == 0, rng))

print(eff1)
print(eff2)