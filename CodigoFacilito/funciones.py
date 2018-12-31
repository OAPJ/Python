def suma(*n):
    print(n)
    print(type(n))

res = suma(12,25,69,85,5)
print(res)

""" Lambdas """
print('---- Lambdas ----')
funcion = lambda n, n2: n + n2
formato = lambda sentencia: '¿{}?'.format(sentencia)
no_valor = lambda : 10
no_resultado = lambda : print('Deben de ejecutar una acción')

resultado = funcion(10,5);
print(resultado)
resultado = formato('Hola');
print(resultado)
resultado = no_valor();
print(resultado)
resultado = no_resultado();
print(resultado)
