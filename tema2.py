# cerinta1
print("Cerinta1\n")


def my_function(*args, **param_1):
    sum = 0
    for i in args:
        if type(i) == int or type(i) == float:
            sum += i
    return sum


res = my_function(1, 5, -3, 'abc', [12, 56, 'cad'])
print(res)

res1 = my_function()
print(res1)

res2 = my_function(2, 4, 'abc', param_1=2)
print(res2)

# cerinta2
print("Cerinta2\n")


def suma(n):
    if n == 0:
        return 0
    return n + suma(n - 1)


print(suma(3))


def suma_pare(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + suma_pare(n - 1)
    else:
        return suma_pare(n - 1)


print(suma_pare(4))


def suma_impare(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return n + suma_impare(n - 1)
    else:
        return suma_impare(n - 1)


print(suma_impare(5))

# cerinta3
print("Cerinta3\n")

def func():
    var = input()
    try:
        var = int(var)
        return var
    except:
        return 0


print(func())
