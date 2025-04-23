# nota2_soma = 1


# informe = int(input('informe a primeira nota '))
# informe2 = int(input('informe a segunda nota '))

# resultado = (informe + informe) / 2
# print(f'Media:{resultado}')

# if resultado >= 5:
#    print(f'aprovado sua nota e:{resultado}')
# else:
#     print(f'reprovado, sua nota e:{resultado}')


# # Verificar se a média é 6 ou mais e informar sobre diploma
# if resultado >= 6:
#     print('Você terá diploma!')


soma = 0

for i in range(1, 4):
    nota = int(input(f'Sua nota {i}:'))

    soma = soma + nota
    
print(f'Sua nota final e: {soma / 3}')

if nota == 5:
  print(f'Aprovado sua nota e: {nota}, esta nota e uma media!')

elif nota > 5:
  print(f'Aprovado sua nota e: {nota}, voce ultrapassou media!')

else:
  print(f'reprovado, sua nota e: {nota}. Com esta nota não foi possivel atinger a nota minima, desta forma reprovado. Segue abaixa as intruções:')