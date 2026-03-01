#Nível 1: Operadores Lógicos e Variáveis (Simples)
def verificar_login():
    usuario_sistema = "admin"
    senha_sistema = "123"

    usuario = input("Informe o nome do usuário: ")
    senha = input("Informe a senha do usuário: ")

    if usuario==usuario_sistema and senha==senha_sistema:
        print("Usuário identificado")
    else:
        print("Usuário não reconhecido")

def verificar_intervalo():
    numero = int(input("Informe um número: "))

    if numero >= 10 and numero <= 50:
        print(f"O número {numero} está entre o intervalo de 10 e 50")
    else:
        print(f"O número {numero} não está entre o intervalo de 10 e 50")

def identificador_de_objetos():
    l1 = [1,2]
    l2 = [1,2]

    print(f"l1 == l2 ? {l1==l2}") #Resultado: True. O sistema compara os valores nas listas
    print(f"l1 is l2 ? {l1 is l2}") #Resultado: False. O sistema compara os endereços de memória
    
    print(f"ID l1: {id(l1)}")
    print(f"ID l2: {id(l2)}")

    l2 = l1 # Atribuição por referência e atuação do Garbage Collector na referência anterior do l2
    print(f"l1 is l2 ? {l1 is l2}") #Resultado: False. O sistema compara os endereços de memória

    print(f"ID l1: {id(l1)}")
    print(f"ID l2: {id(l2)}")

#Nível 2: Strings e Sequências (Intermédio)
def analisar_nome():
    nome = input("Informe seu nome completo: ")

    print(f"Maiúsculo: {nome.upper()}")
    print(f"Quantidade de caracteres: {len(nome)}")
    print(f"Primeiro nome: {nome.split(' ')[0]}")
    print(f"Inverso: {nome[::-1]}") # Inverter string

def validar_dominio():
    email = input("Informme um endereço de email válido:")

    if "@" in email:
        print("Email válido")
    else:
        print("Email inválido")

#Nível 3: Listas, Tuplas e Memória (Complexo)
