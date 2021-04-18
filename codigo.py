#MODULOS-----------------------------------
from fractions import Fraction #para fracciones
import math #para logaritmos
import itertools #para combinatoria
import sys
import operator #para ordenar
import numpy as np #modulo para maatrices (es necesario instalarlo en el equipo --> cmd pip install numpy)


##FUNCIONES P3---------------------------------

#Leer el texto base de un archivo y generar la Fuente de información con frecuencias absolutas.
def fuente_informacion_freq_absolutas(nombre_archivo):
    
    fuente_informacion = {} #diccionario que sera mi fuente (alfabeto + frecuencias)
    
    
    
    with open(nombre_archivo, 'r', encoding='utf8') as f: #open abre el archivo; r en modo lectura; f el descriptor de fichero; importante decirle que es utf8 el fichero que sino no carga las ñ ni ´´

        linea = f.readline() #leo primera linea del archivo


        while linea: #mientras que siga habiendo líneas
            #Cojo caracter a caracter de la línea
            for caracter in linea:
                #print(caracter)


                    #Miro si es el caracter de fin de línea en cuyo caso lo agregaré como un doble espacio separado, dos espacios simples vaya, no un nuevo símbolo que sea "  "
                if caracter == "\n":    
                        
                    caracter = " " #convierto el \n en un espacio
                    for i in range(0,2): #0 incluido, 2 excluido --> 2 iteraciones
                        if " " in fuente_informacion: #si ya he añadido antes un espacio
                            fuente_informacion[" "] = fuente_informacion[" "] + 1 #si ya estaba el simbolo solo le sumo una ocurrencia 
                        else:
                            fuente_informacion[" "] = 1 #si es la primera ocurrencia, añado al diccionario el espacio (" ") con una ocurrencia
                   
                else: #si no es el de fin de linea es otro pero que tampoco esta en el alfabeto actualmente

                    #miro si el caracter esta ya en el alfabeto
                    if caracter in fuente_informacion:


                        fuente_informacion[caracter] = fuente_informacion[caracter]+1  #si está le sumo uno a su nº de ocurencias
                    
                    else:
                        
                        fuente_informacion[caracter] = 1  #simplemente le pongo una ocurrencia (al ponerle 1 ocurrencia se añaden la clave y el valor, es decir el caracter y el 1)



            #sigo leyendo la siguiente
            linea = f.readline()
        



      

    #TENIENDO YA EL ALFABETO Y LAS FRECUENCIAS ABS EN EL DICCIONARIO DE NOMBRE fuente_informacion {caracter : freq} las devuelvo
    return fuente_informacion

def leerAlfabetoTalCual(nombre_archivo):
    alfabeto = []
    
    
    
    with open(nombre_archivo, 'r', encoding='utf8') as f: #open abre el archivo; r en modo lectura; f el descriptor de fichero; importante decirle que es utf8 el fichero que sino no carga las ñ ni ´´

        linea = f.readline() #leo primera linea del archivo


        while linea: #mientras que siga habiendo líneas
            #Cojo caracter a caracter de la línea
            for caracter in linea:
                alfabeto.append(caracter)
        
            linea = f.readline()

     

    #TENIENDO YA EL ALFABETO lo devuelvo
    return alfabeto

def procesarFuenteInformacion(fuenteInformacion):
    
    alfabeto = []
    
    for i in fuenteInformacion.keys():
        alfabeto.append(i)

    return alfabeto

def leerDatoEntrada(nombre_archivo):
    lista = []
    c = ""
    
    
    with open(nombre_archivo, 'r', encoding='utf8') as f: #open abre el archivo; r en modo lectura; f el descriptor de fichero; importante decirle que es utf8 el fichero que sino no carga las ñ ni ´´

        linea = f.readline() #leo primera linea del archivo


        while linea: #mientras que siga habiendo líneas
            #Cojo caracter a caracter de la línea. 
            for caracter in linea:
                               
                #if caracter == '\n'or caracter == ',' or caracter == ' ': #los \n los ignoramos, como si no estuvieran y las comas y espacios que los separan también
                if caracter == '\n':
                  continue
                
                                 
                if caracter == ',' or caracter == ' ': #Al llegar a una , salvo el caracter (puede haber caracteres dobles o triples dependiendo de si no es binario sino mod 10 pej)
                    lista.append(c)
                    c = "" #reseteamos c
                #si caracter aun no es , seguimos guardando en c porque aún no acabó el numero a leer
                else:
                    c = c + caracter

                

                
        
            linea = f.readline()

     

    return lista

