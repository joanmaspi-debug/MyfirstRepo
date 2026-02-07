

#Here we ask the first number
print("Disme un num del 1 al 10")
num = int(input())


while num > 10 or num < 1:
    print("El num no és del 1 al 10", "Torna a provar")
    
    num = int(input())



print("Què vols fer amb el número?", "sumar, restar, dividir o multiplicar")
operacio = (input())

if operacio == "suma":
    print("Disme el numero el qual vols sumar")
    num_2 = int(input())
    while num_2 < 1 or num_2 > 10:
        print("Ha de ser de l'1 al 10, torna-ho a intentar")
        num_2 = int(input())
    resultat = num + num_2
    print("El resultat és :", resultat)




elif operacio == "restar":
    print("Disme el numero que vols restar")
    num_2 = int(input())
    while num_2 < 1 or num_2 > 10:
        print("Ha de ser de l'1 al 10, torna-ho a intentar")
        num_2 = int(input())
    resultat = num - num_2
    print("El resultat és", resultat)


elif operacio == "dividir":
    print("Disme el numero que vols dividir")
    num_2 = int(input())
    while num_2 < 1 or num_2 > 10:
        print("Ha de ser de l'1 al 10, torna-ho a intentar")
        num_2 = int(input())
    resultat = num / num_2
    print("El resultat és", resultat)

elif operacio == "multiplicar":
    print("Disme el numero que vols multiplicar")
    num_2 = int(input())
    while num_2 < 1 or num_2 > 10:
        print("Ha de ser de l'1 al 10, torna-ho a intentar")
        num_2 = int(input())
    resultat = num * num_2
    print("El resultat és", resultat)













