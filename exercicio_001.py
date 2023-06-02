#Exercício 001

nome = 'Georgeo'
sobrenome = 'Nocera'
idade= int(47)
ano_nasc = int(2023 - idade)
maior_idade = bool(idade >= 18)
altura = float(1.73)
print('Nome:',nome)
print('Sobrenome:',sobrenome)
print('Idade:',idade)
print('Ano de Nascimento:',ano_nasc)
if maior_idade == True:
    print('Maior de Idade: Sim')
else:
    print('Maior de Idade: Não')
print('Altura em Metros:',altura)
