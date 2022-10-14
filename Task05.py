# PythonIntroduction HomeWork-1
# Задача-5

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в
#  2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# Корень квадратный из суммы квадратов разности даст нам расстояние между точками


xa = int(input('введите x для точки А ') )
ya = int(input('введите y для точки А ') )
xb = int(input('введите x для точки B ') )
yb = int(input('введите y для точки B ') )

distance1 = (xb-xa)**2+(yb-ya)**2
import math
distance2 = math.sqrt(distance1)
print(f'A ({xa}, {ya}); B({xb}, {yb}) ->', end =" ")
print(round(distance2, 2))
#print(type(distance2))

