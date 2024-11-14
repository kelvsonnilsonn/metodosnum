import numpy as np

# Dados fornecidos
x_points = np.array([0, 1, 2, 3, 4])
y_points = np.array([10, 15, 20, 10, 5])

# Função de interpolação quadrática (usando três primeiros pontos)
def quadratica_interpolation(x_points, y_points, x_val):
    # Apenas usa os três primeiros pontos (0, 1, 2) para o ajuste quadrático
    x0, x1, x2 = x_points[:3]
    y0, y1, y2 = y_points[:3]
    
    # Coeficientes do polinômio quadrático
    a = (y0 / ((x0 - x1) * (x0 - x2))) + (y1 / ((x1 - x0) * (x1 - x2))) + (y2 / ((x2 - x0) * (x2 - x1)))
    b = -((y0 * (x1 + x2)) / ((x0 - x1) * (x0 - x2))) - ((y1 * (x0 + x2)) / ((x1 - x0) * (x1 - x2))) - ((y2 * (x0 + x1)) / ((x2 - x0) * (x2 - x1)))
    c = (y0 * x1 * x2) / ((x0 - x1) * (x0 - x2)) + (y1 * x0 * x2) / ((x1 - x0) * (x1 - x2)) + (y2 * x0 * x1) / ((x2 - x0) * (x2 - x1))
    
    # Avalia o polinômio quadrático no ponto x_val
    y_val = a * x_val**2 + b * x_val + c
    return y_val

# Exemplo de uso para interpolar em x = 2.5
x_val = 2.5
y_val = quadratica_interpolation(x_points, y_points, x_val)

print(f'O valor interpolado pela Interpolação Quadrática em x = {x_val} é y = {y_val}')
