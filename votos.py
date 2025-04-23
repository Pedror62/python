nome = input(f' Qual e o seu nome? ')
idade = int(input(f'Qual a sua idade? '))

if idade < 18:
    print(f'{nome} Voce não pode votar')
elif idade >= 18 and idade <= 64:
    print(f'{nome} Voce pode votar!')
    print(f'Mas o voto e opcional!')
