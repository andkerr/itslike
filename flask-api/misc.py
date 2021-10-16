import googlemaps
from pprint import pprint
from datetime import datetime

now = datetime.now()
gmaps = googlemaps.Client(key=input("Enter API key: "))

start = input("Enter start address: ")
dest = input("Enter destination address: ")

driving_result = gmaps.directions(start, dest, mode='driving', departure_time=now)
if len(driving_result) == 0:
    driving_duration = 'N/A'
    driving_int = float('inf')
else:
    driving_duration = driving_result[0]['legs'][0]['duration']['text']
    driving_int = driving_result[0]['legs'][0]['duration']['value']

transit_result = gmaps.directions(start, dest, mode='transit', departure_time=now)
if len(transit_result) == 0:
    transit_duration = 'N/A'
    transit_int = float('inf')
else:
    transit_duration = transit_result[0]['legs'][0]['duration']['text']
    transit_int = transit_result[0]['legs'][0]['duration']['value']

walking_result = gmaps.directions(start, dest, mode='walking', departure_time=now)
if len(walking_result) == 0:
    walking_duration = 'N/A'
    walking_int = float('inf')
else:
    walking_duration = walking_result[0]['legs'][0]['duration']['text']
    walking_int = walking_result[0]['legs'][0]['duration']['value']


pprint("Driving: " + driving_duration)
pprint("Transit: " + transit_duration)
pprint("Walking: " + walking_duration)

fastest = min(driving_int, transit_int, walking_int)
if fastest == driving_int:
    pprint("Fastest method: Driving")
    fastest = 'driving'
elif fastest == transit_int:
    pprint("Fastest method: Transit")
    fastest = 'transit'
else:
    pprint("Fastest method: Walking")
    fastest = 'transit'

