# Metodo de biseccion
def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        return "La funcion no tiene raices en el intervalo dado"
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            return c  
        elif f(a) * f(c) < 0:
            b = c  # La raíz está en [a, c]
        else:
            a = c  # La raíz está en [c, b]
        
        iter_count += 1
    
    return (a + b) / 2  

# Ejemplo de uso
def funcion(x):
    return x**3 - 4*x - 9

raiz = biseccion(funcion, 2, 3)
print(f"Raíz aproximada: {raiz}")
