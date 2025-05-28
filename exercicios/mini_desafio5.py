# Mini-desafio 5: Compras no Supermercado
# Esse programa pede ao usuário o nome e o preço de 5 produtos e mostra:
# - O total gasto
# - O produto mais barato
# - Quantos produtos custaram mais de R$100

# Inicializa as variáveis para rastrear o total gasto, o menor preço, nome do produto e o contador de produtos
total = 0
preco_mais_barato = 0
nome_mais_barato = ''
acima_de_100 = 0

for i in range(1, 6):
    print('=' * 30)
    print(f'{i}º produto')
    #Solicita os dados do produto
    produto = input('Informe o nome do produto: ')
    preco = float(input('Valor: R$'))
    # Soma o total dos preços
    total += preco
    # Verifica os preços acima de R$100
    if preco > 100:
        acima_de_100 += 1
    # Verifica o produto mais barato
    if i == 1 or preco < preco_mais_barato:
        preco_mais_barato = preco
        nome_mais_barato = produto
# Exibe o resultado
print('=' * 30)
print(f'O total gasto na compra foi de R${total:.2f}.')
print(f'O produto mais barato foi: {nome_mais_barato}, que custou R${preco_mais_barato}.')
print(f'{acima_de_100} produtos custaram mais de R$100.')