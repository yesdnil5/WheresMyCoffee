import json
import urllib2

class CoffeePlace():
	def __init__(self, name, address, city, state, lat, lon):
		self.name = name
		self.address = address
		self.city = city
		self.state = state
		self.distance, self.duration = self.get_distance(lat, lon)

	def get_distance(self, lat, lon):
		temp_address = self.address.replace(" ", "+")
		temp_city = self.city.replace(" ", "+")
		url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=%s,%s&destinations=%s+%s+%s&mode=walking&sensor=true&units=imperial" \
			% (lat, lon, temp_address, temp_city, self.state)
		print url
		con = urllib2.urlopen(url, None)
		response = json.loads(con.read())
		con.close()
		return (response['rows'][0]['elements'][0]['distance']['text'], 
				response['rows'][0]['elements'][0]['duration']['text'])