import math
a = int(input())
b = int(input())
c = int(input())

if a == 0:
    print ("Коэфициент при x^4 не должен быть равен нулю")
else:
    d = b*b - 4*a*c
    if d > 0:
        x1 = (-1*b + math.sqrt(d)) / (2*a)
        x2 = (-1*b - math.sqrt(d)) / (2*a)
        if x1 > 0:
            x11 = math.sqrt(x1)
            x12 = -1* math.sqrt(x1)
            if x2 > 0:
                x21 = math.sqrt(x2)
                x22 = -1* math.sqrt(x2)
                print ("Корни уравнения: ", x11, " ", x12, " ", x21, " ", x22)
            elif x2 == 0:
                print ("Корни уравнения: ", x11, " ", x12, " ", x2)
            else:
                print ("Корни уравнения: ", x11, " ", x12)
        elif x1 == 0:
            if x2 > 0:
                x21 = math.sqrt(x2)
                x22 = -1* math.sqrt(x2)
                print ("Корни уравнения: ", x1, " ", x21, " ", x22)
            elif x2 == 0:
                print ("Корни уравнения: ", x1, " ", x2)
            else:
                print ("Корни уравнения: ", x1)
        else:
            if x2 > 0:
                x21 = math.sqrt(x2)
                x22 = -1* math.sqrt(x2)
                print ("Корни уравнения: ", x21, " ", x22)
            elif x2 == 0:
                print ("Корни уравнения: ", x2)
            else:
                print ("Рациональных корней нет")
    elif d == 0:
        x = (-1*b) / (2*a)
        if x > 0:
            x01 = math.sqrt(x)
            x02 = -1* math.sqrt(x)
            print ("Корни уравнения: ", x01, " ", x02)
        elif x == 0:
            print ("Единственный корень: ", x)
        else:
            print ("Рациональных корней нет")
    else:
        print ("Дискриминант меньше нуля, корней нет")
