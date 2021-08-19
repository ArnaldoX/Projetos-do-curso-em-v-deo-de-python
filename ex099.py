#criando um programa que tenha uma função chamada maior(),
#que receba vários parâmetros com valores inteiros.

def maior():
    lista = list()
    c = 0
    while True:
        n = int(input('\033[1;93m[000] para parar\nDigite um número:'))
        if n == 000:
            break
        else:
            lista.append(n)
            if n >= c:
                c = n
            else:
                c = c
    print(lista)
    print(f'Foram ao todo {len(lista)} números. ')
    print(f'O maior valor é {c}.')


maior()



