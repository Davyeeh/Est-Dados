#Importando a TAD pilha sequencial implementada na questão 1
from questao_1 import Stack

############################### QUESTÃO 3 ###############################
#Implementar um programa que faça conversões de números inteiros na base 10 para outras bases

# ITEM A: Conversão do decimal inserido para números binários
def conversao_binario(num_dec_converter):
    #Verifica se o número é zero, caso sim, retorna '0'
    if num_dec_converter == 0:
        return '0'
    pilha = Stack(100)  #pilha criada localmente para evitar interferências globais
    restos_binarios = []
    
    while num_dec_converter > 0:
        resto = num_dec_converter % 2
        pilha.empilha(resto)
        num_dec_converter //= 2

    while not pilha.pilha_eh_vazia():
        restos_binarios.append(pilha.desempilha())

    #Cada número inteiro vira um caractere string e é concatenado
    return ''.join(map(str, restos_binarios))

# ITEM B: Conversão do decimal inserido para números octonais
def conversao_octonais(num_dec_converter):
    if num_dec_converter == 0:
        return '0'
    pilha = Stack(100)
    restos_octonais = []
    
    while num_dec_converter > 0:
        resto = num_dec_converter % 8
        pilha.empilha(resto)
        num_dec_converter //= 8

    while not pilha.pilha_eh_vazia():
        restos_octonais.append(pilha.desempilha())

    #Cada número inteiro vira um caractere string e é concatenado
    return ''.join(map(str, restos_octonais))

# ITEM C: Conversão do decimal inserido para números hexadecimais
def conversao_hexadecimal(num_dec_converter):
    if num_dec_converter == 0:
        return '0'
    pilha = Stack(100)
    restos_hexadecimais = []
    #Essa string representa todos os números utilizados na conversão para o hexadecimal
    #onde A = 10, e vai aumentando de 1 até o F = 15
    hex_chars = "0123456789ABCDEF"
    
    while num_dec_converter > 0:
        resto = num_dec_converter % 16
        pilha.empilha(resto)
        num_dec_converter //= 16

    while not pilha.pilha_eh_vazia():
        #Aqui os elementos já vêm como string e são concatenados diretamente
        restos_hexadecimais.append(hex_chars[pilha.desempilha()])

    return ''.join(restos_hexadecimais)

# Programa principal
try:
    #Entrada do usuário para conversão
    num_dec_converter = int(input("Digite o número decimal desejado a ser convertido: "))
    base_desejada = input("Digite a base desejada para que se converta (binario, octal ou hexadecimal): ").strip().lower()

    #Verifica qual base foi escolhida e realiza a conversão correspondente
    if base_desejada == 'binario':
        print(f"O número decimal {num_dec_converter} em binário é {conversao_binario(num_dec_converter)}")
    elif base_desejada == 'octal':
        print(f"O número decimal {num_dec_converter} em octal é {conversao_octonais(num_dec_converter)}")
    elif base_desejada == 'hexadecimal':
        print(f"O número decimal {num_dec_converter} em hexadecimal é {conversao_hexadecimal(num_dec_converter)}")
    else:
        print("Base desconhecida. Escolha entre binario, octal ou hexadecimal.")
except ValueError:
    #Captura entradas inválidas e informa o usuário
    print("Entrada inválida. Certifique-se de digitar um número decimal válido.")



















