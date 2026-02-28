# NÍVEL 1: LÓGICA E SEQUENCIAL (SIMPLES)
# ALGORITMO DO CAFE
def FerverAgua():
    print("Fervendo agua")

def ColocarPoNoCoador():
    print("Colocando po no coador")

def PassarCafe():
    print("Despejando agua fervente no coador")
    
def PrepararCafe():
    """
    Realizar o passo a passo do preparo de um cafe
    """
    print("Iniciando preparo do cafe")

    FerverAgua()
    ColocarPoNoCoador()
    PassarCafe()

    print("Preparo do cafe finalizado")

#PrepararCafe()

# CALCULADORA DE AREA
def CalcularAreaRetangulo():
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

#CalcularAreaRetangulo()

def DobrarTriplicar():
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

#DobrarTriplicar()

# NÍVEL 2: CONDICIONAIS E OPERADORES (INTERMEDIÁRIO)
def ParOuImpar():
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

ParOuImpar()