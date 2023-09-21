import datetime
from datetime import date
from datetime import timedelta

def get_dias_equinocio(ano, mes, dia, hora, minuto, segundo, fuso):
    # Local Time
    # colocar o horario local no formato datetime
    LT = datetime.datetime(ano, mes, dia, hora, minuto, segundo)
    
    # Universal Time
    # subtrair o fuso para obter UT
    UT = LT - timedelta(hours = fuso)

    # colocar 21/ mar no formato datetime
    Equinocio = datetime.datetime(ano, 3, 21, 12, 0, 0)

    # intervalo de tempo entre as duas datas
    dias_desde_21mar = (UT - Equinocio).total_seconds() / 86400

    return dias_desde_21mar

def get_Green_TS(fuso, datetime_observacao):
    dia = datetime_observacao.day
    mes = datetime_observacao.month
    ano = datetime_observacao.year

    hora = datetime_observacao.hour
    minuto = datetime_observacao.minute
    segundo = datetime_observacao.second

    hora_decimal = hora + (minuto +(segundo)/60)/60

    n_dias = get_dias_equinocio(ano, mes, dia, hora, minuto, segundo, fuso)
    
    TS_Green = ((hora_decimal - fuso) - 12) + (24/365)*n_dias

    if(TS_Green < 0):
        TS_Green += 24

    # print("TS em Greenwich: %.0fh %.0fmin " %((TS_Green) // 1, (TS_Green % 1)*60))

    return TS_Green

def get_local_TS(longitude, fuso, datetime_observacao):
    TS_Green = get_Green_TS(fuso, datetime_observacao) 

    TS_Local = TS_Green + (longitude*1/15)

    if(TS_Local < 0):
        TS_Local += 24
    elif (TS_Local > 24):
        TS_Local = TS_Local % 24

    # print("TS Local: %.0fh %.0fmin " %((TS_Local) // 1, (TS_Local % 1)*60))

    return TS_Local