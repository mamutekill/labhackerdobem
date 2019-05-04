from random import *

print("Gerador de cumprimentos")
print("--------------------")

adjetivos = [ "maravilhoso" , "acima da media" , "exelente" ]
hobbies = [ "andar de bicicleta" , "programar" , "fazer cha"]

nome = input("Qual e o meu nome?: ")
print( "Aqui esta o seu cumprimento" , nome , ":" )
              
#imprima um item aleatoria da lista 'cumprimentos'
print(nome , "voce e" , choice(adjetivos) , "em" , choice(hobbies) )
print("de nada" )
