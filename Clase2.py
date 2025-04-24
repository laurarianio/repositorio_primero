#mIngrese nombre, apellido, edad y correo electronico y muestrelo por pantalla
nombre = input("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
correo = input ("Ingrese su correo electrónico: ")
# Impresion de datos
separador = "-" * 50
print (separador)
print ("\tNombre: \t",nombre,apellido)
print ("\tEdad:   \t",edad)
print ("\tE-mail: \t",correo)
print (separador)



# No es lo que pide. Se mejora validando la edad
# nombre = input("Ingrese su nombre: ")
# apellido = input ("Ingrese su apellido: ")
# edad = input ("Ingrese su edad: ")
# correo = input ("Ingrese su correo electrónico: ")
# # Impresion de datos
# print ("-----------------------------------------")
# print ("    Nombre: \t",nombre,apellido)
# if edad.isdigit() and int(edad) > 0 and int(edad) < 120:
#     print ("    Edad:   \t",edad)
# else:
#     print ("    Edad:   \t Edad no valida")
# print ("    E-mail: \t",correo)
# print ("-----------------------------------------")