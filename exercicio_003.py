#Exercício 003  
#Digitar 2 valores e informar qual é o maior.
valor_01 = input('Digite o primeiro valor: ')
valor_02 = input('Digite o segundo valor: ')

int_valor_01 = int(valor_01)
int_valor_02 = int(valor_02)

if int_valor_01 >= int_valor_02:
    print(f'Valor 01 - {int_valor_01:.2f} - '
          f'é maior ou igual que o valor 2 - {int_valor_02:.2f} - ')
elif int_valor_01 <= int_valor_02:
    print(f'Valor 02 - {int_valor_02:.2f} - '
          f'é maior que o valor 1 - {int_valor_01:.2f} - ')
