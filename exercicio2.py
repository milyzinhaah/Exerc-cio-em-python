total_horas = int(input("Digite a quantidade de horas: "))

dias = total_horas // 24
horas_restantes = total_horas % 24

print (f"{total_horas} horas equivalem a {dias} dia(s) e {horas_restantes} hora(s).")
