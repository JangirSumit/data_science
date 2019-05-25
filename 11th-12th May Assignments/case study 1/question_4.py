# 4. Write a program to find distance between two locations when their latitude and longitudes are given.
# Hint: Use math module.

import math


def distance(lat1, lon1, lat2, lon2):
    radlat1 = math.pi*lat1/180
    radlon1 = math.pi*lon1/180
    radlat2 = math.pi*lat2/180
    radlon2 = math.pi*lon2/180

    theta = lon1-lon2
    radtheta = math.pi*theta/180

    dist = math.sin(radlat1) * math.sin(radlat2) + \
        math.cos(radlat1)*math.cos(radlat2)*math.cos(radtheta)
    dist = math.acos(dist)
    dist = dist * 180/math.pi
    dist = dist*60*1.1515

    return dist


print("Enter 1st Latitude and longitude")
latlong1 = input(">>> ").split(",")

print("Enter 2nd Latitude and longitude")
latlong2 = input(">>> ").split(",")

lat1 = float(latlong1[0].strip())
lon1 = float(latlong1[1].strip())

lat2 = float(latlong2[0].strip())
lon2 = float(latlong2[1].strip())

dist = distance(lat1, lon1, lat2, lon2)

print(
    f"Distance between ({lat1}, {lon1}) and ({lat1}, {lon2}) is {dist}")