def decodLineal(identidad, secuencias, filas, columnas): #NO PODEMOS DEVOLVER 1 STRING PORQUE PUEDE HABER NUMEROS QUE SEAN DE 2 O MAS SI APPENDEO COMO STRING SE PIERDE QUE ES UN NUM DE 2 POS
    secDecodific = []
    #Si la identidad esta a la izda en la Generadora me quedo con el numero de posiciones que indiquen las filas desde la izda
    if identidad == "I":
        for secuencia in secuencias: #cada pos del vector secuencias (cada trocito de long columnas)
            #print(secuencia)
            for i in range(filas):
                secDecodific.append(secuencia[i]) #i para cada caracter dentro de cada secuencia codificada linealmente desde el 0
    else:    
    #Si no, desde la derecha
          for secuencia in secuencias: #cada pos del vector secuencias
            for i in range(filas, columnas):
                secDecodific.append(secuencia[i]) #i para cada caracter dentro de cada secuencia codificada linealmente desde la segunda mitad

    return secDecodific

def decodFuente(secuencia, alfabeto, base):
    
    caracter = ''

    #  Convertir cada bloque de binario al entero decimal (en éste caso)
    #entero = int(secuencia, base) #convierto la secuencia en string a un numero en la base que hayamos metido, si es 2 binario a decimal, si es 3 ternario a decimal
    #print(entero)
    print ("Sec original long r =", secuencia) #secuencia, es un array de long r, y tengo que transformarlo en un entero decimal (no módulo base)
    
    entero = 0
    exponente = 0
    pos = len(secuencia)-1 #dentro de esas r veces empiezo a coger por el final y voy bajando (derch a izda)

    for num in secuencia: #recorre las posiciones (r veces)
        
        entero = entero + (int(secuencia[pos])*(base**exponente)) 
        exponente = exponente+1
        pos = pos-1
    
   
    # Calculo la posicion en el alfabeto para el entero anterior
    posicion = entero + 1

    # Busco en el alfabeto la posicion teniendo en cuenta que tal como está almacenado el índice es la posición obtenida anterior-1
    print("Símbolo final asociado = ", alfabeto[posicion-1])

    caracter = alfabeto[posicion-1]

    return caracter


def convertirAArrayDeStrings(lista):
    arrayDeStrings = []
    for num in lista:
        arrayDeStrings.append(str(num))
    return arrayDeStrings


##FUNCIONES P4------------------------------------

def esPesoMenorIgualCapCorrectora(secuencia, CapCorrec):
    
    peso = 0
    
    #voy a contar el número de posiciones distintas de 0 en la secuencia actual que se nos pasa (combinacion que se nos pasa)
    for posicion in secuencia:
        #print(posicion)
        if posicion != 0:
            peso = peso + 1

    #ahora voy a comparar si es <= CapCorrec
    if peso <= CapCorrec:
        return True
    else:
        return False

def algoritmoLider(secuencia, sindromes, erroresPatron, base, H):

    #1. Calculo el síndrome de la palabra a corregir
   
    array = []
    for posicion in secuencia:
        array.append(int(posicion)) ##CUIDADO PORQUE LA SECUENCIA ES UN STRING (LO LEI DEL FICHERO COMO TAL); HAY SEPARAR 1 A 1 LAS POSICIONES Y CASTEARLAS A ENTERO
  

    #array = np.array(array) #transforma el array de tamaño 1-> 110100010100110 en [110100010100110]
   
    palabraTraspuesta = np.reshape(array, (len(array), 1)) #traspongo la palabra para poder multiplicar
   
    sindromePalabra = (H.dot(palabraTraspuesta))%base
   
    
    #2. Con ese síndrome voy al tablero incompleto y saco el error patron asociado  (que es hacer una búsqueda en el tablero)
    print(sindromePalabra) 
        #como el sindrome está exactamente en el mismo formato que los del tablero incompleto me facilita muchisimo su busqueda

    
    #pintar todas las claves del diccionario
    print("================= BUSCANDO EN EL TABLERO INCOMPLETO ========================")
    
    indice = 0

    for sindrome in sindromes:
        if ((sindrome == sindromePalabra).all() == True): #all compara termino a termino de los dos arrays que sean iguales
            break
        indice = indice + 1
    
    #encuentra el sindrome correctamente

    errorPatronCorresp = erroresPatron[indice]
    
    print("PALABRA CON RUIDO ",array)
    print("ERROR PATRON ",errorPatronCorresp)
    
       
    #3. Restamos la palabra a corregir del error patron sacado, EN EL MODULO INDICADO A OPERAR (el resultado de dicha resta)
    
    palabraCodigoCorregida = (np.subtract(array, errorPatronCorresp))%base
    print(palabraCodigoCorregida)

    devolver = []

    for i in palabraCodigoCorregida:
        devolver.append(str(i)) #preparo el formato para la entrada de la practica 3

    #print(devolver)
   

    return devolver





