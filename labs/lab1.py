import math as m

def task1(x, y, z): 
    x = float(input('Введите x:'))
    y = float(input('Введите y:'))
    z = float(input('Введите z:'))
    a = m.sin(x)**2 + m.cos(y)**2 + m.log(m.e**x + m.e**(-y))
    b = m.log((abs(x - 1))**0.5) - (abs(y))**0.2
    print('a=', float("{0:.4f}".format(a)), 'b=', float("{0:.4f}".format(b)))
def task2():
    x = float(input('Введите x:'))
    a = 1
    b = 2 
    f = (x + a)**0.5 + ((x**2 + b)/x)
    print('f=', float("{0:.4f}".format(f)))
def task3():
    x = float(input('Введите x:'))
    f = m.sin(x**0.5) + m.cos(x**0.5)
    print('f=', float("{0:.4f}".format(f)))
def task4():
    h = float(input('Введите h:'))
    a = float(input('Введите a:'))
    s = a**2 + 4 * (((h**2 + (a/2)**2)**0.5)*a*0.5)
    v = 1/3*a**2*h
    print('Площадь поверхности:', float("{0:.4f}".format(s)), 'Объём:', float("{0:.4f}".format(v)))
def task5():
    r = float(input('Введите r:'))
    a = float(input('Введите a:'))
    s = (a**2*(3**0.5))/4
    n = s*(3**0.5)*(r**2)/2
    print('Кол-во шаров:', float("{0:.4f}".format(n)))
def task6():
    a = float(input('Введите a:'))
    b = float(input('Введите b:'))
    c = float(input('Введите c:'))
    p = (a + b + c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    h1 = (2*s)/a
    h2 = (2*s)/b
    h3 = (2*s)/c
    h = h1*h2*h3
    print('Произведение высот:', float("{0:.4f}".format(h)))
def task7():
    a = float(input('Введите число А:'))
    b = float(input('Введите число В:'))
    x = b/a
    print('Корень уравнения:', float("{0:.4f}".format(x)))
def task8():
    x = float(input('Введите вес конфет:'))
    a = float(input('Введите стоймость', x, 'кг конфет:'))
    y = float(input('Введите искомый вес:'))
    b = a/x
    c = b*y
    print('Цена 1кг конфет:', float("{0:.4f}".format(b)), 'Цена', y, 'кг конфет:', float("{0:.4f}".format(c)))
def task9():
    k = float(input('Введите комиссию в рублях:'))
    r = float(input('Введите количество рублей:'))
    c = (r-k)*4.88
    print('Кол-во тенге:', float("{0:.4f}".format(c)))
