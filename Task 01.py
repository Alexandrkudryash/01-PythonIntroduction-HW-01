# PythonIntroduction HomeWork-1
# Задача-1 
# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input('введите день недели ') )
if a == 1:
    print(f'- {a} -> нет')
elif a == 2:
    print(f'- {a} -> нет')
elif a == 3:
    print(f'- {a} -> нет')
elif a == 4:
    print(f'- {a} -> нет')
elif a == 5:
    print(f'- {a} -> нет')
elif a == 6:
    print(f'- {a} -> да')
elif a == 7:
    print(f'- {a} -> да')
else:
    print('это не день недели')
