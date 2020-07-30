# module chatbot 
# by Abhay Modi and Nafees Ahmed
from chatterbot import ChatBot #importing chatbot 
from chatterbot.trainers import ListTrainer #method to train chatbot
import os 
import pyttsx3 # this is module to convert text to speech
import google_search # this module is developed for searching on google 
import weather_search #this module is developed for searching about weather
import wiki_search
import load_cities #this modules is used to load cities

# operational function 
# fun_humidity is used for checking humidity in weather 
def fun_humidity(strreq):
	finalstr=request[strreq:]
	humdty = weather_search.humidityWeather(request[strreq:])
	print(humdty)
	speak(humdty)
# fun_temp is used for checking temprature in weather 
def fun_temp(strreq):
	finalstr=request[strreq:]
	temp = weather_search.tempWeather(request[strreq:])
	print(temp+"\n")
	speak(temp)
#fun_weather is used to know whole report of weather 
def fun_weather(strreq):
	finalstr=request[strreq:]
	status = weather_search.statusWeather(request[strreq:])
	print(status)
	speak(status)
#fun fun_complete_weather() is for all over weather
def fun_complete_weather(strreq):
	finalstr=request[strreq:]
	report = weather_search.completeWeather(request[strreq:])
	print(report+"\n")
	speak(report)
#fun wind speed used to check wind speed
def fun_wind_speed(strreq):
	finalstr=request[strreq:]
	wspeed = weather_search.wspeedWeather(request[strreq:])
	print(wspeed)
	speak(wspeed)
#fun_wind_pressure() gives wind pressuer
def fun_wind_pressure(strreq):
	finalstr=request[strreq:]
	press = weather_search.pressureWeather(request[strreq:])
	print(press)
	speak(press)
# defining various function for its featurs:
# this part is text to speech convertor
engine = pyttsx3.init()#engine instance will use the given driver
rate = engine.getProperty('rate')
engine.setProperty('rate', rate) # this function is used to set the rate of speech
def speak(text):
	engine.say(text)
	engine.runAndWait()

# main code starts here
bot = ChatBot('My chatbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path':'chatterbot.logic.MathematicalEvaluation'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, right now i have limited knowledge, will improve.',
            'maximum_similarity_threshold': 0.67
        }
    ])
    
trainer=ListTrainer(bot) # creating chatbot # creating chatbot


speak(" How may i help you ")
while (True):

	print()
	request = input('you: ') # user requesting here with a message

	# action based on response of bot
	if(request=="bye"):
		response = str(bot.get_response(request)) #bot responding to their request
		strrespo= response+", Happy to help you"
		print('Bot:',strrespo) # printing the response of Bot
		speak(strrespo)
		break;
	elif("#wiki" in request):
		speak("sure")
		reqind=request.find("#wiki")
		response= wiki_search.wiki(request[reqind+5:])
		print ("Bot:",response)
		speak(response)
	elif("#google" in request):
		speak("sure")
		speak("here we go")
		reqind=request.find("#google ")
		response=google_search.search(request[reqind+7:])
		print ("check it out please")
		speak("check it out please")
	elif("#humidity" in request):
		reqind=request.find("#humidity ")
		fun_humidity(reqind+10)
	elif("#temp " in request):
		reqind=request.find("#temp ")
		fun_temp(reqind+5)
	elif("#weather " in request):
		reqind=request.find("#weather ")
		fun_complete_weather(reqind+9)
	elif("#weather_status " in request):
		reqind=request.find("#weather_status ")
		fun_weather(reqind+16)
	elif("#wind_speed " in request):
		reqind=request.find("#wind_speed ")
		fun_wind_speed(reqind+12)
	elif("#wind_pressure " in request):
		reqind=request.find("#wind_pressure ")
		fun_wind_pressure(reqind+15)
	else:	
		response = str(bot.get_response(request)) #bot responding to their request
		print('Bot:',response) # printing the response of Bot
		speak(response)
