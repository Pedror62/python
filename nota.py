from builtins import input
# O programa pede para o usuário informar o nome de um produto, seu preço e a quantidade comprada.

def _produto():
    produt = input(f'Qual e o produto? ')
    valor = float(input(f'qual e o valor do produto? '))
    quntidade = float(input(f'Qual e a quantidade comprada? '))
    return produt, valor, quntidade

# Com essas informações, o programa calcula o valor total da compra (multiplicando o preço pela quantidade).
def somaProduto(produt, valor, quntidade):
   somar = valor * quntidade
   print(f"\n valor o produto e: {valor}")
   print(f"\n Serão: {quntidade}")
   print(f"\n Voce escolheu o produto: {produt}")
   print(f"\n O preço de cada produto é: R$ {valor}")
   print(f"\n O valor total da compra é: {somar}")
produt, valor, quntidade = _produto()
somaProduto(produt, valor, quntidade)
# Se o cliente comprar mais de três itens, o programa aplica um desconto de 10% no valor total.

def _desconto(valor, quntidade):
    valor = valor * quntidade
    if quntidade >= 3:
        desconto = valor * 10/100
        novovalor = valor - desconto
        print(f'voce tem desconto de 10%')
        print(f'\n O novo valor e de {novovalor}')
    else:
        print (f'Sem desconto pois voce fez somente {quntidade}')
 
_desconto(valor, quntidade)