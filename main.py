import math

# Cada função representa um exercício.
def funcao1(x):
    return (math.sqrt(5-x) - 2**(x-1))
def funcao2(x):
    return (math.log(3*x - 1) + 2*x)
def funcao3(x):
    return (x + 5*math.log(x,2.71828)- 2)

dicionario = {'f1':funcao1,'f2':funcao2,'f3':funcao3}

# Input dos valores para preparar o cálculo.
escolha = input('\nEscolha qual exercício deseja calcular: (f1,f2,f3): ')
def funcao(x):
    return dicionario[escolha](x)

a = float(input('\nDigite o valor inicial do intervalo: '))
b = float(input('Digite o valor final do intervalo: '))
print(f'\nO intervalo será |{a:.2f},{b:.2f}|.')
e = float(input('\nDigite o valor do erro aceito: '))

# Cálculo do K para definir o número de iterações.
def calcular_K(a, b, e):
    return (math.log10(b - a) - math.log10(e)) / math.log10(2)
K = math.ceil(calcular_K(a, b, e)) #Utilizamos 'ceil' porque é necessário arredondar para cima.
print(f'\nO valor do K é {K} iterações.')

# Cabeçalho da tabela.
print(f'{"K":^3} | {"a":^9} | {"b":^9} | {"média":^9} | {"f(a)":^9} | {"f(média)":^10} | {"sinal":^5} | {"erro":^9}')

# Calcula e gera a tabela
def calcular_iteracao(a, b, e, k=0, c=0):
    cont_raiz = c
    a_aplicado = funcao(a)
    media = (a + b) / 2
    media_aplicada = funcao(media)
    
    if a_aplicado * media_aplicada > 0:
        sinal = '+'
    else:
        sinal = '-'
    
    print(f'{k:^3} | {a:^9.6f} | {b:^9.6f} | {media:^9.6f} | {a_aplicado:^9.6f} | {media_aplicada:^10.6f} | {sinal:^5} | {b - a:^9.6f}')
    
    if sinal == '+':
        intervalo_raiz = f'\nA raiz está entre o intervalo [{a:.5f};{b:.5f}].'
        a = media
    else:
        intervalo_raiz = f'\nA raiz está entre o intervalo [{a:.5f};{b:.5f}].'
        cont_raiz += 1
        b = media
        
    if k == K:
        print(intervalo_raiz)
        input('\nAperte ENTER para encerrar..')
        exit()
    elif sinal == '-':
        calcular_iteracao(a, b, e, k + 1, cont_raiz)
    else:
        calcular_iteracao(a, b, e, k + 1, cont_raiz)
        
# Chama a função principal
calcular_iteracao(a, b, e)