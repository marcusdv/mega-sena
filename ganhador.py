"""
    Esse código acessa a API de jogos da MEGA-SENA
    Calcula quantas vezes cada dezena saiu [Vezes, Dezena]
"""

import requests

response = requests.get("https://loteriascaixa-api.herokuapp.com/api/mega-sena")
api_loterica = response.json()


def enlistar_senas():
    todos_os_jogos = []
    for dado in api_loterica:
        todos_os_jogos.append(dado['dezenas'])
    return todos_os_jogos
    

def gerar_numeros_count():
    nums_1_a_60 = []
    for x in range(1, 61):
        nums_1_a_60.append([0, x])
    return nums_1_a_60


def analisar():
    contadores = gerar_numeros_count()
    todos_os_jogos = enlistar_senas()
    
    for dezenas in todos_os_jogos:
        for dezena in dezenas:
            for contador in contadores:
                if(int(dezena) == contador[1]):
                    contador[0] += 1
                
                
    numeros_organizados = sorted(contadores, reverse = True)
    return numeros_organizados

analise = analisar()

for x in analise:
    print(x)