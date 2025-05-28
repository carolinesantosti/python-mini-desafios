 # Minidesafio 2 - Temperatura extrema
 # Peça a temperatura registrada em 7 cidades diferentes.

# Inicializando as variáveis que vão armazenar:
# a maior e menor temperatura, e a soma total das temperaturas
maior_temperatura = 0
menor_temperatura = 0
total_temperatura = 0

# Loop para registrar a temperatura de 7 cidades
for t in range(1, 8):
    # Solicita a temperatura da cidade atual
    temperatura = float(input(f'A temperatura da {t}ª cidade: '))

    # Soma a temperatura atual ao total
    total_temperatura += temperatura

    # Na primeira cidade, define a temperatura como maior e menor
    if t == 1:
         maior_temperatura = temperatura
         menor_temperatura = temperatura
    else:
        #Atualiza a maior temperatura, se a atual for maior
        if temperatura < menor_temperatura:
             menor_temperatura = temperatura
        # Atualiza a menor temperatura, se a atual for menor
        if temperatura > maior_temperatura:
             maior_temperatura = temperatura

# Calcula a média das temperaturas
media_temperatura = total_temperatura / 7

# Exibe o resultado das temperaturas
print('=' * 40)
print(f'🔥A maior temperatura foi de {maior_temperatura:.1f} graus.')
print(f'❄️A menor temperatura foi de {menor_temperatura:.1f} graus.')
print(f'📊A temperatura média de todas as cidades foi de {media_temperatura:.1f} graus.')
print('~' * 20, 'Fim do Programa', '=' * 20 )
