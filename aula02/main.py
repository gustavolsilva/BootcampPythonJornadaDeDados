# %%
# Exemplo de TypeError
nome = "Gustavo"
try: # Tenta executar o código
    resultado = len(3)
except TypeError as e: # Captura o erro de tipo
    print(f"Erro: {e}") # Imprime a mensagem de erro
else: # Executado se não houver erro
    print(f"Tudo Ocorreu bem")
finally: # Sempre executado
    print("O importante é participar!")
# %%
# Exemplo de Type Check
numero = int(input("Insira um numero: "))
if isinstance(numero, int):
    print(f"A variável é um inteiro!")
else:
    print(f"A variável não é um inteiro!")

# %%

idade = 16
IDADE_MINIMA = 18

if idade < IDADE_MINIMA:
    print("Não pode dirigir ainda!")
elif idade == IDADE_MINIMA:
    print("Pode tirar a carteira de motorista!")
else:
    print("Pode dirigir!")
