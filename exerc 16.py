#Escreva um algoritmo para ler a hora de início e a hora de fim de um jogo de Xadrez
# (considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em horas,
# sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar
# em um dia e terminar no dia seguinte.

duraçao=24
inicio=int(input("digite a hora inicio: "))
fim=int(input("digite a hora fim: "))
if inicio > fim:
  duraçao=(24-inicio)+fim
else:
  duraçao=fim-inicio
print(f"a duração foi de {duraçao} horas")
