#Escreva um algoritmo para ler dois valores (considere que não serão lidos valores iguais)
# e escrevê-los em ordem crescente

n1=float(input("digite o primeiro numero: "))
n2=float(input("digite o segundo numero: "))

if n1>n2:
  print(f"A sequencia crescente é {n2}, {n1}.")
else:
  print(f"A sequencia crescente é {n1}, {n2}.")
