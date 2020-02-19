place1 = "Bangalore"
place2 = "Chennai"
place3 = "Telangana"

south_India = ("Famous cities in South India are : {0} ,{1} and {2}").format(place1, place2, place3)
print(south_India)

# New way

south_India = (f"Famous cities in South India are : {place1}, {place2} and {place3}")
print(south_India)