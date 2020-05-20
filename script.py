destinations = ['Paris, France','Shanghai, China','Los Angeles, USA','São Paulo, Brazil','Cairo, Egypt']

test_traveler  = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  for i  in list(range(len(destinations))):
    if destinations[i] == destination:
      return i

#print(get_destination_index("Los Angeles, USA"))
#print(get_destination_index("Paris, France"))
#print(get_destination_index("Hyderabad, India"))

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)
attractions = [[item] for item in destinations]
#print(attractions)

def add_attraction(destination,attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
  except ValueError:
    return

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
#print(attractions)
#print("here")

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#print(attractions)
#print(' ')
#print(attractions[2])
#print(get_destination_index('Los Angeles, USA'))
#print(" ")

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_cit = attractions[destination_index]
  attractions_in_city = attractions_in_cit[1:]
  #print(attractions_in_city)
  attractions_with_interest= []
  #possible_attraction=[]

  for item in attractions_in_city:
    possible_attraction = item
    attraction_tags = possible_attraction[1]
    #print(" ")
    #print(attraction_tags)
    for i in interests:
      for j in range(len(attraction_tags)):
        if  attraction_tags[j] == i:
          attractions_with_interest.append(possible_attraction[0])
   
  return attractions_with_interest


la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts)
#print("here2")

#print(attractions)













  









  





