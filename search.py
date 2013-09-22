import oauth2
import urllib
import urllib2
import json
import location

def get_response(lat, lon, token, consumer_key, consumer_secret, token_secret):
	url_params = {'term': 'coffee', 'sort': 1, 'll': lat + "," + lon}
	encoded_params = ''
	if url_params:
		encoded_params = urllib.urlencode(url_params)
	url = 'http://api.yelp.com/v2/search?%s' % (encoded_params)
	print 'URL: %s' % (url,)

	# Sign the URL
	consumer = oauth2.Consumer(consumer_key, consumer_secret)
	oauth_request = oauth2.Request('GET', url, {})
	oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
	                      'oauth_timestamp': oauth2.generate_timestamp(),
	                      'oauth_token': token,
	                      'oauth_consumer_key': consumer_key})

	token = oauth2.Token(token, token_secret)
	oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
	signed_url = oauth_request.to_url()
	print 'Signed URL: %s\n' % (signed_url,)

	response = ""
	# Connect
	try:
	  conn = urllib2.urlopen(signed_url, None)
	  try:
	    response = json.loads(conn.read())
	  finally:
	    conn.close()
	except urllib2.HTTPError, error:
	  response = json.loads(error.read())
	return response

# lat, lon = location.get_location()
# response = get_response(lat, lon, token, consumer_key, consumer_secret, token_secret)
# for x in response['businesses']:
# 	print x['name']
# print response['businesses'][0]['name']