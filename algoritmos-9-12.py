#Nível 1: Tipos e Conversões (Simples)
"""
Exploração de Objetos: Crie três variáveis: uma com um número inteiro, outra com um número real e outra com uma frase. Use a função type() para imprimir o tipo de cada uma e o id() para exibir o endereço de memória desses objetos.
"""
def tipos_e_conversoes():
    valores = [1, 0.5, "hello world"]

    for valor in valores:
        print(f"Tipo: {type(valor)} ID: {id(valor)}")

# tipos_e_conversoes()
"""
Conversor de Tipos: Peça para o usuário digitar um número decimal (float). Converta esse número para inteiro e exiba o resultado. Em seguida, pegue um número inteiro e converta-o para string, concatenando com a frase " é o meu número da sorte".
"""
def converter_float_para_int():
    e_float = float(input("Informe um número decimal:"))
    e_int = int(e_float)
    e_str = str(e_int)

    print(f"Número convertido de float: {e_float} para int: {e_int}")

    print(f"{e_str} é o meu número da sorte")

# converter_float_para_int()

"""
Soma de Strings: O que acontece se você tentar somar duas entradas do input() sem convertê-las? Crie um código que demonstre isso e depois corrija-o para que realize a soma aritmética real.
"""
def soma_string():
    e_1 = input("Informe um número:")
    e_2 = input("Informe outro número:")

    soma = e_1 + e_2

    print(f"Soma sem conversão entre {e_1} e {e_2} = {soma}")

    e_1_int = int(e_1)
    e_2_int = int(e_2)
    soma_int = e_1_int + e_2_int

    print(f"Soma após conversão entre {e_1} e {e_2} = {soma_int}")

# soma_string()

#Nível 2: Biblioteca Padrão e Matemática (Intermédio)
"""
Sorteio Aleatório: Importe a biblioteca random. Crie um programa que gere um número aleatório entre 1 e 100 e peça para o usuário tentar adivinhar. (Dica: use random.randint()).
"""
from random import randint

def criar_numero_aleatorio():
    numero_aleatorio = randint(1,100)

    input_usuario = int(input("Adivinhe o número! Arrisque um número entre 1 e 100:"))

    if input_usuario < numero_aleatorio:
        print(f"Seu palpite foi menor do que o número sorteado. Número sorteado: {numero_aleatorio}")
    elif input_usuario > numero_aleatorio:
        print(f"Seu palpite foi maior do que o número sorteado. Número sorteado: {numero_aleatorio}")
    else:
        print(f"Parabéns você acertou o número sorteado. Número sorteado: {numero_aleatorio}")

#criar_numero_aleatorio()

"""
Calculadora Científica: Utilizando a biblioteca math, peça um número ao usuário e exiba:
    O logaritmo de base 10 desse número.
    O valor do fatorial desse número.
    O valor do seno e cosseno (lembre-se de converter para radianos se necessário).
"""
import math

def math_lab():
    input_usuario = int(input("Informe um número:"))

    print(f"Log base 10: {math.log10(input_usuario)}")
    print(f"Fatorial: {math.factorial(input_usuario)}")
    print(f"Seno: {math.sin(input_usuario)}")
    print(f"Cosseno: {math.cos(input_usuario)}")

#math_lab()

"""
Simulação de Lançamento: Crie um programa que simule o lançamento de um dado de 6 faces 10 vezes (use um laço for). Ao final, mostre a soma de todos os valores obtidos.
"""
import random

def soma_sorte():
    dado = list(range(1,7))
    soma = 0

    for i in range(10):
        numero_aleatorio = random.choice(dado)
        soma += numero_aleatorio
        print(f"Numero aleatório: {numero_aleatorio}")
        print(f"soma lançamento {i}:{soma}")

soma_sorte()
#Nível 3: Funções Avançadas e Integração (Complexo)
"""
Calculadora Dinâmica com eval(): Crie um programa que receba uma expressão matemática inteira como string do usuário (ex: "2 + 5 * 3") e utilize a função eval() para exibir o resultado calculado.
Desafio: Adicione um aviso sobre os riscos de segurança ao usar o eval().
"""

"""
Análise de Dataset Fictício: Imagine que você está preparando dados para sua pós em IA.
    Importe random.
    Crie uma lista com 10 números flutuantes aleatórios representando "pesos" de um modelo.
    Use funções como sum(), len(), min() e max() para descrever esse pequeno conjunto de dados.
"""

"""
Interação com o Sistema: Crie um script .py que pergunte o nome do usuário, sua idade e sua profissão. O programa deve calcular em que ano o usuário completará 100 anos e salvar essa informação em uma string formatada (f-string), exibindo-a com destaque no terminal.
"""

"""
Otimização de Memória: Explique (em comentários no código) a diferença entre uma conversão implícita e explícita. Crie um exemplo onde uma divisão de dois inteiros resulta em um float (implícita) e onde você força o resultado a ser inteiro (explícita).
"""