#FUNÇÃO PARA CALCULAR O TOTAL DE VENDAS DE TODOS OS PRODUTOS NA LISTA

#FUNÇÃO PARA VERIFICAR SE EXISTE ALGUMA QUANTIDADE NEGATIVA OU ZERADA E AVISAR AO USUARIO
def validação_de_preços(vendas):
    for venda in vendas:
        if venda["preco"] <= 0:
            print(f"ERRO! O preço de {venda['item']} esta negativo ou zera")

def validação_de_quantidade(vendas):
    for venda in vendas:
        if venda["quantidade"] <= 0:
            print(f"ERRO! A quantidade de {venda['item']} está negativa ou zerada.")
        
def calcular_total(vendas):
    total_de_vendas = 0
    for venda in vendas:
        total_de_vendas += venda["quantidade"] * venda["preco"]
        #CALCULANDO E ADCIONANDO ESSE VALOR AO TOTAL QUE INICIA COM 0. Depois de calcular o valor total, o resultado é acrescido a variavel total_de_vendas
    
    return total_de_vendas
#FUNÇÃO PARA CALCULAR A MEDIA DE VENDAS DA LOJA POR PRODUTO
def calcular_media(vendas):
    tamanho = len(vendas)
    total_de_vendas = calcular_total(vendas)
    media = total_de_vendas / tamanho
    media = round(media, 2) #AQUI ESTOU LIMITANDO A MEDIA DE VENDAS PARA DUAS CASAS DECIMAIS
    return media


vendas = [
    {"item": "camiseta", "quantidade": 10, "preco": 20.0},
    {"item": "calça", "quantidade": 5, "preco": 50.0},
    {"item": "meia", "quantidade": 20, "preco": 5.0},
    {"item": "tênis", "quantidade": 2, "preco": 100.0},
    {"item": "boné", "quantidade": 7, "preco": 15.0},
    {"item": "jaqueta", "quantidade": 3, "preco": 150.0},
    {"item": "bermuda", "quantidade": 8, "preco": 30.0},
    {"item": "cinto", "quantidade": 6, "preco": 25.0},
    {"item": "blusa", "quantidade": 9, "preco": 35.0},
    {"item": "shorts", "quantidade": 11, "preco": 25.0},
    {"item": "sapato", "quantidade": 4, "preco": 120.0},
    {"item": "jaqueta de couro", "quantidade": 1, "preco": 250.0},
    {"item": "mochila", "quantidade": 15, "preco": 80.0},
    {"item": "óculos de sol", "quantidade": 10, "preco": 60.0},
    {"item": "pulseira", "quantidade": 18, "preco": 12.0},
    {"item": "bolsa", "quantidade": 7, "preco": 45.0},
    {"item": "camisa social", "quantidade": 12, "preco": 55.0},
    {"item": "jaqueta jeans", "quantidade": 5, "preco": 90.0},
    {"item": "vestido", "quantidade": 8, "preco": 120.0},
    {"item": "blusão de lã", "quantidade": 3, "preco": 80.0},
    {"item": "tenis esportivo", "quantidade": 6, "preco": 110.0},
    {"item": "bermuda de praia", "quantidade": 14, "preco": 40.0},
    {"item": "chapeu", "quantidade": 9, "preco": 20.0},
    {"item": "jaqueta impermeável", "quantidade": 4, "preco": 180.0},
]

erro = validação_de_quantidade(vendas) #VERIFICANDO SE A ALGUM ITEM NEGATIVO OU ZERADO
erro2 = validação_de_preços(vendas) #VERIFICANDO SE ALGUM PREÇO ESTA NEGATIVO OU ZERADO


print('Esse é o valor total de vendas de todos os produtos: R$',calcular_total(vendas))
print("Essa é a media de vendas por produto: R$",calcular_media(vendas),"\n")
item_mais_vendido = max(vendas, key=lambda venda: venda["quantidade"])
#Uso a função key para orientar a função max a calcular o valor baseado na 'quantidade' dentro da lista
#print('Esse é o item mais vendido:', item_mais_vendido)                 

print(f"Esse é o item mais vendido: {item_mais_vendido['item']}")
print(f"Quantidade vendida: {item_mais_vendido['quantidade']}")
print(f"Preço unitário: R${item_mais_vendido['preco']}\n")
#Outra forma de mostrar o iten mais vendido de forma clean. Puxando itens da lista separadamente, mas usando a função para puxar as informações do item mais vendido.

item_mais_vendido = min(vendas, key=lambda venda: venda["quantidade"])

print(f"Esse é o item menos vendido: {item_mais_vendido['item']}")
print(f"Quantidade vendida: {item_mais_vendido['quantidade']}")
print(f"Preço unitário: R${item_mais_vendido['preco']}")
