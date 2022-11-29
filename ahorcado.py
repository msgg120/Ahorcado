import random
import os 
palabras = ["USA", "MEXICO", "CANADA", "BRASIL", 
"ARGENTINA", "COREA", "URUGUAY", "ALEMANIA", "BELGICA", "CAMERUN"]
palabra = list(random.choice(palabras))

horca = ["     l====N",
         "          N",
         "          N",
         "          N",
         "          N",
         "          N",
         "          N",
         " _________N"]

ahorcado = ["     l====N",
            "     o     N",
            "   / l \   N",
            "   \ l /   N",
            "    / \    N",
            "   /   \   N",
            "  _\   /_  N",
            " _________N"]

letras_todas = [] #Todas las letras ingresadadas por el usuario
fallos = 1        #Contador de los fallos del usuario

resultado = [] #Lista con guiones a sustituir con las letras correctas

for i in range(len(palabra)):
    resultado.append("_")

while True:
    os.system("cls")

    print("----- Juego del ahorcado-----")
 

    for i in range(fallos):
        print(ahorcado[i])  
    for i in range(len(horca)-fallos):
        print(horca[i+fallos])
    
    print()

    #Se muestra el resultado que se va obteniendo

    print("    ",end= " ")
    for i in resultado:
        print(i, end=" ")
    
    print()
    print()

    #Se comprueba si ha acertado la palabra o se han terminado los intentos

    if resultado == palabra:
        print("--- Ganaste ---")
        palabra = list(random.choice(palabras))
        break

    if fallos > 6:
        print("--- Perdiste ---")
        print("la palabra era: ","".join(palabra))
        palabra = list(random.choice(palabras))
        
        break

    #Bucle para que el usuario elija las letras

    while True:
        LetraIngresada = input("Dame una letra: ")
        LetraFinal = LetraIngresada.upper()
        if len(LetraFinal) != 1:
            print("introducce una letra")
        elif LetraFinal in letras_todas:
            print("Esa letra ya la has dicho")
        elif LetraFinal not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
            print("introduce una letra")
        else:
            letras_todas.append(LetraFinal)
            break
    # Comprobamos si la letra escrita por el usuario esta en la palabra
    for i in range(len(palabra)):
        if palabra[i] == LetraFinal:
            resultado[i] = LetraFinal
    
    if LetraFinal not in palabra:
        fallos+=1
        
    print()
    print()


            
    
       

