#metodo busqueda aleatoria

import random

def busqueda_aleatoria(f, a, b, tol=1e-6, max_iter=1000):
    mejor_x = None
    mejor_f = float('inf')
    
    for _ in range(max_iter):
        x = random.uniform(a, b) 
        fx = abs(f(x)) 
        
        if fx < mejor_f:
            mejor_x, mejor_f = x, fx
        
        if mejor_f < tol:
            return mejor_x
    
    return mejor_x

# funcion
def funcion(x):
    return x**2 - 4 


# Calcular la raíz aproximada
raiz = busqueda_aleatoria(funcion, -3, 3)
print(f"Raíz aproximada encontrada: {raiz}")