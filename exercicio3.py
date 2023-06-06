nota1 = float (input("Digite a 1ª nota:"))
nota2 = float (input("Digite a 2ª nota:"))
nota3 = float (input("Digite a 3ª nota:"))
nota4 = float (input("Digite a 4ª nota:"))

media = (nota1+nota2+nota3+nota4)/4

print("Sua média é",media)

if media >= 7 :
    print("Você foi aprovado")

elif media == 6.5 :
    print("Você está de recuperação6")

else:
    print("você foi reprovado")