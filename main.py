import urllib.request
import json
import os
import keyboard
from time import sleep
from colorama import Fore, Style

# Cores:
verde = Fore.GREEN
vermelho = Fore.RED
branco = Fore.WHITE
azul = Fore.BLUE
cyan = Fore.CYAN
reset = Style.RESET_ALL

# Escolha de turno:
while (True):
    print("--- DADOS DAS ELEIÇÕES 2022 ---")
    print("0 - Sair \n1 - 1º Turno \n2 - 2º Turno")
    op = input(branco + "Escolha qual turno deseja checar: " + reset)
    if op == "1":
        turno = "544"
        break
    elif op == "2":
        turno = "545"
        break
    elif op == "0":
        exit()
    else:
        print(vermelho + "Opção inválida! Tente novamente..." + reset)
        os.system("cls")

# Adquire o JSON do site do TSE:
try:
    with urllib.request.urlopen("https://resultados.tse.jus.br/oficial/ele2022/" + turno + "/dados-simplificados/br/br-c0001-e000" + turno + "-r.json") as url:
        # Declara o JSON como variável:
        data = json.load(url)

        # Dados que se atualizam a cada segundo:
        while (True):
            os.system("cls")
            x = 0

            # Variáveis do JSON:
            candUmVotos = data['cand'][0]['vap']
            candDoisVotos = data['cand'][1]['vap']
            candUmPorcem = data['cand'][0]['pvap']
            candDoisPorcem = data['cand'][1]['pvap']

            # Trocando as "," por "." para que não dê erro:
            for letter in candUmPorcem:
                if letter == ",":
                    candUmPorcem = candUmPorcem.replace(
                        letter, ".")

            for letter in candDoisPorcem:
                if letter == ",":
                    candDoisPorcem = candDoisPorcem.replace(
                        letter, ".")

            # Cálculos:
            subVotos = int(candUmVotos) - int(candDoisVotos)
            subPorcem = float(candUmPorcem) - float(candDoisPorcem)

            # Printando os dados:
            print(azul + "Diferença do 1º ao 2º em votos: " + reset +
                  branco + str(subVotos) + reset)

            print(azul + "Diferença do 1º ao 2º em %: " + reset + branco +
                  str("%.2f" % subPorcem) + "%" + reset)

            # Exibe os candidatos e seus respectivos dados:
            while (x < 11):
                if (data['cand'][x]['nm'] == "LULA"):
                    cor = vermelho
                elif (data['cand'][x]['nm'] == "JAIR BOLSONARO"):
                    cor = verde
                else:
                    cor = azul

                print("\n")
                print(cor + data['cand'][x]['nm'] + reset + branco + " / Votos: " + reset + cyan + data['cand']
                      [x]['vap'] + reset + branco + " / Porcentagem: " + reset + cyan + data['cand'][x]['pvap'] + "%" + reset)
                x += 1

            if keyboard.is_pressed("esc"):
                os.system("cls")
                exit()

except urllib.error.HTTPError:
    print("Erro ao carregar os dados, tente novamente...")
    sleep(5)
