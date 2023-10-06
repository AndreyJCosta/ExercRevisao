#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00
# se forem compradas pelo menos 12. Escreva um programa que leia
#o número de maçãs compradas, calcule e escreva o custo total da compra.

print("      Promoção do Dia")
print("1 maçã é 1,30 a partir de 12 sai a 1,00")
print()
Total=0
quant=int(input("digite a quantidade de maças: "))
print()
if quant < 12:
  total = quant * 1.30

else:
  total= quant * 1.0

print(f"O custo total da compra é de {total}")
