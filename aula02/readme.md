## Aula 02 | TypeError, Type Check, Type Conversion, try-except e if

### 1. Tipos Primitivos

Variáveis são espaços na memória designados para armazenar dados que podem ser modificados durante a execução de um programa. Em Python, a declaração de variáveis é dinâmica, o que significa que o tipo de dado é inferido durante a atribuição.

<b>Exemplo em Python:</b> <br>
Python suporta vários tipos de dados simples, tais como:
- Inteiros (int): Números inteiros, positivos ou negativos, sem casas decimais.
- Ponto flutuante (float): Números reais, positivos ou negativos, com casas decimais.
- Strings (str): Sequências de caracteres, delimitadas por aspas simples ou duplas.
- Booleanos (bool): Valores lógicos, que podem ser Verdadeiro (True) ou Falso (False).

#### 1.1 Inteiros (int) <br>
* <b> Métodos e operações </b><br>
    i. `+` - Adição <br>
    ii. `-` - Subtração <br>
    iii. `*` - Multiplicação <br>
    iv. `//` - Divisão inteira <br>
    v. `%` - Módulo (resto da divisão) <br>

#### 1.2 Ponto flutuante (float)
* <b> Métodos e operações </b><br>
    i. `+` - Adição <br>
    ii. `-` - Subtração <br>
    iii. `*` - Multiplicação <br>
    iv. `/` - Divisão <br>
    v. `**` - Potênciação

#### 1.3 Strings (str)
* <b> Métodos e operações </b><br>
    i. `.upper()` - Converte a string para letras maiúsculas<br>
    ii. `.lower()` - Converte a string para letras minúsculas<br>
    iii. `.strip()` - Remove espaços em branco do início e do fim da string <br>
    iv. `.strip(sep)` - divide a string em uma lista de substrings, usando `sep` como delimitador<br>
    v. `+` - Concatenação de duas strings

#### 1.4 Booleanos (bool)
* <b> Operações Lógicas </b><br>
    i. `and` - Operador lógico "E"<br>
    ii. `or` - Operador lógico "OU"<br>
    iii. `not` - Operador lógico "NÃO"<br>
    iv. `==` - Igualdade<br>
    v. `!=` - Diferença

### Exercícios

<b> Inteiros (int) </b>

1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

<b> Números de Ponto flutuante (float) </b>

6. Escreva um programa que receba dois números flutuantes e realize sua adição.

7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

<b> Strings (str) </b>

11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

<b> Booleanos (bool) </b>

16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

### TypeError, Type Check, Type Conversion em Python
Python é uma linguagem de programção dinâmica, mas fortemente tipada, o que signifca que não é necessário declarar tipo de variáveis explicitamente, mas o tipo de uma variável é determinado pelo valor que ela armazena. Isso introduz a necessidade de compreender como Python lida com diferentes tipos de dados, especialmente quando se trata de operações que envolvem múltiplos tipos. Vamos explorar três conceitos importantes: `TypeError`, verificação de tipo (`Type Check`) e conversão de tipo (`Type Conversion`).

### TypeError
Um `TypeError` ocorre em Python quando uma operação ou função é aplicada a um objeto de tipo inadequado. Python não sabe como aplicar a operação porque os tipos de dados não são compatíveis.

#### Exemplo de TypeError
Um exemplo clássico é tentar utilizar a função `len()` em um número inteiro, o que resulta em um `TypeError` pois `len()` espera um objeto iterável, como uma string, lista ou tupla, não um inteiro.

```python
# Exemplo de TypeError
try:
    resultado = len(5)
except TypeError as e:
    print(f"Erro: {e}") # Imprime a mensagem de erro
```

O código acima tenta obter o comprimento de um inteiro, o que não faz sentido, resultando na mensagem de erro "object of type 'int' has no len()".

### Type Check
Verificação de tipo (`Type Check`) é o processo de verificar o tipo de uma variável. Isso pode ser útil para garantir que operações ou funções sejam aplicadas apenas a tipos de dados compatíveis, evitando erros em tempo de execução.

#### Exemplo de Type Check
Para verificar o tipo de uma variável em Python, você pode usar a função `type()` ou o operador `isinstance()`. 

```python
# Exemplo de Type Check
numero = 10
if isinstance(numero, int):
    print("A variável é inteiro.")
else:
    print("A variável não é um inteiro.")
```
Esse código verifica se `numero` é uma instância `int` e imprime uma mensagem apropriada.

### Type Conversion
Conversão de tipo (`Type Conversion`), também conhecinda como casting, é o processo de converter o valor de uma variável de um tipo para outro. Python oferece várias funções intergradas para realizar conversões explícitas de tipo, como `int()`, `float()`, `str()`, entre outras.

#### Exemplo de Type Conversion
Se você quiser somar um inteiro e um número flutuante, pode ser necdessário converter o inteiro para flutuante ou vice-versa para garantir a operação de soma seja realizada corretamente.

