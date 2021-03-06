'''

Задание 7
Напишите функцию, которая проверяет является ли 
число палиндромом. Число передаётся в качестве пара-
метра. Если число палиндром нужно вернуть из функции 
true, иначе false.
«Палиндром» — это число, у которого первая часть 
цифр равна второй перевернутой части цифр. Например, 
123321 — палиндром (первая часть 123, вторая 321, которая 
после переворота становится 123), 546645 — палиндром, 
а 421987 — не палиндром. 
'''
import math

def palind(self):
    str_len = len(list(map(int, str(self))))
    str_part = math.ceil(str_len / 2)
    
    if str(self)[:str_part] == str(self)[::-1][:str_part]:
        print(f"{self} is a palindrome")
    else:
        print(f"{self} is not palindrome")

palind(222)