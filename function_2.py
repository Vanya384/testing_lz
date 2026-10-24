import math

def function_number_2(a,b,c,d,f):
    if c==d:
        print("Ошибка : при c == d мы получаем деление на 0 \n")
        return None

    if f<0:
        print("Ошибка: при f<0 корень из f вычисляться не будет(без особых модулей и способов)")
        return None

    y = ( ( a + b ) / ( c - d ) ) + math.sqrt(f)
    return y

