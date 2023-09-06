import rotation as rot
import math as m
import numpy as np

def radec_to_Ah (ra, dec, TS, phi):
    H = TS - ra
    #Vetor coordenadas equatoriais
    EQ = [[m.cos(dec)*m.cos(H)],    #x
          [m.cos(dec)*m.sin(H)],    #y
          [m.sin(dec)]]             #z

    # rotacionar sistema equatorial em 90 - phi no eixo y
    AH = np.dot(rot.Ry(m.radians(90) - phi), EQ)
    
    # rotacionar em 180 no eixo z
    AH = np.dot(rot.Rz(m.radians(180)), AH)

    z = m.acos(AH[2,0]) #temp

    A_temp = m.acos((1/m.sin(z))*(AH[0,0]))

    if ((1/m.sin(z))*(AH[1,0]) > 0):
        A = A_temp
    else:
        A = 2*(m.pi) - A_temp

    h = m.pi / 2 - z
    return h, A

def decimal_to_sexagesimal(theta):
    S = np.sign(theta)
    theta = abs(theta)
    graus = theta // 1
    minutos = ((theta%1)*60) // 1
    segundos = (((theta%1)*60) % 1) * 60

    sexagesimal = [S*graus, S*minutos, S*segundos]
    return sexagesimal

def sexagesimal_to_decimal(vetor_angulo):
    graus, minutos, segundos = vetor_angulo

    S = np.sign(graus)
    graus = abs(graus)
    minutos = abs(minutos)
    segundos = abs(segundos)

    minutos = minutos + (segundos / 60)
    theta = graus + minutos/60

    return S*theta

def horario_to_decimal(vetor_angulo):
    horas, minutos, segundos = vetor_angulo
    minutos += segundos / 60
    horas += minutos / 60

    theta = horas*15
    return theta