```python
# Exemplo de Type Conversion
numero_inteiro = 5
numero_flutuante = 2.5
# Converte o inteiro para flutuante e realiza a soma
resultado = float(numero_inteiro) + numero_flutuante
print(f"O resultado da soma é: {resultado}")  # Imprime: O resultado da soma é: 7.5
```
#### try-except
A estrutura `try-except` é usada para tratamento de exceções em Python. Uma exceção é um erro que ocorre durante a execução do programa e que, se não tratado, interrompe o fluxo normal do programa e termina sua execução. O tratamento de exceções permite que o programa lide com erros de maneira elegante, permitindo que continue a execução ou falhe de forma controlada.
* **try:** Este bloco é o primeiro na estrutura de tratamento de exceções. Python tenta executar o código dentro deste bloco.
* **except:** se uma exceção ocorrer no bloco `try`, a execução imediatamente salata para o bloco `except`. Aqui, você pode especificar tipos de exceção específicas para capturar e tratar apenas essas exceções. Se nenhum tipo de exceção for especificado, ele captura todas as exceções.
* **else:** Este bloco é opcional e executa se o bloco `try` não gerar nenhuma exceção. É útil para código que deve ser executado apenas quando não há erros.
* **finally:** Este bloco é opcional e sempre executa, independentemente de uma exceção ter ocorrido ou não. É útil para liberar recursos, como fechar arquivos ou conexões de banco de dados.

#### Exemplo de try-except
```python
# Exemplo de try-except
try:
    # Código que pode terar uma exceção
    resultado = 10 / 0  # Isso causará uma exceção de divisão por zero
except ZeroDivisionError as e:
    # Código que executa se a exceção ZeroDivisionError ocorrer
    print(f"Divisão por zero não é permitida")  # Imprime a mensagem de erro
except Exception as e:
    # Código que executa para qualquer outra exceção
    print(f"Ocorreu um erro: {e}")  # Imprime a mensagem de erro genérica
else:
    # Código que executa se não houver exceção
    print(f"O resultado é: {resultado}")  # Imprime o resultado da operação
finally:
    # Código que sempre executa, independentemente de uma exceção ter ocorrido ou não
    print("Fim do tratamento de exceção")  # Imprime mensagem de finalização
```
#### if
O `if` é uma estrutura de controle de fluxo que permite ao programa executar diferentes ações com base em diferentes condições. Se a condição avaliada pelo `if` for verdadeira (`True`), o bloco de código identado sobe ele será executado. Se a condição for falsa (`False`), o bloco de código será ignorado.
* **if:** Avalia uma condição. Se a condição for verdadeira, executa o bloco de código associado.
* **elif:** abreviação de "else if". Permite verificar múltiplas condições em sequencia.
* **else:** Executa um bloco de código se todas as condições anteriores no `if` e `elif` forem falsas.

#### Exemplo de if
```python
# Exemplo de if
idade = 18
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Exatamente 18 anos")
else:
    print("Maior de idade")
```
Ambas estruturas, `try-except` e `if`, são fundamentais para o criação de programas em Python que são capazes de lidar com situações inesperadas (como erros de execução) e tomar decisões com base em condições, permitindo assim que você construa programas mais robustos, flexíveis e seguros.

### Exercícios
Aqui estão cinco exercícios que envolvem  `TypeError`, verificação de tipo (`Type Check`), o uso de  `try-except` e a utilização da estrutura condicional `if`. Esses exercícios aumentam progressivamente em dificuldade e abordam situações práticas onde você pode aplicar esses conceitos.

**Exercício 21: Conversor de Temperatura**
Escreva um programa que converta a temperatura em Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando `try-except`, garantir que a entrada seja numérica, tratando qualquer `ValueError`. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

**Exercício 22: Verificação de Palindromo**
Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuaões). Use `try-except` para garantir que a entrada seja uma string. Dica: Utilize a função `isinstance()` para verificar o tipo de entrada.

**Exercício 23: Calculadora Simples**
Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (`+`, `-`, `*`, `/`) do usuário. Use `try-except` para lidar com divisões por zero e entradas não númericas. Utilize `if-elif-else` para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

**Exercício 24: Classificador de Números**
Escreva um programa que solicite ao usuário para digitar um número. Utilize `try-except` para assegurar que a entrada seja numérica e utilize `if-elif-else` para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

**Exercício 25: Conversão de Tipo com Validação**
Crie um script que solicite ao usuário uma lista de números separados por virgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize `try-except` para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão falhar ou um elemento não for inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

## Desafio - Refatorar o projeto da aula anterior evitando bugs!

Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas para um número de ponto flutuante e prevenção de valores negativos para salário e bônus, você pode modificar o código diretamente. Isso envolve adicionar verificações adicionais após a tentativa de conversão para garantir que os valores sejam positivos.

![alt text](img\image.png)

