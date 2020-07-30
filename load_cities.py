#Writer:ABHAY MODI
# this module returns various cities values 
import json 
import os 
returndata=[] 
def load_cities():
	for _file in os.listdir('./data_countries/'):
		filename=str(_file)
		with open('./data_countries/'+_file,'r') as fileobj:
			data = json.load(fileobj)
			for i in data:
				if(filename=="countries-and-cities.json"):
					returndata.append(i['name'])
				elif(filename=="worldcities.json"):
					returndata.append(i['city'])
	return returndata