# Exercício 6: Calcular Fatorial

while True:
    try:
        numero = int(input("Digite um número inteiro não negativo para calcular o fatorial: "))
        if numero >= 0:
            break
        else:
            print("O número deve ser não negativo.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Inicializa o resultado do fatorial
# O fatorial de 0 é 1
fatorial = 1

# Inicializa o contador para o loop de cálculo
contador = numero

# Usa o loop while para calcular o fatorial
while contador > 1:
    fatorial = fatorial * contador
    contador -= 1

print("-" * 30)
print(f"O fatorial de {numero}! é: **{fatorial}**")
print("-" * 30)