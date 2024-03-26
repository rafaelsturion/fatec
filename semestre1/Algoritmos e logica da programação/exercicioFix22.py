compra1 = int(input("Digite o valor da primeira compra: "))
compra2 = int(input("Digite o valor da segunda compra: "))
compra3 = int(input("Digite o valor da terceira compra: "))

def calcular_desconto(valor):
    if valor > 300:
        return valor * 0.8 # 20% de desconto
    elif valor > 200:
        return valor * 0.85 # 15% de desconto
    elif valor > 100:
        return valor * 0.9 # 10% de desconto
    else:
        return valor    # sem desconto
    

total = compra1 + compra2 + compra3
total_com_desconto = calcular_desconto(compra1) + calcular_desconto(compra2) + calcular_desconto(compra3)

print("RA 1051392411012, Nome: João Rafael Sturion Mantoanelli, Turma I DSM")
print("O valor total de suas compras é: ", total)
print("O valor total de suas compras com desconto é: ", total_com_desconto)