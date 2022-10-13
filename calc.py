# while True :
#    s = input('Выберите Знак (+ , - , * , /): ')
#    if s == 'exit' :
#       break
#    if s not in ('+', '-' , '*' , '/') :
#       continue
#    try :
#     a = int(input('Введите число а : '))
#     b = int(input('Введите число b : '))
#    except BaseException:
#       print('Строковое значения!')
#       break
#    if s == '+' : print(a + b)
#    elif s == '-':print(a - b)
#    elif s == '*':print(a * b)
#    elif s == '/':
#       if b != 0 :print(a / b)
#    else:
#       print('Деление на ноль')
# Если мы перечислим все натуральные числа до 10, кратные 3 или 5, мы получим 3, 5, 6 и 9. Сумма этих кратных равна 23.

# Найдите сумму всех чисел, кратных 3 или 5 меньше 1000.


# a = 1
# b = 0

# while a < 999 :
#    a += 1
#    if a % 3 == 0 or a % 5 == 0 :
#       b = a + b
# print(b)     

# fib1 = fib2 = 1
# a = 0
 
# n = int(input())
 
# print(fib1, fib2)
 
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     if fib2 % 2 == 0 :
#        a += fib2
#        if fib2 == 3999999 :
#          break
#     print(f'{fib2}')
# print(f'sasa{a}')    

# count = 0

# for i in range(3) :
#    name = input('Введите никнейм : ')
#    password = int(input('Введите пароль : '))
#    password_repeat = int(input('Введите пароль : '))
   
#    if count == 2 :
#       print('Попробуйте позже!')
#       break
#    if '@' in name or '/' in name :
#       print('Никнейм не должен содержать "@" or "/"')
#       count += 1
#       print(count)
#    elif password == password_repeat :
#       print('Успешно зарегисрирован')
#       break
