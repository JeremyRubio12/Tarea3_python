a = 2
b = []
while a > 0:
 a = int(input("Introduce todos tus numeros: "))
 if a > 0:
    b.append(a)
 if a < 1:
     print("Hasta aqui llegado la suma debido que ya introducido un numero negativo o igual a cero\n")
     def suma(b):
         resultado = 0
         for i in b:
             resultado = resultado + i
         return resultado


     print("Este es el resultado de todos los numeros sumados: ", suma(b))



