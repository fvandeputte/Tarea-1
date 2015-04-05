#Extraccion datos

documento=open("foursquare_checkins.csv")

#Total Check-Ins
lista_checkins=documento.readlines()
total_checkins=(len(lista_checkins)-1)


mayor=0
for fila in lista_checkins:
    usuario=fila.split(",")[0]
    if usuario!="user":
        if int(usuario)>mayor:
            mayor=int(usuario)
            
total_usuarios=mayor+1 #Parte del usuario 0

#Total ubicaciones

mayor2=0
for fila in lista_checkins:
    usuario=fila.split(",")[4]
    if usuario!="location\n":
        if usuario!="user":
            if int(usuario)>mayor2:
                mayor2=int(usuario)
            
total_ubicaciones=mayor2+1

#Promedio checkins/usuarios
prom_check_usuario=total_checkins/total_usuarios

#Promedio checkins/ubicaciones
prom_check_ubicacion=total_checkins/total_ubicaciones

#Promedio amigos/usuarios
documento_amistades=open("foursquare_friendship.csv")
lista_lazos=documento_amistades.readlines()
total_lazos=len(lista_lazos)-1
prom_amigos_usuarios=(total_lazos*2)/total_usuarios


print("Total checkins: "+str(total_checkins))
print("Total usuarios: "+str(total_usuarios))
print("Total ubicaciones: "+str(total_ubicaciones))
print("Promedio checkins por usuario :"+str(prom_check_usuario))
print("Promedio checkins por ubicaciones :"+str(prom_check_ubicacion))
print("Promedio amigos por usuarios :"+str(prom_amigos_usuarios))
