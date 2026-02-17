'''
the eq_data.json file is a json file that contains detailed information about
earthquakes around the world for a period of a month. Use this file for this
assignment

NOTE: No hard-coding allowed except for keys for the dictionaries

1) Print out the number of earthquakes

2) Iterate through the eq_dictionary and extract the location, magnitude, 
   longitude and latitude of all earthquakes that have a magnitude > 6.0.
   Put it in a new dictionary. Using the new dictionary, 
   print out the information as shown below (first three shown as example):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''



import json
infile = open('eq_data-1.json','r')

eq_dictionary = json.load(infile)

earthquakes = eq_dictionary["features"]
print(len(earthquakes))

for quake in earthquakes:
    magnitude = quake["properties"]["mag"]
    if magnitude is not None and magnitude > 6.0:
        location = quake["properties"]["place"]
        longitude = quake["geometry"]["coordinates"][0]
        latitude = quake["geometry"]["coordinates"][1]

        print("Location:", location)
        print("Magnitude:", magnitude)
        print("Longitude:", longitude)
        print("Latitude:", latitude)
        print()

