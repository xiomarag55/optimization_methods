# metodo de la interpolacion cuadratica
def metodo_interpolacion_cuadratica(f, x0, x1, x2, tol=1e-6, max_iter=100):

    for _ in range(max_iter):
        f0, f1, f2 = f(x0), f(x1), f(x2)
        
        # Calcular puntos del vertice
        num = (x1 - x0)**2 * (f1 - f2) - (x1 - x2)**2 * (f1 - f0)
        den = (x1 - x0) * (f1 - f2) - (x1 - x2) * (f1 - f0)
        
        if den == 0:
            return x1  
        
        x3 = x1 - 0.5 * (num / den)
        
        if abs(x3 - x1) < tol:
            return x3

        if f(x3) < f(x2):
            x0, x1, x2 = x1, x2, x3
        else:
            x0, x1, x2 = x1, x3, x2
    
    return x1

# funcion
def funcion(x):
    return (x - 2)**2 + 3 


# Calcular minimo
minimo = metodo_interpolacion_cuadratica(funcion, 0, 1, 4)
print(f"Mínimo encontrado: {minimo}")