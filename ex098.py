# criando um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.

from time import sleep
def contador (i,f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i <= f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ',flush=True)
            sleep(0.5)
            cont -= p

#Programa principal
contador(0, 20, 5)
print('\033[1;94mAgora é a sua vez de personalizar o contador! ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)

