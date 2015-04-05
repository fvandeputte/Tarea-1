#Seleccionador 500

import random

archivo=open("foursquare_checkins.csv")
lista_check_ins=archivo.readlines()

#Vamos a seleccionar 500 de manera aleatoria entre el total de de checkins:
total=len(lista_check_ins)

#Ademas voy a crear una lista para que no se repitan
lista_numeros=[]
lista_seleccion=[]

for i in range(0,500):
	numero=random.randint(1,total) 		#Se excluye el 0 pues la lista allí no es un checkin
	if not numero in lista_numeros:
		lista_seleccion.append(lista_check_ins[numero])
		lista_numeros.append(numero)

archivo.close()
archivo_output=open("500_checkins.js","w+")
archivo_output.write("lista=")
lista_def=[]
for fila in lista_seleccion:
	lat=float(fila.split(",")[1])
	lon=float(fila.split(",")[2])
	fila_nueva=[lat,lon]
	lista_def.append(fila_nueva)


archivo_output.write(str(lista_def))
       
        
        
        

archivo_output.close()
        

