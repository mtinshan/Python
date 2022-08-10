price = [57.8, 46.51, 97, 32.14, 11.49, 87.31, 32.9, 632, 314.11, 19.40]
price.sort()
for numb in price:
    rub = int(numb)
    cent = (numb - int(numb)) * 100
    res = f'{rub} руб. {cent:02.0f} коп.'
    print(res)

print()

price = [57.8, 46.51, 97, 32.14, 11.49, 87.31, 32.9, 632, 314.11, 19.40]
price.sort(reverse=True)
for numb in price:
    rub = int(numb)
    cent = (numb - int(numb)) * 100
    res = f'{rub} руб. {cent:02.0f} коп.'
    print(res)

print()

for num, i in enumerate(price, 1):
    print('Top {cout}: {maxim}'.format(maxim = max(price), cout = num))
    price.remove(max(price))