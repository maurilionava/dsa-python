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
"""
Gestão de Estoque: Crie uma lista chamada produtos.
    Peça para o usuário inserir 3 produtos.
    Remova o segundo item da lista.
    Adicione o produto "Monitor" na primeira posição (index 0).
    Exiba a lista final e o total de itens nela.
"""
def gestao_estoque():
    produtos = []
    index_remocao = 1
    contador = 0

    for i in range(3):
        produtos.append(input(f"Informe o produto {i+1}:"))

    print(f"Produto removido da posição {index_remocao+1}: {produtos.pop(index_remocao)}")

    produtos.insert(0, "Monitor")
    print(f"Adicionado o produto 'Monitor' na primeira posição da lista")

    print(f"Quantidade de itens na lista: {len(produtos)}")

    for produto in produtos:
        print(produto)

"""
Proteção de Dados (Tuplas): Crie uma tupla que armazene as coordenadas geográficas (latitude, longitude) de um quartel. Tente alterar um dos valores da tupla via código e trate o erro (ou explique por que o Python impede essa ação com base no conceito de imutabilidade).
"""
def protecao_de_dados():
    cerrado_coords = (1,2)
    
    for i in range(2):
        print(cerrado_coords[i])

    try:
        cerrado_coords[0] = 3
    except:
        print("[Exception] Tratando erro ao tentar alterar valor de tupla")

"""
Desafio do Hardware (Simulado): Escreva um programa que receba uma frase e crie uma lista contendo o código ASCII de cada caractere da frase.
Dica: Utilize a função ord() para converter o caractere em número.
"""
def converter_para_ascii():
    entrada = input("Informe uma frase:")
    lista_ascii = []

    for i in entrada:
        lista_ascii.append(ord(i))

    print(f"{lista_ascii}")

"""
Filtro de Acesso: Crie uma lista de tuplas, onde cada tupla contém (nome, idade). Use um laço de repetição e operadores lógicos para exibir apenas o nome das pessoas que possuem mais de 18 anos e cujo nome começa com a letra "A".
"""
def filtrar_acessos():
    contador = 0
    usuarios = [
        ("Andre", 20),
        ("Ana", 17),
        ("Alice", 25),
        ("Arthur", 15),
        ("Beatriz", 22),
        ("Amanda", 16),
        ("Antonio", 60),
        ("Caio", 12),
        ("Aline", 18),
        ("Bruno", 30),
        ("Augusto", 14),
        ("Daniela", 19),
        ("Agatha", 13),
        ("Alberto", 45),
        ("Eduardo", 10)
    ]

    for usuario in usuarios:
        if usuario[0].startswith('A') and usuario[1] >= 18:
            print(usuario)
            contador += 1

    print(f"Quantidade de usuários com inicial A e maiores de 18: {contador}")