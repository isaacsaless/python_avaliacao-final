#Pequena explicação
print("Descubra a média de valores positivos.")
#Criação da lista "numeros" e da variável "positivo"
numeros = []
positivo=0
#Repete uma ação 5 vezes
for i in range(0,5):
#Pede um valor para ser armazenado em na variável "numero"
    numero = float(input(f'Digite o {i+1}° número: '))
#Se o número for maior que 0 adicionar 1 na variável positivo, colocar ele na lista "numeros"
    if numero>0:
        positivo = positivo+1
        numeros.append(numero)
#Soma todos os números da lista "numeros"
soma = sum(numeros)
#Mostra a quantidade de valores positivos
print(f"{positivo} valores positivos")
#Mostra a média da lista "numeros"
print(f"{soma/5}")