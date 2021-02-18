print("Convertir numeros a letras del 0 al 9")
b = ["A","B","C","D","F","G","H","I","J","K"]
numero = int(input("Introduce tu numero del 0 al 9: "))
if numero == 0:
    print("\nEste es tu numero en letras: ",b[0])
if numero == 1:
    print("\nEste es tu numero en letras: ",b[1])
if numero == 2:
    print("\nEste es tu numero en letras: ",b[2])
if numero == 3:
    print("\nEste es tu numero en letras: ",b[3])
if numero == 4:
    print("\nEste es tu numero en letras: ",b[4])
if numero == 5:
    print("\nEste es tu numero en letras: ",b[5])
if numero == 6:
    print("\nEste es tu numero en letras: ",b[6])
if numero == 7:
    print("\nEste es tu numero en letras: ",b[7])
if numero == 8:
    print("\nEste es tu numero en letras: ",b[8])
if numero == 9:
    print("\nEste es tu numero en letras: ",b[9])
elif numero > 9 or numero < 0:
    print("\nEste numero no esta entre 0 o 9.")