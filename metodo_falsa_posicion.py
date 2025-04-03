# metodo de falsa posicion

def falsa_posicion(f, a, b, tol=1e-6, max_itr=100):

    if f(a) * f(b) >= 0:
        return "La funcion no cambia de signo en [a, b]"
    
    for _ in range(max_itr):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if abs(f(c)) < tol:
            return c
        
        if f(a) * f(c) < 0:
            b = c # raiz en [a, c]
        else:
            a = c # raiz en [c, b]
    return c

# Funcion
def funcion(x):
    return x**4 - 5*x - 9

# Calculamos la raiz
raiz = falsa_posicion(funcion, 2, 3)
print(f"Raiz encontrada: {raiz} ")
