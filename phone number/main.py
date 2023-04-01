import phonenumbers
import opencage
import folium
from test import number

from phonenumbers import geocoder
co_number=phonenumbers.parse(number, "CO")
print(geocoder.description_for_number(co_number, "en"))
location=geocoder.description_for_number(co_number, "en")
print(location)

from phonenumbers import carrier
service_number=phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))

from opencage.geocoder import OpenCageGeocode

key='7e1499f17126421da577bb00a67d519d'

geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)

myMap=folium.Map(location=[lat,lng], zoom_status=9)
folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("myloaction.html")

