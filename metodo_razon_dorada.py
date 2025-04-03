#metodo de la razon dorada

def metodo_razon_dorada(f, a, b, tol=1e-6, max_itr=100):

    phi = (1 + 5**0.5) / 2 
    resphi = 2 - phi
    
    x1 = a + resphi * (b - a)
    x2 = b - resphi * (b - a)
    f1 = f(x1)
    f2 = f(x2)
    
    for _ in range(max_itr):
        if abs(b - a) < tol:
            return (a + b) / 2
        
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + resphi * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - resphi * (b - a)
            f2 = f(x2)
    
    return (a + b) / 2

# funcion
def funcion(x):
    return (x - 2)**2 + 3

# Calcular minimo
minimo = metodo_razon_dorada(funcion, 0, 4)
print(f"Mínimo encontrado: {minimo}")