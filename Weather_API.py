import requests

import os 

from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

key=os.getenv('key')


city=input('enter the city:').strip()

url='https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+key
print(url)

res=requests.get(url).json()

# print(res)

print('city:',res['name'])

print('country:',res['sys']['country'])

print('temp:',res['main']['temp'])

print('coords:',res['coord'])

print('longitude',res['coord']['lon'])

print('latitude',res['coord']['lat'])

print('description',res['weather'][0]['description'])




