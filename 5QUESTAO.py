#Pequena explicação
print("Contagem de valores pares")
#Criação da lista "numeros" e da variável "par"
numeros = []
par=0
#Repete uma ação 5 vezes
for i in range(0,5):
#Pede que o usuário coloque um número
    numero = int(input(f'Digite o {i+1}° número: '))
#Se o número for par adicionar 1 a variável "par"
    if numero % 2 == 0:
        par = par+1
#Mostra quantos números pares existem na lista
print(f"{par} valores pares")