from sys import argv, exit

# Ler o valor passado como primeiro argumento do programa
# Há uma tentativa de conversão para inteiro, que decide continuar o programa ou não
# Além disso, verifica se o número está compreendido entre 0 e 255 (incluindo os limites)
try:
    decimal = int(argv[1])
    if decimal < 0 or decimal > 255:
        raise ValueError
except ValueError:
    print('Por favor, informe como parâmetro um número decimal entre 0 e 255.')
    exit()

# Com o número decimal dentro dos limites, o programa avança normalmente
print('Número decimal: ' + str(decimal))

# A string do número binário começa vazia
binario = ''

# Usando laço de repetição para os oito bits
# A função range cria uma lista de 8 elementos,
# sendo 7 (sete) o primeiro (limite incluído)
# e 0 (zero) o último (limite não incluído)
# Detalhe para o passo (step) negativo para ordem descrescente
for digito in range(7, -1, -1):
    resto = decimal - pow(2, digito)
    if resto >= 0:
        binario = binario + '1'
        decimal = decimal - pow(2, digito)
    else:
        binario = binario + '0'

# Apresentação do resultado final
print('Convertido para binário: ' + binario)

# Converter de binário para decimal
decimal = 0

# Usando laço de repetição para fazer a prova real
# de binário para decimal
# Detalhe para a sequência de dígitos que é inversa à potência de 2 (dois)
# por isso o uso de valor absoluto (módulo) do número
for digito in range(0, 8, 1):
    if binario[digito] == '1':
        decimal = decimal + pow(2, abs(digito - 7))

# Apresentação da prova real
print('Convertido de volta para decimal: ' + str(decimal))