##PROGRAMA------------------------
print("Bienvenid@ a la Práctica 4: Simulacion de una codificación binaria lineal CON RUIDO")
print("Introduzca las Filas de la matríz GENERADORA")
filas = input()
print("Introduzca las Columnas de la matríz GENERADORA")
columnas = input()
print("La Generadora es de Orden "+filas+"x"+columnas)

filas = int(filas) #Lo parseo a entero
columnas = int(columnas) #Lo parseo a entero

print("¿En qué parte de la generadora está la Identidad?[D/I]") #Me es útil para la parte de la P3 para la decodificación lineal
identidad = input()

if identidad != 'D' and identidad != 'I':
    print("Error de entrada")
    exit()




    #1. Cargar Alfabeto 

#ENTRADA TAL CUAL DEL ARCHIVO
#alfabeto = leerAlfabetoTalCual('/Users/mario/Desktop/Segundo Cuatrimestre/Seguridad Informática/Prácticas/Practica_3_SI/Resolución/Alfabeto.txt')
#print("Tal cual del archivo", alfabeto)

fuenteInformacion = fuente_informacion_freq_absolutas('/Users/mario/Desktop/Segundo Cuatrimestre/Seguridad Informática/Prácticas/Practica_4_SI/Resolución/Alfabeto.txt')
print("Tam Alf = ", sum(fuenteInformacion.values()))
alfabeto = procesarFuenteInformacion(fuenteInformacion) #de la fuente de informacion nos quedamos solo con el alfabeto en una lista

print("Alfabeto = ", alfabeto)
print("Tamaño = ", len(alfabeto))
m = len(alfabeto) #Numero de símbolos del alfabeto
m = int(m)

#ENTRADA MANUAL
#alfabeto = []
#alfabeto = ['P','R','A','C','T','I','C','A','T','R','E','S']
#print(alfabeto)


    # Leer dato entrada (lista L) OJO, NECESARIA COMA FINAL PARA QUE GUARDE EL ÚLTIMO

#lista = leerDatoEntrada('/Users/mario/Desktop/Segundo Cuatrimestre/Seguridad Informática/Prácticas/Practica_3_SI/Resolución/Dato.txt')
#print("Lista Entrada", lista)



    #ENTRADA DATO MANUAL (MAS CÓMODO):
lista = [5,1,1,5,2,6,4,0,0,1,3,5,4,1,5,5,6,0,6,5,3,0,3,6,6,2,4,3,6,2,0,6,3,0,3,6,1,4,0,1,3,5,6,1,5,2,4,6,5,4,3,0,3,6,4,6,0,3,2,1,1,3,0,3,2,1,1,5,3,4,1,5,3,5,5,2,4,6,6,3,5,5,6,0,1,0,3,0,3,6,0,3,0,1,3,5,1,4,1,5,2,6]
lista = convertirAArrayDeStrings(lista)
print("Dato Entrada = ")
print(lista)




    # Calculo el tamaño de la lista (longitud del mjs codificado) y lo divido por el número de columnas de la generadora
tam = len(lista)
print("Tam Dato Entrada = ", tam)

cociente = tam // columnas
resto = tam % columnas

print("Cociente = ", cociente)
print("Resto = ", resto)


    # De la lista leída tendremos: "cociente" secuencias de "columnas" elementos y una cola de "resto" elementos

secuencia = []
secuencias = []
contador = 0

for i in range(cociente*columnas):
    secuencia.append(lista[i]) #añado el elemento subi de la lista de entrada
    #print(secuencia)
    contador = contador + 1
    
    if contador == columnas:
        #he completado una secuencia, la salvo en el vector de secuencias separadas
        secuencias.append(secuencia)
        #print("vuelco")
        secuencia = []
        contador = 0


cola = [] #array para que no se pierda si es qario y el numero es mas de una cifra

