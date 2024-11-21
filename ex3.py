# Flávia Glenda e Lanna Kamilly
peso = float(input("Quantos quilos Vegeta pescou? "))

limite = 40
valor_multa_por_quilo = 6.00

if peso > limite:
    excesso = peso - limite
    multa = excesso * valor_multa_por_quilo
else:
    excesso = 0
    multa = 0

print(f"Peso total pescado: {peso} kg")
if excesso > 0:
    print(f"Excesso de peso: {excesso} kg")
    print(f"Multa a pagar: R$ {multa:.2f}")
else:
    print("Nenhum excesso. Sem multa.")
