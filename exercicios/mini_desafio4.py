# Mini-desafio: Cálculo de médias de alunos
# Este programa lê nome e duas notas de 4 alunos e informa:
# - A média de cada aluno
# - A maior e a menor média
# - Quantos alunos tiveram média maior ou igual a 7

# Inicializa as variáveis para rastrear as maiores e menores médias, e os alunos aprovados
maior_media = 0
menor_media = 0
aprovados = 0
nome_menor_media = ''
nome_maior_media = ''

for i in range(1, 5):
    print('-' * 30)
    print(f'{i}º aluno')
    # Solicita dados do aluno
    nome = input('Informe seu nome: ')
    nota1 = float(input('Sua primeira nota: '))
    nota2 = float(input('Sua segunda nota: '))
    # Calcula a média do aluno
    media_aluno = (nota1 + nota2) / 2
    print(f'A média de {nome} foi {media_aluno:.2f}')
    # Verifica se o aluno está aprovado
    if media_aluno >= 7:
        aprovados += 1
    # Na primeira iteração, define a maior e menor média com os dados do primeiro aluno
    if i == 1:
        menor_media = media_aluno
        maior_media = media_aluno
        nome_menor_media = nome
        nome_maior_media = nome
    else:
        # Atualiza a maior média, se necessário
        if media_aluno > maior_media:
            maior_media = media_aluno
            nome_maior_media = nome
        # Atualiza a menor média, se necessário
        if media_aluno < menor_media:
            menor_media = media_aluno
            nome_menor_media = nome

# Exibe os resultados após processar todos os alunos
print(f'O(a) aluno(a) que teve a MENOR MÉDIA foi o(a) {nome_menor_media}, com a média de {menor_media:.2f}.')
print(f'O(a) aluno(a) que teve a MAIOR MÉDIA foi o(a) {nome_maior_media}, com a média de {maior_media:.2f}.')
print(f'✅Tivemos um total de {aprovados} APROVADOS!!!')