for i in range((cociente*columnas), tam): #cociente*columnas fue excluido en el bucle previo porque llegaba justo hasta el valor anterior a ese y ahora parto desde ese inclusive y hasta el final para coger todo lo que quede
    cola.append(lista[i])


print("SECUENCIAS DE COLUMNA ELEMENTOS = ")
print(secuencias)
print("COLA")
print(cola)

###################################### PRÁCTICA 4 ############################################################################################################################################################


    # Cálculo del TABLERO INCOMPLETO

#Distancia de Hamming
print("Distancia de Hamming:")
d = input()
d = int(d) #Lo parseo a entero

#Pido si es código binario, ternario F3 F5
print("¿Qué tipo de código es [Binario --> 2]?")
base = input()
base = int(base)

#Capacidad Correctora del codigo
t = math.floor(Fraction((d-1), 2))
print("Cap Correctora es t= ", t)

#Implementación por Fuerza Bruta

ordenaciones = list(itertools.product(range(base), repeat=columnas)) #Formas de ordenar base elementos en columnas posiciones

#print(ordenaciones)

erroresPatron = []

for ordenacion in ordenaciones: #recorro c/u de las ordenaciones obtenidas por fuerza bruta
    testigo = esPesoMenorIgualCapCorrectora(ordenacion, t) #le paso cada ordenacion a la función para que me diga si el peso es menor o igual que la capacidad correctora calculada
    if testigo == True: #si es <=t sé fijo que la combinación es un error patron
        erroresPatron.append(ordenacion) #y lo guardo

#print("ERRORES PATRON", erroresPatron)


    #Cálculo de la Matriz De Control H = (-A^T|Id de orden filas de A)

### INPUT DE MATRIZ A (LA QUE SE NOS PROPORCIONA)
A = np.array([[2,3,4,5],
[6,1,2,3]])

print("FILAS DE A =",A.shape[0])
print("COLUMNAS DE A =",A.shape[1])


print("MATRIZ ENTRADA = ", A)

#NA = np.negative(A)
NA = ((-1)*A)%base #La clave para operar en un módulo determinado con matrices!! :)
print("Matriz NEGADA -A", NA)

#La transpongo:
NATraspuesta = NA.transpose()
print("Matriz TRANSPUESTA -AT", NATraspuesta)

#Calculo la identidad
Id = np.identity(A.shape[1]) # Matriz identidad de tamaño filas de la traspuesta de A (que NO son las columnas que doy al ppio, esas son las totales de la generadora), sino las columnas de A solamente
print("MATRIZ IDENTIDAD PARA COMPLETAR H; Id", Id)

#Junto las 2 en 1
H = np.concatenate((NATraspuesta, Id), axis=1)
print("MATRIZ DE CONTROL H= ",H)


#Para cada uno de los errores patron que me valen por tener el peso oportuno, calculo su síndrome y meto las dos cosas juntas, en la misma posicion pero en dos listas

sindromes = []


for errorPatron in erroresPatron: #Recorro las entradas todas
    errorPatron = np.reshape(errorPatron, (len(errorPatron), 1)) #Le cambio las dimensiones para que sea 15*1 y podamos multiplicar por H; porque errorPatron que teniamos guardados eran 1*15
    sindromes.append((H.dot(errorPatron))%base) #añado a la tabla de sindromes el correspondiente (al error patron en esa posicion) síndrome calculado  9*1 NO OLVIDAR QUE EL PRODUCTO ES EN EL MODULO INDICADO/CUERPO FINITO

print(sindromes)


#Construido el tablero incompleto


    # APLICO EL ALGORITMO DEL LÍDER para eliminar el ruido a cada una de las secuencias, corregir cada una de las secuencias

secuenciaSCorregidas = []

for secuencia in secuencias: #"secuencias" son la lista dato con ruido dividida ya por bloques
    secSinRuido = algoritmoLider(secuencia, sindromes, erroresPatron, base, H)
    #me vuelve del algoritmo corregida y en string
    secuenciaSCorregidas.append(secSinRuido) #la añado al conjunto de las corregidas
       

    #AHORA TENEMOS LA LISTA DE ENTRADA PERO YA SIN RUIDO, Y SE LA PASAMOS A LA PARTE DE LA PRACTICA 3 COMO DATO

print(secuenciaSCorregidas) #No contiene la cola
print(cola)




###################################### PRÁCTICA 3 ############################################################################################################################################################

    # Decodificación Lineal

