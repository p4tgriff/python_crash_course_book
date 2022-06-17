def city_country(city_name, country_name):
    """Write a function that takes in the name of a city and its country.  Return 3 strings."""
    place = {'city': city_name, 'country': country_name}
    return place


location = city_country('Torronto', 'Canada')
print(location)

location = city_country('Mexico City', 'Mexico')
print(location)

location = city_country('Washington D.C.', 'United States of America')
print(location)
