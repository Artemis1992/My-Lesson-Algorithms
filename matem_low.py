ppp = "\n---------------------------------------------------"
print(ppp)
# давайте рассмотрим 10 примеров использования оператора % в коде. Это поможет понять, как применять его для различных задач.

# Первый пример и самы распространенный.
# Пример 1: Проверка четности числа.

number = 10
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
    # Вывод: 10 is even


ppp = "\n---------------------------------------------------"
print(ppp)
# Пример 2: Определение остатка при делении

numerator = 17
denominator = 5
reminder = numerator % denominator
print(f"{numerator} % {denominator} = {reminder}")
# 17 % 5 = 2


ppp = "\n---------------------------------------------------"
print(ppp)
# Пример 3: Проверка кратности числа

number = 21
if number % 7 == 0:
    print(f"{number} is devision by 7")
else:
    print(f"{number} is not devision 7")
    
ppp = "\n---------------------------------------------------"
print(ppp)
# Пример 4: Использование оператора % в цикле

# Давайте разберем пример 2 % 3 более подробно.
# Когда мы делим 2 на 3, результат деления будет 0 
# (потому что 3 не помещается в 2 целых раз). 
# Остаток от этого деления будет равен самому числу 2, потому что 2 - это то, что остается, 
# когда мы пытаемся разделить его на 3.

for i in range(1, 11):
    print(f"{i} % 3 = {i % 3}")
# 1 % 3 = 1
# 2 % 3 = 2
# 3 % 3 = 0
# 4 % 3 = 1
# 5 % 3 = 2
# 6 % 3 = 0
# 7 % 3 = 1
# 8 % 3 = 2
# 9 % 3 = 0
# 10 % 3 = 1


ppp = "\n---------------------------------------------------"
print(ppp)
# Пример 5: Циклический индекс в массиве
arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = len(arr1)
index = 5
ciclic_index = index % n
print(arr1[ciclic_index])
# Вывод 60:
# Поскольку 5 меньше, чем 9, деление 5 на 9 не дает полного деления (целое число раз), то есть 9 не помещается в 5 ни разу целиком.
# В этом случае результат целочисленного деления равен 0, и весь остаток остается равным самому числу 5.


ppp = "\n---------------------------------------------------"
print(ppp)
# Пример 6: Проверка высокосного года




ppp = "\n---------------------------------------------------"
print(ppp)
# Допустим, у нас есть массив arr с длиной n = 8:

arr = [5, 8, 6, 4, 9, 2, 7, 3]
n = len(arr)  # n = 8

# Теперь вычислим значение left для пяти различных значений i:

# Пример 1: i = 0








