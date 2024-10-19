import math
a = int(input("Введите целое число сторону А >>>"))
b = int(input("Введите целое число сторону В >>>"))
c = int(input("Введите целое число сторону С >>>"))
p = (a + b + c) / 2

if(a > b and a > c):
  maxn = a
  catet1 = b
  catet2 = c
elif(b > a and b > c):
  maxn = b
  catet1 = a
  catet2 = c 
else:
  maxn = c
  catet1 = a
  catet2 = b

if(a <= 0 or b <= 0 or c <= 0):
    print("Сторона не может быть равной нулю или меньше нуля")
elif(catet2 + catet1 <= maxn):
   print("такого треугольника не существует")
else:
    print(f"Площадь Треугольника = {round(math.sqrt(p*(p - a)*(p - b)*(p - c)),3)}")
    if(a != b and a != c):
        print("Треугольник разностороний")
    elif(a == b and a != c or c == b and c != a or a == c and a != b):
        print("Треугольник равнобедренный")
    else:
        print("Треугольник Равностороний")

