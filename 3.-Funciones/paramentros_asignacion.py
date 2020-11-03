# Función que modifica parámetros recibidos
def my_func(n, l):
    print(">>my_func():", n, l)
    n = 0
    l[0] = "hola"
 
x = 5
y = [ "hello" ]
# Para entenderlo: como si al iniciar my_func() se hace: n, l = x, y
my_func(x, y)
print(x, y)
a = []
a.append("hola")
b = a

print(a is b)
print(a == b)
print(b)