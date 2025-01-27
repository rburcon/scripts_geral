#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 12:27:02 2025

@author: rburcon
"""

# Cálculo do tamanho da primeira camada da malha em função do y+

def calcular_delta_y(y_plus, U, L, nu, rho):
    """
    Calcula o tamanho da primeira camada de célula (Delta y1) em função de y+.
    
    Parâmetros:
        y_plus (float): Valor desejado de y+.
        U (float): Velocidade do escoamento (m/s).
        L (float): Comprimento característico (m).
        nu (float): Viscosidade cinemática (m²/s).
        rho (float): Densidade do fluido (kg/m³).
        
    Retorna:
        float: Tamanho da primeira camada (Delta y1) em metros.
    """
    # Cálculo do número de Reynolds
    Re_L = U * L / nu
    
    # Coeficiente de atrito (C_f) para placa plana turbulenta (correlação de Schlichting)
    C_f = 0.058 / (Re_L ** 0.2)
    
    # Velocidade de fricção na parede (u_tau)
    u_tau = (0.5 * C_f * rho * U**2 / rho) ** 0.5  # Simplificado para eliminar rho
    
    # Tamanho da primeira camada da malha
    delta_y1 = (y_plus * nu) / u_tau
    
    return delta_y1


# Exemplo de uso:
if __name__ == "__main__":
    # Parâmetros do escoamento
    y_plus = 1  # Desejado (e.g., 1 para resolver a subcamada viscosa)
    U = 10.0    # Velocidade do escoamento (m/s)
    L = 1.0     # Comprimento característico (m)
    nu = 1.5e-5 # Viscosidade cinemática do ar (m²/s)
    rho = 1.225 # Densidade do ar (kg/m³)

    # Cálculo do tamanho da primeira camada
    delta_y1 = calcular_delta_y(y_plus, U, L, nu, rho)
    print(f"\n\nTamanho da primeira camada da malha (Delta y1): {delta_y1:.6e} m")
