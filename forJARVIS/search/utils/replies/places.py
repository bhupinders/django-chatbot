import requests

def coordinates(data):
    location = data['entities']['location'][0]['value']
	#https://maps.googleapis.com/maps/api/geocode/json?address=abc&key=key
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    key = 'AIzaSyDDtNsuFPODrssDIYqiu1f4zk_26QpaTIA'
    finalUrl = url+location+'&key='+key
    r = requests.get(finalUrl)
    data = r.json()
	#result.results[0].geometry.location
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']
    address = data['results'][0]['formatted_address']
    print(lat, lng, address)

    ## Places
    #key2 = 'AIzaSyAihSAF7VvPbcQT07s56XUSoViR349LZ_g'
    #url2 = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(lat)+','+str(lng)+'&type=monument&radius=50000&key='+key2
    #r2 = requests.get(url2)
    #data2 = r2.json()
    #for i in data2['results']:
	# 	print(i['name'])
	#print((data2['results'][2]['name']))

	## Trip advisor api
	#keyta = ''
	#url3 ='http://api.tripadvisor.com/api/partner/2.0/map/'+str(lat)+','+str(lng)+'?key='+keyta;
	#r23 = requests.get(url3)
	#data3 = r23.json()
	#print(data3)
    answer = 'Lat : ' + str(lat) + ', Lng : ' + str(lng)
    return answer
