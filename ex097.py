# criando um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def write(msg):
    size = len(msg) +6
    print('=' * size)
    print(f'  {msg}')
    print('=' * size)


write('Arnaldo')
write('Texto adaptável')