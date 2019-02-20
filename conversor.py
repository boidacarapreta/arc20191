# Valores iniciais: um valor decimal a ser convertido para binário
decimal = 80
print('Número decimal: ' + str(decimal))

# A string do número binário começa vazia
binario = ''

# Cálculo do primeiro dígito: 2^7
doisnasete = decimal - 128
if doisnasete >= 0:
    binario = binario + '1'
    decimal = decimal - 128
else:
    binario = binario + '0'

# Cálculo do segundo dígito: 2^6
doisnaseis = decimal - 64
if doisnaseis >= 0:
    binario = binario + '1'
    decimal = decimal - 64
else:
    binario = binario + '0'

# Cálculo do terceiro dígito: 2^5
doisnacinco = decimal - 32
if doisnacinco >= 0:
    binario = binario + '1'
    decimal = decimal - 32
else:
    binario = binario + '0'

# Cálculo do quarto dígito: 2^4
doisnaquatro = decimal - 16
if doisnaquatro >= 0:
    binario = binario + '1'
    decimal = decimal - 16
else:
    binario = binario + '0'

# Cálculo do quinto dígito: 2^3
doisnatres = decimal - 8
if doisnatres >= 0:
    binario = binario + '1'
    decimal = decimal - 8
else:
    binario = binario + '0'

# Cálculo do sexto dígito: 2^2
doisnadois = decimal - 4
if doisnadois >= 0:
    binario = binario + '1'
    decimal = decimal - 4
else:
    binario = binario + '0'

# Cálculo do sétimo dígito: 2^1
doisnaum = decimal - 2
if doisnaum >= 0:
    binario = binario + '1'
    decimal = decimal - 2
else:
    binario = binario + '0'

# Cálculo do oitavo dígito: 2^0
doisnazero = decimal - 1
if doisnazero >= 0:
    binario = binario + '1'
    decimal = decimal - 1
else:
    binario = binario + '0'

# Apresentação do resultado final
print('Convertido para binário: ' + binario)

# Converter de binário para decimal
decimal = 0

# Cálculo do primeiro dígito: 2^7
# Se a posição 0 (zero) do número binário for 1 (um), adiciona 128 (2^7)
if binario[0] == '1':
    decimal = decimal + 128

# Cálculo do segundo dígito: 2^6
if binario[1] == '1':
    decimal = decimal + 64

# Cálculo do terceiro dígito: 2^5
if binario[2] == '1':
    decimal = decimal + 32

# Cálculo do quarto dígito: 2^4
if binario[3] == '1':
    decimal = decimal + 16

# Cálculo do quinto dígito: 2^3
if binario[4] == '1':
    decimal = decimal + 8

# Cálculo do sexto dígito: 2^2
if binario[5] == '1':
    decimal = decimal + 4

# Cálculo do sétimo dígito: 2^1
if binario[6] == '1':
    decimal = decimal + 2

# Cálculo do oitavo dígito: 2^0
if binario[7] == '1':
    decimal = decimal + 1

# Apresentação da prova real
print('Convertido de volta para decimal: ' + str(decimal))
