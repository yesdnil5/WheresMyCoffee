from flask import Flask, render_template, request
import search
from coffee_place import CoffeePlace 
from constants import consumer_key, consumer_secret, token, token_secret
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/coffee', methods=["POST"])
def get_coffee_list():
	lat = request.form['lat']
	lon = request.form['lon']
	print lat
	print lon
	response = search.get_response(lat, lon, token, consumer_key, 
									consumer_secret, token_secret)
	coffee_keys = []
	coffee_dict = {}
	for x in response['businesses']:
		coffee_keys.append(x['name'])
		coffee_dict[x['name']] = CoffeePlace(x['name'], x['location']['address'][0],
								x['location']['city'], x['location']['state_code'], lat, lon)

	return render_template('coffee.html', coffee_keys=coffee_keys, 
											coffee_places=coffee_dict)

if __name__ == '__main__':
	app.run(debug=True)