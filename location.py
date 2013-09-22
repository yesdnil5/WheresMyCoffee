import urllib2
import json
from bs4 import BeautifulSoup 
from constants import wunder_key

def get_location():
	url = 'http://api.hostip.info/get_json.php?position=true'

	con = urllib2.urlopen(url, None)
	response = json.loads(con.read())
	con.close()
	#print json.dumps(response, sort_keys=True, indent=2)
	lat = response['lat']
	lon = response['lng']
	return lat, lon