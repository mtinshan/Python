def func():
  duration = int(input('Введите количество секунд: '))
  if (duration / 60) < 1:
    print (duration, 'сек')
  if (duration // 60) >= 1 and (duration // 60) < 60:
    print ((duration // 60), 'мин', (duration % 60), 'сек')
  if (duration // 60) >= 60 and (duration // 60) < 1440:
    print ((duration // 3600), 'час', ((duration % 3600) // 60), 'мин', ((duration % 3600) % 60), 'сек')
  if (duration // 86400) >= 1 and (duration // 86400) < 365:
    print ((duration // 86400), 'дн', ((duration % 86400) // 3600), 'час', (((duration % 86400) % 3600)) // 60, 'мин', (((duration % 86400) % 3600)) % 60, 'сек')
  again = input("Введите текст: y-повтор, n-выход ").lower()
  if again == 'y':
    func()
func() 