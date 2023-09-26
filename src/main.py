import math as m
import datetime
from temposideral import get_local_TS
import convertion
import stars

stars_arr = stars.get_stars_arr()
estrela = stars_arr[42]

ra_deg = convertion.horario_to_decimal(estrela.ra)
dec_deg = convertion.sexagesimal_to_decimal(estrela.dec)

#---------------OBSERVADOR------------------#

#DATA OBSERVACAO
dia_observ = 22
mes_observ = 9
ano_observ = 2023
hora_observ = 20
minuto_observ = 42

#LOCAL OBSERVACAO
fuso_local = -3
phi  = -25.4300
longitude = -49.27

datetime_observ = datetime.datetime(ano_observ, mes_observ, dia_observ, hora_observ, minuto_observ, 0)

TS_Local = get_local_TS(longitude, fuso_local, datetime_observ)
TS_Local = (TS_Local)*15 #verificar

ra  = m.radians(ra_deg)         # deg para rad
dec = m.radians(dec_deg)        # deg para rad
TS  = m.radians(TS_Local)       # deg para rad
phi = m.radians(phi)            # deg para rad

Ah = convertion.radec_to_Ah(ra, dec, TS, phi) #Vetor com as coordenadas horizontais em rad

Ah_sexagesimal = [convertion.decimal_to_sexagesimal(m.degrees(Ah[0])),  #Vetor com coordenadas horizontais
                  convertion.decimal_to_sexagesimal(m.degrees(Ah[1]))]  #no sistema sexagesimal

#print("NAME:",stars_arr[i].name)
#print("DISTANCE:", stars_arr[i].distance)
#print("RA:", stars_arr[i].ra[0], stars_arr[i].ra[1], stars_arr[i].ra[2])
#print("DEC:", stars_arr[i].dec[0], stars_arr[i].dec[1], stars_arr[i].dec[2])

print("Data de observacao: %d/%d/%d" %(dia_observ, mes_observ, ano_observ))
print("Horario de observacao: %d:%d" %(hora_observ, minuto_observ))

print("")
print("Nome:", estrela.name)
print("Distancia:", estrela.distance,"ly")

print("Altura: %.0f° %.0f' %.0f\"" %(Ah_sexagesimal[0][0], Ah_sexagesimal[0][1], Ah_sexagesimal[0][2]))
print("Azimute: %.0f° %.0f' %.0f\"" %(Ah_sexagesimal[1][0], Ah_sexagesimal[1][1], Ah_sexagesimal[1][2]))
print("")