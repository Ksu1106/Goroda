from opencage.geocoder import OpenCageGeocode




def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)

    if results:
        return results[0]['geometry']['lat'],results[0]['geometry']['lng']
    else:
        return 'Город не найден'


key = '5cdb6cccb9db459d8d5f3807bfd239c2'
city = 'Moscow'
coordinates = get_coordinates(city,key)
print(f'Координаты города {city}:{coordinates}')