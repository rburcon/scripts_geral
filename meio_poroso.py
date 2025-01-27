#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 13:07:55 2025

@author: rburcon
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Definição da equação de Darcy-Forchheimer
def darcy_forchheimer(v, D, F):
    """
    Modelo de Darcy-Forchheimer: ΔP/L = D*v + F*v^2
    """
    return D * v + F * v**2

# Dados experimentais (substitua pelos seus dados reais)
# Velocidade superficial (v) em m/s
velocidade = np.array([0.1, 0.2, 0.3, 0.4, 0.5])

# Gradiente de pressão (ΔP/L) em Pa/m
gradiente_pressao = np.array([10, 25, 50, 85, 130])

# Ajuste do modelo aos dados experimentais
parametros, covariancia = curve_fit(darcy_forchheimer, velocidade, gradiente_pressao)

# Coeficientes ajustados
D, F = parametros

# Exibindo os resultados
print(f"Coeficiente D (resistência viscosa): {D:.4f} Pa·s/m²")
print(f"Coeficiente F (resistência inercial): {F:.4f} Pa·s²/m³")

# Gráfico de comparação
velocidade_ajustada = np.linspace(0, max(velocidade), 100)
gradiente_ajustado = darcy_forchheimer(velocidade_ajustada, D, F)

plt.scatter(velocidade, gradiente_pressao, label="Dados Experimentais", color="blue", marker="o")
plt.plot(velocidade_ajustada, gradiente_ajustado, label="Ajuste Darcy-Forchheimer", color="red")
plt.xlabel("Velocidade Superficial (v) [m/s]")
plt.ylabel("Gradiente de Pressão (ΔP/L) [Pa/m]")
plt.title("Ajuste do Modelo Darcy-Forchheimer")
plt.legend()
plt.grid(True)
plt.show()
