# Altura da galera - Peça o nome e a altura (em metros) de 5 pessoas.
# Inicializando as variáveis que vão armazenar: a maior e menor altura, e os seus respetivos nomes associados
maior_altura = 0
menor_altura = 0
nome_maior_altura = ''
nome_menor_altura = ''
soma_alturas = 0    # Soma total das alturas para calcular a média
acima_180 = 0       # Contador para alturas acima de 1.80m
# Loop para registrar os nomes e as alturas das pessoas
for p in range(1, 6):
    # Solicita o nome a altura da pessoa
    nome = input(f'Informe o {p}º nome da pessoa: ')
    altura = float(input(f'Informe sua altura: '))
    print('-' * 40)
    soma_alturas += altura  # Somando a altura para cálculo da média depois
    if altura > 1.80:       # Verificando se a pessoa tem mais de 1.80m
        acima_180 += 1
    # Na primeira pessoa, define o nome e a altura da mais alta e mais baixa
    if p == 1:
        maior_altura = altura
        menor_altura = altura
        nome_maior_altura = nome
        nome_menor_altura = nome
    else:
        # Atualiza a altura e o nome da pessoa, se for a menor
        if altura < menor_altura:
            menor_altura = altura
            nome_menor_altura = nome
        # Atualiza a altura e o nome, se for maior
        if altura > maior_altura:
            maior_altura = altura
            nome_maior_altura = nome
# Cálculo da média de altura
media_altura = soma_alturas / 5
# Exibe o resultado
print('=' * 60)
print(f'{nome_maior_altura} foi a pessoa mais alta com {maior_altura:.2f}m.')
print(f'{nome_menor_altura} foi a pessoa mais baixa com {menor_altura:.2f}m.')
print(f'A média de altura foi de {media_altura:.2f}m.')
print(f'{acima_180} pessoa(s) têm mais de 1.80m.')
