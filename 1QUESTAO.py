#Pequena explicação
print("Saiba quanto de impostos você precisa pagar")
#Pedir a entrada/salário
salario = float(input("Digite seu salário: "))
#Se o valor for menor que 0 pedir que o usuário digite a entrada/salário novamente
while salario < 0:
    print("\nDigite um salário válido.")
    salario = float(input("Digite seu salário: "))
#Verificar se o valor está entre 0R$ e 2000R$ e fazer as ações necessárias.
if salario <= 2000:
    print('Insento')
#Verificar se o valor está entre 2000R$ e 3000R$ e fazer as ações necessárias.
elif salario > 2000 and salario < 3000.01: 
    print(f"R$ {salario*(8/100):.2f}")
#Verificar se o valor está entre 3000R$ e 4500R$ e fazer as ações necessárias.
elif salario > 3000 and salario < 4500.01:
    print(f"R$ {salario*(18/100):.2f}")
#Verificar se o valor é maior que 4500R$ e fazer as ações necessárias.
else:
    print(f"R$ {salario*(28/100):.2f}")