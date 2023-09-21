#Alpha Tauri
#RA:  04h 35m 55.2s
#dec: +16°30'33.5"

#Antares
#RA: 16h 29min 24.98s
#DEC: -60°49' 1.2s

#Vega
#RA: 18h 37m45.3s
# DEC: +38°48'28.3"

#Antares
#RA: 16h 29min 24.98s
#DEC: -26d -25min -28.4s

class Star:
    def __init__(self, ra, dec, name):
        self.ra = ra
        self.dec = dec
        self.name = name

              #deg  min  seg
antares = Star([16, 29, 24.98], [-26, -25, -58.4], "Antares")
rigil_k = Star([14, 39, 28.42], [-60, -49, -1.2], "Rigil Kentaurus")
vega = Star([18, 37, 45.3], [38, 48, 28.3], "Vega")

arr_stars = [antares, rigil_k, vega]

def get_arr_stars():
    return arr_stars