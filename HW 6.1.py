import string

symb = string.ascii_letters
start, end = input("Введите две буквы через дефис: ").split('-')

print(symb[symb.index(start): symb.index(end) + 1])