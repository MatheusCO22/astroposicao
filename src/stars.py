import tablereader

class Star:
    def __init__(self, name, identifier, constellation, distance, ra, dec):
        self.name = name
        self.identifier = identifier
        self.constellation = constellation
        self.distance = distance
        self.ra = ra
        self.dec = dec

def parse_radec(ra, dec):
    ra_h, ra_min, ra_s = ra.split(" ")          #h, min, sec
    dec_d, dec_min, dec_s = dec.split(" ")      #degree, min, sec
    
    parsed_ra = [int(ra_h), int(ra_min), float(ra_s)]
    parsed_dec = [int(dec_d), int(dec_min), float(dec_s)]

    return parsed_ra, parsed_dec

def get_stars_arr():
    return stars_arr

#stars dataframe
df = tablereader.get_dataframe()
stars_arr = []

for i in df.index:
    name = df["Name"][i]
    identifier = df["Identifier"][i]
    constellation = df["Constellation"][i]
    distance = df["Distance"][i]
    ra = df["RAJ2000"][i]
    dec = df["DECJ2000"][i]

    parsed_ra, parsed_dec = parse_radec(ra, dec)

    star = Star(name, identifier, constellation, distance, parsed_ra, parsed_dec)
    stars_arr.append(star)

#print("NAME:",stars_arr[i].name)
#print("DISTANCE:", stars_arr[i].distance)
#print("RA:", stars_arr[i].ra[0], stars_arr[i].ra[1], stars_arr[i].ra[2])
#print("DEC:", stars_arr[i].dec[0], stars_arr[i].dec[1], stars_arr[i].dec[2])