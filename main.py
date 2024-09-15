import math

a = float(input('Digite o valor inicial do intervalo: '))
b = float(input('Digite o valor final do intervalo: '))
print(f'\nO intervalo será |{a},{b}|.')

e = float(input('\nDigite o valor do erro aceito: '))

# Exemplo usando x.log(x)-1
def funcao(x):
    return (x * math.log10(x)) - 1
    
def calcular_K(a, b, e):
    return (math.log10(b - a) - math.log10(e)) / math.log10(2)
K = math.ceil(calcular_K(a, b, e)) #Utilizamos 'ceil' porque é necessário arredondar para cima.
print(f'O valor do K é {K} iterações.')

print('K |    a    |    b    |  média  |   f(a)   | f(média) | sinal | erro |')
def calcular_iteracao(a, b, e, k=0, c=0):
    cont_raiz = c
    a_aplicado = funcao(a)
    media = (a + b) / 2
    media_aplicada = funcao(media)
    
    if a_aplicado * media_aplicada > 0:
        sinal = '+'
    else:
        sinal = '-'
    
    print(f'{k} | {a:.5f} | {b:.5f} | {media:.5f} | {a_aplicado:.5f} | {media_aplicada:.5f} |  {sinal}  | {b - a:.5f}')
    
    if sinal == '+':
        a = media
    else:
        cont_raiz += 1
        b = media
        
    if k == K:
        print('Fim')
        print(f'A quantidade de raízes encontradas é igual a {cont_raiz}.')
    elif sinal == '-':
        calcular_iteracao(a, b, e, k + 1, cont_raiz)
    else:
        calcular_iteracao(a, b, e, k + 1, cont_raiz)
        
calcular_iteracao(a, b, e)