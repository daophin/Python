# Curos em Vídeo de Python
# Exercício 4 - dissecando uma variável

var = input('Digite algo: ')
tipo = type(var)
print(f'O tipo primitivo desse valor é {tipo}')
numerico = var.isnumeric()
alfabetico = var.isalpha()
alfanumerico = var.isalnum()
espaco = var.isspace()
maiuscula = var.isupper()
minuscula = var.islower()
print(f'É um número? {numerico}')
print(f'É alfabético? {alfabetico}')
print(f'Só tem espaços {espaco}')
print(f'É alphanumérico? {alfanumerico}')
print(f'Está em letras maiúsculas? {maiuscula}')
print(f'Está em letras minúsculas? {minuscula}')
