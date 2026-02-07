#Es defineix variable com a tipo int(numeros enters) y s'imprimeix
iq_primera_variable = 100
print(iq_primera_variable)

#Es defineix una variable com a tipo int i s'imprimeix el tipus
la_int_variable = 5
print(type(la_int_variable))

#Es cree una variable que sigui la anterior que era de tipo int y la transforma en string
#Despres s'imprimeix el tipus de variable que es i com l'hem transformat en string sera string
transformar_int_variable_to_string_variable = str(la_int_variable)
print(type(transformar_int_variable_to_string_variable))

print("5" and "5")


esta_lloviendo = False

if esta_lloviendo:
    print("Lleva paraguas")
else:
    print("Sal tranquilo, no llueve")



esta_plovent = input('Esta plovent? (Si / No)')

esta_plovent_si = (esta_plovent == 'Si')

print (esta_plovent_si)
