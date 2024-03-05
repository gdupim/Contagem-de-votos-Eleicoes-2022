import json
import os
import platform
import urllib.request
import urllib.error
import keyboard
from multiprocessing import Process
from time import sleep
from colorama import Fore, Style


def apagarTela():
    if (platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")


# ? Variáveis:
# ? Cores:
verde = Fore.GREEN
vermelho = Fore.RED
branco = Fore.WHITE
azul = Fore.BLUE
cyan = Fore.CYAN
reset = Style.RESET_ALL

# ? Escolha de turno:
while (True):
    apagarTela()
    print("--- DADOS DAS ELEIÇÕES 2022 ---")
    print("0 - Sair \n1 - Primeiro Turno. \n2 - Segundo Turno.")
    op = input(branco + "Escolha qual turno deseja checar: " + reset)
    if op == "1":
        turno = "544"
        turnoGovernador = "546"
        numCandidatos = 11
        break
    elif op == "2":
        turno = "545"
        turnoGovernador = "547"
        numCandidatos = 2
        break
    elif op == "0":
        apagarTela()
        exit()
    else:
        print(vermelho + "Opção inválida! Tente novamente..." + reset)
        apagarTela()

# ? Define URL:
urlPresidente = ("https://resultados.tse.jus.br/oficial/ele2022/" + turno
                 + "/dados-simplificados/br/br-c0001-e000" + turno + "-r.json")
urlGovernador = ("https://resultados.tse.jus.br/oficial/ele2022/" + turnoGovernador
                 + "/dados-simplificados/sp/sp-c0003-e000" + turnoGovernador + "-r.json")


def eleicaoPresidente():
    # ? Adquire o JSON do site do TSE:
    try:
        with urllib.request.urlopen(urlPresidente) as url:
            # ? Declara o JSON como variável:
            data = json.load(url)

            # ? Dados que se atualizam a cada segundo:

            # ? Variáveis do JSON:
            candUmVotos = data["cand"][0]["vap"]
            candDoisVotos = data["cand"][1]["vap"]
            candUmPorcem = data["cand"][0]["pvap"]
            candDoisPorcem = data["cand"][1]["pvap"]
            porcemUrnaApurada = data["psi"]

            # ? Trocando as "," por "." para que não dê erro depois:
            for letter in candUmPorcem:
                if letter == ",":
                    candUmPorcem = candUmPorcem.replace(letter, ".")

            for letter in candDoisPorcem:
                if letter == ",":
                    candDoisPorcem = candDoisPorcem.replace(letter, ".")

            # ? Cálculos:
            subVotos = int(candUmVotos) - int(candDoisVotos)
            subPorcem = float(candUmPorcem) - float(candDoisPorcem)

            # ? Printando os dados:
            print(azul + "Diferença do 1º ao 2º em votos: " + reset
                  + branco + str(subVotos) + reset)

            print(azul + "Diferença do 1º ao 2º em porcentagem: " + reset
                  + branco + str("%.2f" % subPorcem) + "%" + reset)

            print(azul + "Porcentagem de urnas apuradas: " + reset
                  + branco + str(porcemUrnaApurada) + "%" + reset)

            # ? Exibe os candidatos e seus respectivos dados:
            x = 0
            cor = ""
            while x < numCandidatos:
                if (data["cand"][x]["nm"] == "LULA"):
                    cor = vermelho
                elif (data["cand"][x]["nm"] == "JAIR BOLSONARO"):
                    cor = verde
                elif (data["cand"][x]["nm"] == "FELIPE D&apos;AVILA"):
                    data["cand"][x]["nm"] = "FELIPE D'AVILA"
                else:
                    cor = azul

                print("\n")
                print(cor + data["cand"][x]["nm"] + reset
                      + branco + " / Votos: " + reset
                      + cyan + data["cand"][x]["vap"] + reset
                      + branco + " / Porcentagem: " + reset
                      + cyan + data["cand"][x]["pvap"] + "%" + reset)
                x += 1

            # ? Dados que se atualizam a cada 10 segundos:
            sleep(10)

            apagarTela()

    except urllib.error.HTTPError:
        apagarTela()
        print("Erro ao carregar a página, tente novamente...")
        sleep(5)

    except urllib.error.URLError:
        apagarTela()
        print("Erro de conexão, tente novamente...")
        sleep(5)


def eleicaoGovernador():
    # ? Adquire o JSON do site do TSE:
    try:
        with urllib.request.urlopen(urlGovernador) as url:
            # ? Declara o JSON como variável:
            data = json.load(url)

            # ? Dados que se atualizam a cada segundo:
            # ? Variáveis do JSON:
            candUmVotos = data["cand"][0]["vap"]
            candDoisVotos = data["cand"][1]["vap"]
            candUmPorcem = data["cand"][0]["pvap"]
            candDoisPorcem = data["cand"][1]["pvap"]
            porcemUrnaApurada = data["psi"]

            # ? Trocando as "," por "." para que não dê erro depois:
            for letter in candUmPorcem:
                if letter == ",":
                    candUmPorcem = candUmPorcem.replace(letter, ".")

            for letter in candDoisPorcem:
                if letter == ",":
                    candDoisPorcem = candDoisPorcem.replace(letter, ".")

            # ? Cálculos:
            subVotos = int(candUmVotos) - int(candDoisVotos)
            subPorcem = float(candUmPorcem) - float(candDoisPorcem)

            # ? Printando os dados:
            print(azul + "Diferença do 1º ao 2º em votos: " + reset
                  + branco + str(subVotos) + reset)

            print(azul + "Diferença do 1º ao 2º em porcentagem: " + reset
                  + branco + str("%.2f" % subPorcem) + "%" + reset)

            print(azul + "Porcentagem de urnas apuradas: " + reset
                  + branco + str(porcemUrnaApurada) + "%" + reset)

            # ? Exibe os candidatos e seus respectivos dados:
            x = 0
            cor = ""
            while x < 2:
                if (data["cand"][x]["nm"] == "FERNANDO HADDAD"):
                    cor = vermelho
                else:
                    cor = verde

                print("\n")
                print(cor + data["cand"][x]["nm"] + reset
                      + branco + " / Votos: " + reset
                      + cyan + data["cand"][x]["vap"] + reset
                      + branco + " / Porcentagem: " + reset
                      + cyan + data["cand"][x]["pvap"] + "%" + reset)
                x += 1

            # ? Dados que se atualizam a cada 10 segundos:
            sleep(10)

            apagarTela()

    except urllib.error.HTTPError:
        apagarTela()
        print("Erro ao carregar a página, tente novamente...")
        sleep(5)

    except urllib.error.URLError:
        apagarTela()
        print("Erro de conexão, tente novamente...")
        sleep(5)


while (True):
    apagarTela()
    eleicaoPresidente()
    # eleicaoGovernador()
