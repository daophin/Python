# Curos em Vídeo de Python
# Exercício 6 – Dobro, Triplo, Raiz Quadrada
msg1 = 'DESAFIO 006 - DOBRO, TRIPLO, RAÍZ QUADRADA'
msg2 = '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
print(msg2)
print(msg1)
print(msg2)
num = int(input('DIGITE UM VALOR INTEIRO QUALQUER: '))
dobro = num * 2
triplo = num * 3
raizq = num ** (1/2)
print(f'O VALOR INSERIDO FOI {num}')
print(f'O DOBRO DE {num} = {dobro}')
print(f'O TRIPLO DE {num} = {triplo}')
print(f'RAÍZ QUADRADA DE {num} = {raizq:.2f}')
