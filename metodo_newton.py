#metodo de newton
def metodo_newton(f, df, x0, tol=1e-6, max_iter=100):

    for _ in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        
        if dfx == 0:
            return "La derivada es 0"
        
        x1 = x0 - fx / dfx
        
        if abs(x1 - x0) < tol:
            return x1
        
        x0 = x1
    
    return x0

# funcion
def funcion(x):
    return x**2 - 4 

def derivada(x):
    return 2*x 



# Calcular la raíz
raiz = metodo_newton(funcion, derivada, 3)
print(f"Raíz encontrada: {raiz}")
