# NÍVEL 1: LÓGICA E SEQUENCIAL (SIMPLES)
# ALGORITMO DO CAFE
def ferver_agua():
    print("Fervendo agua")

def colocar_po_no_coador():
    print("Colocando po no coador")

def passar_cafe():
    print("Despejando agua fervente no coador")
    
def preparar_cafe():
    """
    Realizar o passo a passo do preparo de um cafe
    """
    print("Iniciando preparo do cafe")

    FerverAgua()
    ColocarPoNoCoador()
    PassarCafe()

    print("Preparo do cafe finalizado")

# CALCULADORA DE AREA
def calcular_area_retangulo():
    """
    Calcular a area de um retângulo a partir de sua base e altura

    Args:
        Base do retângulo (float)
        Altura do retângulo (float)

    Returns:
        Area (float)
    """
    print("Iniciando calculo da area de um retangulo")

    base = eval(input("Informe a base do retângulo: "))
    altura = eval(input("Informe a altura do retângulo: "))

    area = base * altura

    print(f"Base: {base} Altura: {altura} Area: {area}")

    print("Fim do calculo de area do retangulo")

def dobrar_e_triplicar():
    """
    Imprimi o dobro e o triplo de um número digitado pelo usuário
    """
    print("Iniciando função dobrar e triplicar entrada")

    entrada = eval(input("Informe um número: "))

    if type(entrada) is int:
        print(f"Entrada: {entrada} Dobro: {entrada * 2} Triplo: {entrada * 3}")
    else:
        print("O valor de entrada não é do tipo inteiro.")

    print("Finalizando a execução da função")

# NÍVEL 2: CONDICIONAIS E OPERADORES (INTERMEDIÁRIO)
def par_ou_impar():
    """
    Determina se o número informado pelo usuário é par ou ímpar
    """

    entrada = int(input("Informe um número inteiro: "))

    # TODO: IMPLEMENTAR VALIDAÇÃO DE TIPO
    if entrada % 2 == 0:
        print(f"O número {entrada} é par")
    else:
        print(f"O número {entrada} é ímpar")

    print("Encerrando execução da função")

def converter_temperatura():
    """
    Converte a temperatura de Celsius para Fahrenheit a partir da entrada do usuário
    """

    celsius = int(input("Informe a temperatura em Celsius: "))

    fahrenheit = celsius * 1.8 + 32

    print(f"Celsius: {celsius}ºC Fahrenheit: {fahrenheit}ºF")

from datetime import date

def verificar_maioridade():
    ano_de_nascimento = int(input("Informe seu ano de nascimento: "))

    idade = date.today().year - ano_de_nascimento

    if idade >= 18:
        print("Você é obrigado a votar")
    elif idade >= 16:
        print("Você já pode votar, porém ainda não é obrigatório")
    else:
        print("Você ainda não tem idade para votar")

# Nível 3: Repetição e Bibliotecas (Complexo)
def media_harmonica():
    """
    A média harmônica é o inverso da média dos inversos
    """

    valor_01 = int(input("Informe o primeiro valor: "))
    valor_02 = int(input("Informe o segundo valor: "))
    valor_03 = int(input("Informe o terceiro valor: "))

    media_harmonica = 3/(1/valor_01 + 1/valor_02 + 1/valor_03)

    print(f"Media harmônica dos números {valor_01}, {valor_02}, {valor_03} = {media_harmonica:.2f}")

def classificar_triangulos():
    """
    Classifica se um triângulo é válido e determina seu tipo
    """

    # Recebe os valores informados pelo usuário
    a = int(input("Informe o primeiro valor:"))
    b = int(input("Informe o segundo valor:"))
    c = int(input("Informe o terceiro valor:"))

    # Valida a formação de um triângulo
    if not(a+b > c and b+c > a and a+c > b):
        print("Os valores informados não formam um triângulo")
        return None
    
    if a==b and b==c:
        print("Equilátero: todos os lados são iguais")
    elif a==b or b==c or a==c:
        print("Isósceles: possui dois lados iguais")
    elif a!=b and b!=c and c!=a:
        print("Escaleno: todos os lados são diferentes")
    else:
        print("Erro de lógica")

def caixa_eletronico():
    valor_saque = int(input("Informe o valor de saque: R$"))
    valor_saque_aux = valor_saque

    valor_saque_aux = dividir_notas(50, valor_saque_aux)
    valor_saque_aux = dividir_notas(20, valor_saque_aux)
    valor_saque_aux = dividir_notas(10, valor_saque_aux)

def dividir_notas(valor, valor_saque_aux):
    if valor_saque_aux >= valor:
        aux = valor_saque_aux // valor
        valor_saque_aux = valor_saque_aux - (valor * aux)
        print(f"Notas de {valor} {aux}")
        return valor_saque_aux