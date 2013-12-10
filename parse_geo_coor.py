# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from geopy.geocoders import GoogleV3
import numpy as np
from time import sleep

s_radds = np.loadtxt('data/suspect.csv', skiprows=1, delimiter=',', 
                 dtype={'names': ('date', 'address'),'formats': ('S10', 'S128')})

geolocator = GoogleV3()

s_radds_list = []
for row in xrange(len(s_radds)):
    print(s_radds[row][1])
    a, (lat, lng) = geolocator.geocode(s_radds[row][1])
    # sleep for 1.5 secs
    sleep(1.5)
    s_radds_list.append([row+1, s_radds[row][0], s_radds[row][1], lng, lat])

# <codecell>

with open("suspect_w_coord.csv", "wb") as f:
    f.write("id,date,address,long,lat\n")
    for row in xrange(len(s_radds_list)):
        r1 = s_radds_list[row][0]
        r2 = s_radds_list[row][1]
        r3 = s_radds_list[row][2]
        r4 = s_radds_list[row][3]
        r5 = s_radds_list[row][4]
        f.write(str(r1)+","+r2+","+r3+","+str(r4)+","+str(r5)+"\n")

# <codecell>


