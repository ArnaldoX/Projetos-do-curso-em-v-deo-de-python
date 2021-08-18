#Criando um programa que tenha a função chamada área,
# que receba as dimensões de um terreno retangular(largura, e comprimento), que mostre a área do terreno.

def area(larg,comp):
    a = larg * comp
    print(f'A área do terreno é {larg} x {comp} é de {a}m²')


print('='*30)
print('\033[1;36mControle tamanho de terrenos')
print('='*30)
larg = float(input('Qual a largura do terreno?em m²: '))
comp = float(input('Qual o comprimento do terreno?em m² '))
area(larg,comp)


