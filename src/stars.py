import tablereader

class Star:
    def __init__(self, name, identifier, constellation, Vmagnitude, Amagnitude, distance, ra, dec):
        self.name = name
        self.identifier = identifier
        self.Vmagnitude = Vmagnitude
        self.Amagnitude = Amagnitude
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
    Vmagnitude = df["VMagnitude"][i]
    Amagnitude = df["AMagnitude"][i]
    distance = df["Distance"][i]
    ra = df["RAJ2000"][i]
    dec = df["DECJ2000"][i]

    parsed_ra, parsed_dec = parse_radec(ra, dec)

    star = Star(name, identifier, constellation, Vmagnitude, Amagnitude, distance, parsed_ra, parsed_dec)
    stars_arr.append(star)