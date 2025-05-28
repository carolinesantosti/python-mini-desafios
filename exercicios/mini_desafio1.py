# A Corrida - Peça o nome e o tempo (em minutos) que 5 corredores levaram para completar uma prova.
# Inicializando as variáveis
tempo_mais_alto = 0
tempo_mais_baixo = 0
recorde = 0
nome_mais_rapido = ''
nome_mais_lento = ''
# Loop para registrar os corredores e o tempo
for i in range(1, 6):
    print(f'{i}º corredor:')
    nome = input('Digite seu nome: ').upper()
    tempo = float(input('Digite seu tempo: '))
    recorde += tempo      # Soma o tempo atual ao total
    print('-' * 30)
    # Se for o primeiro corredor, inicializa as variáveis com os valores dele
    if i == 1:
        tempo_mais_baixo = tempo
        tempo_mais_alto = tempo
        nome_mais_rapido = nome
        nome_mais_lento = nome
    else:
        # Se o tempo atual for menor que o mais baixo registrado, atualiza o mais rápido
        if tempo < tempo_mais_baixo:
            tempo_mais_baixo = tempo
            nome_mais_rapido = nome
        # Se o tempo atual for maior que o mais alto registrado, atualiza o mais lento
        if tempo > tempo_mais_alto:
            tempo_mais_alto = tempo
            nome_mais_lento = nome
# Calcula a média dos tempos
media_tempo = recorde / 5
# Exibe o resultado
print(f'{nome_mais_rapido} fez o tempo mais rápido de {tempo_mais_baixo}minutos.')
print(f'{nome_mais_lento} fez o tempo mais lento e seu tempo foi {tempo_mais_alto}minutos.')
print(f'A média de tempo dos corredores foi {media_tempo:.2f}minutos.')
