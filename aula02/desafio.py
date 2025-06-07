"""
Para resolver os bugs identificados — tratamento de entradas inválidas que não podem 
ser convertidas para um número de ponto flutuante e prevenção de valores negativos para 
salário e bônus, você pode modificar o código diretamente. Isso envolve adicionar verificações 
adicionais após a tentativa de conversão para garantir que os valores sejam positivos.
"""
# %%
CONSTANTE_BONUS = 1000
salario = 0.0
bonus = 0.0
# Solicita ao usuário que digite o seu nome
try:
    nome = input("Digite o seu nome: ")

    # Verifica se o nome está vazio
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    # Verifica se há nuúmeros no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não pode conter números.")
    else:
        print(f"Nome válido: Olá, {nome}!")
except ValueError as e:
    print(f"Erro: {e}")

# Solicita ao usuário que digite o valor do seu salário e converte para float
try:
    salario = float(input("Digite o valor do seu salário: "))
    
    # Verifica se o salário é negativo
    if salario < 0:
        raise ValueError("Por favor, digite um valor positivo para o salário.")
except ValueError as e:
    print(f"Erro: {e}")

# Solicita ao usuário que digite o valor do seu bônus e converte para float

try:
    bonus = float(input("Digite o valor do seu bônus: "))
    
    # Verifica se o bônus é negativo
    if bonus < 0:
        raise ValueError("Por favor, digite um valor positivo para o bônus.")
except ValueError as e:
    print(f"Entrada inválida para o bônus. Por favor, digite um número.")

# Assumindo uma lógica de cálculo para o bônus final e KPI

bonus_final = bonus * 1.2 # Exemplo de cálculo, ajuste conforme necessário
kpi = (salario + bonus_final) / 1000  # Exemplo de cálculo de KPI, ajuste conforme necessário

# Imprime as informações para o usuário
print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome}, seu salário é R$ {salario:.2f} e seu bônus final é R$ {bonus_final:.2f}.")
# %%
