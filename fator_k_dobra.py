#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:10:03 2025

@author: rburcon
"""

def calcular_fator_k(material, espessura, raio_dobra):
    """
    Calcula o fator k com base no tipo de material, espessura e raio de dobra.

    :param material: Tipo de material (string).
    :param espessura: Espessura da chapa (mm).
    :param raio_dobra: Raio interno de dobra (mm).
    :return: Fator k estimado.
    """
    # Tabela aproximada de fatores para a linha neutra
    fator_k_material = {
        "1": 0.4,
        "2": 0.35,
        "3": 0.4,
        "4": 0.3,
    }

    if material.lower() not in fator_k_material:
        raise ValueError("Material não suportado. Escolha entre: aço carbono, aço inoxidável, alumínio, liga de alta resistência.")

    # Estima o fator k com base no material
    fator_k = fator_k_material[material.lower()]
    linha_neutra = fator_k * espessura
    desconto_dobra = 2 * 3.1416 * (raio_dobra + linha_neutra) * (90 / 360)  # Para 90 graus

    return fator_k, linha_neutra, desconto_dobra


def estimar_raio_minimo(material, espessura):
    """
    Estima o raio mínimo de dobra com base no material e espessura.

    :param material: Tipo de material (string).
    :param espessura: Espessura da chapa (mm).
    :return: Raio mínimo de dobra (mm).
    """
    # Fatores típicos de raio mínimo
    fator_raio_material = {
        "1": 1.5,
        "2": 3,
        "3": 1,
        "4": 4,
    }

    if material.lower() not in fator_raio_material:
        raise ValueError("Material não suportado. Escolha entre: aço carbono, aço inoxidável, alumínio, liga de alta resistência.")

    raio_minimo = fator_raio_material[material.lower()] * espessura
    return raio_minimo


# Menu interativo
if __name__ == "__main__":
    print("Cálculo do Fator K e Raio Mínimo de Dobra")
    print("-----------------------------------------")

    # Entrada do usuário
    try:
        material = input("Digite o material (1-aço carbono, 2-aço inoxidável, 3-alumínio, 4-liga de alta resistência): ").strip()
        espessura = float(input("Digite a espessura da chapa (mm): "))
        raio_dobra = float(input("Digite o raio interno de dobra (mm): "))

        # Cálculos
        fator_k, linha_neutra, desconto_dobra = calcular_fator_k(material, espessura, raio_dobra)
        raio_minimo = estimar_raio_minimo(material, espessura)

        # Resultados
        print("\nResultados:")
        print(f"- Fator K estimado: {fator_k:.2f}")
        print(f"- Posição da linha neutra: {linha_neutra:.2f} mm")
        print(f"- Desconto de dobra (para 90°): {desconto_dobra:.2f} mm")
        print(f"- Raio mínimo de dobra: {raio_minimo:.2f} mm")
    except ValueError as e:
        print(f"Erro: {e}")
