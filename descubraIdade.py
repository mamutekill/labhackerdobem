print("Em que ano você nasceu?")
nascimento=input()
nascimento=int(nascimento)

print("Vc quer descobrir sua idade em que ano?")
ano=input()
ano=int(ano)

if ano-nascimento <= 120:
    print("Em",ano,"você tera",ano-nascimento,"anos")
else:
    print("Acho que vc não vai viver até os",ano-nascimento,"anos")
