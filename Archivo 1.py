#comentario del tablero 
def TableroVacio ():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        ]

def ContenidoColumna (nrocolumna,tablero):
    columna = []
    for row in tablero:
        celda = row[nrocolumna - 1]
        columna.append(celda)
    return columna 
        
         

def soltarFichaEnColumna (ficha, column, tablero):
        for row in range(6, 0, -1):
                if tablero[row - 1][column - 1] == 0:
                        tablero[row -1][column -1] = ficha
                        return 
def CompletarTableroOrden (secuencia, tablero):
    t = 0
    for a in secuencia:
        if t % 2 == 0:
            soltarFichaEnColumna(1, a, tablero)
        else:
            soltarFichaEnColumna(2, a, tablero)
        t+=1
    return tablero

secuencia_texto = input("Ingrese la secuencia de numeros:")
secuencia=[]
for items in secuencia_texto.split (','):
    secuencia.append(int(items))

def DibujarTablero (tablero):
    for row in range(len(tablero)):
        for cell in range(len(tablero[0])):
            if cell == 0:
                print(' | ',end = '')
            if cell == 6:
                print ('|',end = '')
            else:
                print(str(tablero[row][cell]) + ' ', end = '')
        print('')
    print(" + - - - - - - + ")
    #for x in tablero:
        #c=0
        #for a in x:
            #if(c % 7 == 0)or c == 0:
               # print("|")
           # if(a == 0):
               # print('   ', end = '')
            #else:
                #print(' %s ' %a, end = '')
            #c+=1
        #print('')
            

def TiroValido (secuencia):
    for s in secuencia:
        if s<=7&s>0:
            q=1
        else:
            q=0
    return q

tablero = []

if TiroValido (secuencia)==1:
    tablero= (CompletarTableroOrden(secuencia, TableroVacio()))
    DibujarTablero(tablero)
else:
 print ("El rango ingresado no es valido")

#print (ContenidoColumna(5,tablero))


        






                           
