import math as m

def task1(x, y, z): 
    x = float(input('Введите x:'))
    y = float(input('Введите y:'))
    z = float(input('Введите z:'))
    a = m.sin(x)**2 + m.cos(y)**2 + m.log(m.e**x + m.e**(-y))
    b = m.log((abs(x - 1))**0.5) - (abs(y))**0.2
    return float("{0:.4f}".format(a)), float("{0:.4f}".format(b))
def task2():
    x = float(input('Введите x:'))
    a = 1
    b = 2 
    f = (x + a)**0.5 + ((x**2 + b)/x)
    return float("{0:.4f}".format(f))
def task3():
    x = float(input('Введите x:'))
    f = m.sin(x**0.5) + m.cos(x**0.5)
    return float("{0:.4f}".format(f))
def task4():
    h = float(input('Введите h:'))
    a = float(input('Введите a:'))
    s = a**2 + 4 * (((h**2 + (a/2)**2)**0.5)*a*0.5)
    v = 1/3*a**2*h
    return float("{0:.4f}".format(s)), float("{0:.4f}".format(v))
def task5(x):
    r = float(input('Введите r:'))
    a = float(input('Введите a:'))
    s = (a**2*(3**0.5))/4
    n = s*(3**0.5)*(r**2)/2
    return float("{0:.4f}".format(n))
def task6():
    a = float(input('Введите a:'))
    b = float(input('Введите b:'))
    c = float(input('Введите c:'))
    p = (a + b + c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    h1 = (2*s)/a
    h2 = (2*s)/b
    h3 = (2*s)/c
    return float("{0:.4f}".format(h1)), float("{0:.4f}".format(h2)), float("{0:.4f}".format(h3))
def task7():
    a = float(input('Введите число А:'))
    b = float(input('Введите число В:'))
    x = b/a
    return float("{0:.4f}".format(x))
def task8():
    x = float(input('Введите вес конфет:'))
    a = float(input('Введите стоймость', x, 'кг конфет:'))
    y = float(input('Введите искомый вес:'))
    b = a/x
    c = b*y
    return float("{0:.4f}".format(b)), float("{0:.4f}".format(c))
def task9():
    k = float(input('Введите комиссию в рублях:'))
    r = float(input('Введите количество рублей:'))
    c = (r-k)*4.88
    return float("{0:.4f}".format(c))
