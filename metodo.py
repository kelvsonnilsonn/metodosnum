import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

# Dados simulados de medições de pressão em pontos específicos
x_points = np.array([0, 1, 2, 3, 4])
y_points = np.array([10, 15, 20, 10, 5])

# Função para interpolação quadrática
def interpolacao_quadratica(x_points, y_points):
    # Ajuste de um polinômio de segundo grau (quadrático) aos três primeiros pontos
    p = Polynomial.fit(x_points[:3], y_points[:3], 2)
    return p

# Função para interpolação de Lagrange
def interpolacao_lagrange(x_points, y_points):
    # Criação do polinômio de Lagrange usando os pontos fornecidos
    poly_lagrange = lagrange(x_points, y_points)
    return poly_lagrange

# Plotar resultados
def plot_resultados(x_points, y_points, poly_quadratica, poly_lagrange):
    # Criação de uma linha suave para visualizar a interpolação
    x_smooth = np.linspace(x_points.min(), x_points.max(), 500)
    
    # Resultados interpolados
    y_smooth_quadratica = poly_quadratica(x_smooth)
    y_smooth_lagrange = poly_lagrange(x_smooth)
    
    # Plot dos resultados
    plt.figure(figsize=(10, 6))

    # Plotando os pontos de dados originais
    plt.scatter(x_points, y_points, color='red', label='Dados originais', zorder=5)

    # Curva interpolada (Quadrática)
    plt.plot(x_smooth, y_smooth_quadratica, label='Interpolação Quadrática', linestyle='--', color='blue')

    # Curva interpolada (Lagrange)
    plt.plot(x_smooth, y_smooth_lagrange, label='Interpolação de Lagrange', linestyle='-', color='green')

    # Configurações do gráfico
    plt.title('Comparação dos Métodos de Interpolação')
    plt.xlabel('Posição na superfície (x)')
    plt.ylabel('Pressão medida (y)')
    plt.legend()
    plt.grid(True)

    # Exibir o gráfico
    plt.show()

# Executar as funções de interpolação
poly_quadratica = interpolacao_quadratica(x_points, y_points)
poly_lagrange = interpolacao_lagrange(x_points, y_points)

# Plotar os resultados
plot_resultados(x_points, y_points, poly_quadratica, poly_lagrange)
