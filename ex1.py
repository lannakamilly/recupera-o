# Flávia Glenda e Lanna Kamilly 
def questao_teste_mesa(n1, n2):
    while n1 != n2:
        if n1 < n2: 
            n2 = n2 - n1
        else: 
            n1 = n1 - n2  # Corrigir lógica para alterar n1 adequadamente
    return n1  # Corrigir para retornar o valor final de n1 ou n2 (são iguais)

print(questao_teste_mesa(40, 5))
