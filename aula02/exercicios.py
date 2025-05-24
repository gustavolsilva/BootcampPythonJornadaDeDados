# %%
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print("A soma é:", soma)
# %%
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = int(input("Digite um número: "))
resto = num % 5
print("O resto da divisão por 5 é:", resto)
# %%
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
produto = num1 * num2
print("O produto é:", produto)
# %%
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
divisao_inteira = num1 // num2
print("A divisão inteira é:", divisao_inteira)

# %%
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num = int(input("Digite um número: "))
quadrado = num ** 2
print("O quadrado é:", quadrado)

# %%
#6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print("A soma é:", soma)

# %%
#7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
media = (num1 + num2) / 2
print("A média é:", media)
# %%
#8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
potencia = base ** expoente
print("A potência é:", potencia)
# %%
#9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("A temperatura em Fahrenheit é:", fahrenheit)
# %%
#10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio do círculo: "))
area = 3.14 * raio ** 2
print("A área do círculo é:", area)

# %%
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string = input("Digite uma string: ")
string_maiuscula = string.upper()
print("A string em maiúsculas é:", string_maiuscula)
# %%
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = input("Digite seu nome completo: ")
print("O nome em minúsculas é:", nome_completo.lower())

# %%
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
print("A frase sem espaços em branco é:", frase.strip())

# %%
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data (dd/mm/aaaa): ")
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

# %%
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
print("A string concatenada é:", string1 + string2)

# %%
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
bool1 = input("Digite o primeiro valor booleano (True/False): ")
bool2 = input("Digite o segundo valor booleano (True/False): ")
bool1 = bool(bool1)
bool2 = bool(bool2)
resultado = bool1 and bool2
print("O resultado da operação AND é:", resultado)

# %%
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
bool1 = input("Digite o primeiro valor booleano (True/False): ")
bool2 = input("Digite o segundo valor booleano (True/False): ")
bool1 = bool(bool1)
bool2 = bool(bool2)
resultado = bool1 or bool2
print("O resultado da operação OR é:", resultado)

# %%
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
bool1 = input("Digite um valor booleano (True/False): ")
bool1 = bool(bool1)
resultado = not bool1
print("O valor invertido é:", resultado)

# %%
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = num1 == num2
print("Os números são iguais:", resultado)

# %%
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = num1 != num2
print("Os números são diferentes:", resultado)
# %%
