import numpy as np

# Dados fornecidos
x_points = np.array([0, 1, 2, 3, 4])
y_points = np.array([10, 15, 20, 10, 5])

# Função de interpolação de Lagrange
def lagrange_interpolation(x_points, y_points, x_val):
    result = 0
    n = len(x_points)
    
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if j != i:
                term *= (x_val - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Exemplo de uso para interpolar em x = 2.5
x_val = 2.5
y_val = lagrange_interpolation(x_points, y_points, x_val)

print(f'O valor interpolado em x = {x_val} é y = {y_val}')