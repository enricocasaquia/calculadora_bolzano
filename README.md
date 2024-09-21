# Cálculo de Funções e Raízes Usando Intervalos e Iterações

Este repositório contém um script em Python que realiza o cálculo de três diferentes funções, determinando a raiz de uma função selecionada em um intervalo definido pelo usuário, utilizando o método da bisseção e calculando o número de iterações com base no erro aceito.

## Funções Incluídas

O código implementa três funções matemáticas, cada uma representando um exercício:

- **Função 1**: \( f_1(x) = \sqrt{5 - x} - 2^{x-1} \)
- **Função 2**: \( f_2(x) = \ln(3x - 1) + 2x \)
- **Função 3**: \( f_3(x) = x + 5 \ln(x) - 2 \)

O usuário pode escolher qual função deseja calcular e, em seguida, o intervalo inicial, final e o erro aceito para determinar o número de iterações necessárias para encontrar a raiz dentro do intervalo.

## Requisitos

Este script foi desenvolvido em Python e depende da biblioteca `math`. Certifique-se de que o Python está instalado e que a biblioteca necessária esteja disponível.

Para instalar o Python e a biblioteca `math`, basta seguir os passos abaixo:

1. Instale o Python (https://www.python.org/downloads/).
2. A biblioteca `math` já está incluída na instalação padrão do Python.

## Execução do Script

Para executar o script, basta rodar o seguinte comando no terminal:

python main.py

Ao rodar o script, o usuário será solicitado a:

1. Escolher a função para calcular (`f1`, `f2` ou `f3`).
2. Inserir o valor inicial e final do intervalo.
3. Inserir o valor do erro aceito.

O script calculará o número de iterações (valor de \(K\)) e exibirá uma tabela detalhada com os seguintes dados em cada iteração:

- \( K \) (Número da iteração)
- \( a \) (Limite inferior do intervalo)
- \( b \) (Limite superior do intervalo)
- Média do intervalo
- Valor da função aplicada em \( a \) e na média
- Sinal (positivo ou negativo)
- Erro (diferença entre \( b \) e \( a \))

Ao final das iterações, o intervalo em que a raiz está localizada será exibido.

### Exemplo de Saída

Escolha qual exercício deseja calcular: (f1,f2,f3): f2  
Digite o valor inicial do intervalo: 1.0  
Digite o valor final do intervalo: 2.0  
Digite o valor do erro aceito: 0.001

O intervalo será |1.00,2.00|.  
O valor do K é 10 iterações.

 K  |    a     |    b     |   média   |   f(a)   |  f(média) | sinal |   erro  
 0  | 1.000000 | 2.000000 | 1.500000  | 0.000000 | 0.512134  |   +   | 1.000000

A raiz está entre o intervalo [1.78125;1.81250].  
Aperte ENTER para encerrar...

## Geração de Executável

O script foi convertido em um executável (.exe) utilizando a biblioteca **PyInstaller**, permitindo sua execução direta sem a necessidade de um ambiente Python.

### Como gerar o arquivo executável:

1. Instale o **PyInstaller**:

pip install pyinstaller

2. Navegue até o diretório do script e execute o comando:

pyinstaller --onefile main.py

Isso irá gerar um executável na pasta `dist/`, que pode ser distribuído para execução sem a necessidade de Python.

## Licença

Este projeto está licenciado sob os termos da [MIT License].
