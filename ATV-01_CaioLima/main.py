from controle import Controle
from televisao import *

tv = Televisao()
controle = Controle()


def menu():
    while True:
        print("                 Controle                ")
        print("             [L] On | [O] Off            ")
        print("           [+] +Vol | [-] -Vol           ")
        print("               [1] [2] [3]               ")
        print("               [4] [5] [6]               ")
        print("               [7] [8] [9]               ")
        print("                   [0]                  ")
        print("                [X] EXIT                  ")


        resp = input("Escolha: ").lower()
        if resp == "o":
            chamarFuncoes(resp)
        elif resp.isdigit() and int(resp) in range(11):
            if tv.ligada:
                controle.mudarCanal(tv, int(resp))
            else:
                print("Televisão Desligada")
        elif resp == 'x':
            break       
        else:
            chamarFuncoes(resp)


def chamarFuncoes(resp):
    match resp:
        case "l":
            return controle.ligarTv(tv)
        case "o":
            return controle.desligarTv(tv)
        case "+":
            return controle.aumentarVolume(tv)
        case "-":
            return controle.diminuirVolume(tv)
        case _:
            return print('**ERRO**')


def interacaoTeclado(numero):
    match numero:
        case "l":
            return controle.ligarTv(tv)
        case "o":
            return controle.desligarTv(tv)
        case "+":
            return controle.aumentarVolume(tv)
        case "-":
            return controle.diminuirVolume(tv)
        case _:
            return print('**ERRO**')


menu()