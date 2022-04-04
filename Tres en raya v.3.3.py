#Tres en raya

# variables

# las variables de a-f definen el campo de juego
a = "|"*20
b = a + "|||"+" "*5+" "*2+" "*5+"||"+" "*5+" "*2+" "*5+"||"+" "*5+" "*2+" "*5+"|||"+a
c = "|||"+" "*5
d = " "*5+"|||"
e = "-"*35
f = a + "|||"+e

# la lista ca son las casillas a llenar 
ca = [" "," "," "," "," "," "," "," "," "]

o10= ["O","X"]      # estas son las opciones para rellenar las casillas
i=1

#Bienvenida

print(a+"*"*3+"-"*15+"BIENVENIDO"+"-"*15+"*"*3+a) 

#dibujar el campo

print("="*86)
print(a*4+"||||||"); print(a*4+"||||||")
print(b)
print(b)
print(a+c+ca[0]*2+" "*5+"|"*2+" "*5+ca[1]*2+" "*5+"||"+5*" "+ca[2]*2+d+a)
print(b)
print(b)
print(a +"|||"+ "="*40+"|||"+a)
print(b)
print(b)
print(a+c+ca[3]*2+" "*5+"|"*2+" "*5+ca[4]*2+" "*5+"||"+5*" "+ca[5]*2+d+a)
print(b)
print(b)
print(a +"|||"+ "="*40+"|||"+a)
print(b)
print(b)
print(a+c+ca[6]*2+" "*5+"|"*2+" "*5+ca[7]*2+" "*5+"||"+5*" "+ca[8]*2+d+a)
print(b)
print(b)
print(a+a+a+a+"||||||")
print(a+a+a+a+"||||||")

#seleccion de casilla 
while i <10:
    
    # condiciones
    seleccionDeCasilla = int(input(f+"Dame un número del 1 al 9: "))-1      # aqui el programa te pide un numero y se convierte en una variable
    
    # El programa compara el numero elegido con las 9 casillas, y reemplaza la escogida con una X o O.
    if seleccionDeCasilla == 0:
        if ca[0] == " ":
            ca[0] = o10[i%2]
            i=i+1
        else:
            print("="*86); print("!!!!!!!!!!!!!!!!!!!!!!---------La casilla está ocupada---------!!!!!!!!!!!!!!!!!!!!!!"); print("="*86)           
    elif seleccionDeCasilla == 1:
        if ca[1] == " ":
            ca[1] = o10[i%2]
            i=i+1
        else:
            print("="*86); print("!!!!!!!!!!!!!!!!!!!!!!---------La casilla está ocupada---------!!!!!!!!!!!!!!!!!!!!!!"); print("="*86)           
    elif seleccionDeCasilla == 2:
        if ca[2] == " ":
            ca[2] = o10[i%2]
            i=i+1
        else:
            print("="*86); print("!!!!!!!!!!!!!!!!!!!!!!---------La casilla está ocupada---------!!!!!!!!!!!!!!!!!!!!!!"); print("="*86) 
    elif seleccionDeCasilla == 3:
        if ca[3] == " ":
            ca[3] = o10[i%2]
            i=i+1
        else:
            print("="*86); print("!!!!!!!!!!!!!!!!!!!!!!---------La casilla está ocupada---------!!!!!!!!!!!!!!!!!!!!!!"); print("="*86)  
    elif seleccionDeCasilla == 4:
        if ca[4] == " ":
            ca[4] = o10[i%2]
            i=i+1
        else:
            print("="*86); print("!!!!!!!!!!!!!!!!!!!!!!---------La casilla está ocupada---------!!!!!!!!!!!!!!!!!!!!!!"); print("="*86) 
    elif seleccionDeCasilla == 5:
        if ca[5] == " ":
            ca[5] = o10[i%2]
            i=i+1
        else:
            print("="*86); print("!!!!!!!!!!!!!!!!!!!!!!---------La casilla está ocupada---------!!!!!!!!!!!!!!!!!!!!!!"); print("="*86)      
    elif seleccionDeCasilla == 6:
        if ca[6] == " ":
            ca[6] = o10[i%2]
            i=i+1
        else:
            print("="*86); print("!!!!!!!!!!!!!!!!!!!!!!---------La casilla está ocupada---------!!!!!!!!!!!!!!!!!!!!!!"); print("="*86)     
    elif seleccionDeCasilla == 7:
        if ca[7] == " ":
            ca[7] = o10[i%2]
            i=i+1
        else:
            print("="*86); print("!!!!!!!!!!!!!!!!!!!!!!---------La casilla está ocupada---------!!!!!!!!!!!!!!!!!!!!!!"); print("="*86)    
    elif seleccionDeCasilla == 8:
        if ca[8] == " ":
            ca[8] = o10[i%2]
            i=i+1
        else:
            print("="*86); print("!!!!!!!!!!!!!!!!!!!!!!---------La casilla está ocupada---------!!!!!!!!!!!!!!!!!!!!!!"); print("="*86)          
    else:
        print("!!!!!!!!!!!!!!!!!!!!!---------Coloca un numero del 1 - 9---------!!!!!!!!!!!!!!!!!!!!!")

    #dibujar el campo
    print("="*86)
    print(a+a+a+a+"||||||")
    print(a+a+a+a+"||||||")
    print(b)
    print(b)
    print(a+c+ca[0]*2+" "*5+"|"*2+" "*5+ca[1]*2+" "*5+"||"+5*" "+ca[2]*2+d+a)
    print(b)
    print(b)
    print(a +"|||"+ "="*40+"|||"+a)
    print(b)
    print(b)
    print(a+c+ca[3]*2+" "*5+"|"*2+" "*5+ca[4]*2+" "*5+"||"+5*" "+ca[5]*2+d+a)
    print(b)
    print(b)
    print(a +"|||"+ "="*40+"|||"+a)
    print(b)
    print(b)
    print(a+c+ca[6]*2+" "*5+"|"*2+" "*5+ca[7]*2+" "*5+"||"+5*" "+ca[8]*2+d+a)
    print(b)
    print(b)
    print(a+a+a+a+"||||||")
    print(a+a+a+a+"||||||")  

    # Aqui el programa compara las 8 combinaciones posibles de un ganador, para ver si algun jugador ganó el juego
    if ca[0] == ca[1] == ca[2] and ca[0]!=" ":

        print(f+"Gano",ca[0])
        break
    elif ca[3] == ca[4] == ca[5] and ca[4]!=" ":

        print(f+"Gano",ca[3])
        break
    elif ca[6] == ca[7] == ca[8] and ca[8]!=" ":

        print(f+"Gano",ca[6])
        break
    elif ca[0] == ca[3] == ca[6] and ca[0]!=" ":

        print(f+"Gano",ca[0])
        break
    elif ca[1] == ca[4] == ca[7] and ca[1]!=" ":

        print(f+"Gano",ca[1])
        break
    elif ca[2] == ca[5] == ca[8] and ca[2]!=" ":

        print(f+"Gano",ca[2])
        break
    elif ca[0] == ca[4] == ca[8] and ca[0]!=" ":

        print(f+"Gano",ca[0])
        break
    elif ca[2] == ca[4] == ca[6] and ca[2]!=" ":

        print(f+"Gano",ca[2])
        break

# una vez el bucle termina, el juego tambien lo hace.
    
print("="*86)
print(a+"|"*14,"TERMINO EL JUEGO","|"*14+a)