cod_fuente_lista = decodLineal(identidad, secuenciaSCorregidas, filas, columnas) #tengo la secuencia decodificada linealmente sin la cola

#Añadimos la cola
for num in cola:
    cod_fuente_lista.append(num) #tendriamos el msj decodif linealmente pero manteniendo los dobles, triples... numeros porque cada uno tiene su posicion en la lista (actualemnte es un msj metido en array)

print("MSJ DEC LINEALMENTE = ", cod_fuente_lista)


    # Calcular la longitud mínima en bloque (para codificar en binario en éste caso)


# Calcular el logaritmo en base, la indicada, del nº símbolos del alfabeto
long_min = math.log(m,base)
print(long_min)

# Separo parte entera del resultado y parte decimal
long_min = math.ceil(long_min)
#parte_decimal, parte_entera = math.modf(long_min)
#print(parte_entera) #Como tiene que ser el entero superior siempre va a ser 1 mas que el que salga
#print(parte_decimal)

#long_min = int(parte_entera+1) #hago un cast a entero porque sino quedaba float
print("Longitud mínima (Entero Superior) = ", long_min)



    # Troceo el mensaje dec linealmente en bloques/secuencias de esa long mínima (debo usar un array de arrays para no perder los simbolos dobles, triples... quarios vaya)

secsCodFuente = []
secuenciaLongMin = []
contador = 0

for i in cod_fuente_lista: #caracter a caracter del mensaje + cola (string) vamos cogiendo hasta completar r términos
    secuenciaLongMin.append(i) #añado cada caracter
    contador = contador + 1
    
    if contador == long_min:
        #he completado una secuencia, la salvo en el vector de secuencias separadas
        secsCodFuente.append(secuenciaLongMin)
        #print("vuelco")
        secuenciaLongMin = []
        contador = 0


print(secsCodFuente)

    # CICLO - Repetir tantas veces como secuencias de long mínima haya en nuestra secsCodFuente. Es decir, como marque la longitud
mensaje = ""

print()
print("PROCESO DE DECODIFICACION DE LA FUENTE:")

for secuencia in secsCodFuente: #recorro cada secuencia de long mínima del array
    mensaje = mensaje + decodFuente(secuencia, alfabeto, base)

#es posible que vengan 2 espacios juntos y eso equivale para nosostros al salto de linea \n
mensaje = mensaje.replace("  ", "\n")


print("\n======================================================================")
print("MENSAJE DECODIFICADO:")
print(mensaje)
print("======================================================================")

print("\nFIN DEL PROGRAMA")
       







##APENDICES:

    #pintar todos los valores del diccionario
#for i in fuente_freq_abs.values():
#        print(i)

    #pintar todas las claves del diccionario
#for i in fuente_freq_abs.keys():
#        print(i)

    #manejar clave y valor a la vez en un diccionario para ir por las posiciones
#for clave, valor in fuente_de_informacion.items():  
#        fuente_de_informacion[clave] = Fraction(valor, total_frecuencias)


    #fraccion es numerador/denominador
#fraccion = Fraction(1, 2) #--> 1/2
#print(fraccion)


    #logaritmo en base 2 de 100
#math.log(100,2)



#utf8stdout = open(1, 'w', encoding='utf-8', closefd=False) # fd 1 is stdout
#cadena = "ó"
#print(cadena)
#for i in fuente_freq_abs.keys():
    #print(i, file=utf8stdout)

#print("Entero Inferior", math.floor(2.3))
#print("Entero Inferior", math.floor(2))
#print("Entero Superior", math.ceil(2.3))
#print("Entero Superior", math.ceil(2))

#itertools.combinations(range(4), 3) #--> 012 013 023 123


#CHECK DE QUE NUMPY ESTA INSTALADO
#a = np.array([1, 2, 3])
#print(a)               # Output: [1, 2, 3]
#print(type(a))         # Output: <class 'numpy.ndarray'>

#NA2 = ((-1)*A)%2 #La clave para operar en un módulo determinado con matrices!! :)

#Convierto un array de elementos separados por comas en un string
#str(array)

#convierto una tupla (el1, el2, el3) en un array [[el1], [elem2], [elem3]]
#tupla = np.asarray(tupla)


#CONVERTIR STRING EN ARRAY
#str = "Millie Bobby Brown is Enola Holmes"
#arr = str.split()
#print(arr)

#si elems separados por coma
#>>> text = 'a,b,c'
#>>> text = text.split(',')
#>>> text
#[ 'a', 'b', 'c' ]