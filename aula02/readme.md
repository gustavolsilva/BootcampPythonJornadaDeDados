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

