numb_set = str(input('Введите текстом число от 1 до 10 на английском: '))

dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def numbs_in_rus(eng_word):
  if eng_word[0] == eng_word[0].upper():
    eng_word = eng_word.lower()
    return dict[eng_word].capitalize()
  return dict.get(eng_word)

print(numbs_in_rus(numb_set))