#Pequena explicação
print("Cofre")
#Guarda o valor da senha
senha = 2002
#Pedir a entrada/senha
tentativa = int(input("Digite a senha: "))
#Verifica se a senha colocada pelo usuário é a senha correta, caso não, pedir a senha novamente
while tentativa != senha:
    print("Senha Invalida")
    tentativa = int(input("Digite a senha: "))
#Caso a senha colocada pelo usuário for a senha correta finalizar o código
print("Acesso permitido")