import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Weather data of Karnataka 
city_name = 'Karnataka'
API_key = '94618497d80f0baad7e6c2a646b9dcf3'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
    print('karataka weather', data ['weather'][0]['description'])
    print('current temperature is', data ['main']['temp'])
    print('current humidity is', data ['main']['humidity'])
    print('current wind speed', data ['wind']['speed'])
labels = ['temperature','humidity','wind speed']
values = [data ['main']['temp'],data ['main']['humidity'],data ['wind']['speed']]
plt.bar(labels,values)
plt.title("weather data of Karnataka")
plt.show()

# Weather data of Jammu
city_name = 'Jammu'
API_key = '94618497d80f0baad7e6c2a646b9dcf3'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
    print('Jmamu weather', data['weather'][0]['description'])
    print('current temperature is', data['main']['temp'])
    print('current humidity is', data['main']['humidity'])
    print('current wind speed is', data['wind']['speed'])
labels = ['temperature','humidity','wind speed']
values = [data ['main']['temp'],data ['main']['humidity'],data ['wind']['speed']]
plt.bar(labels,values)
plt.title("weather data of jammu")
plt.show()

# Weather data of Rajasthan
city_name = 'Rajasthan'
API_key = '94618497d80f0baad7e6c2a646b9dcf3'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
    print('Rajasthan weather', data['weather'][0]['description'])
    print('current temperature is', data['main']['temp'])
    print('current humidity is', data['main']['humidity'])
    print('current wind speed is', data['wind']['speed'])
labels = ['temperature','humidity','wind speed']
values = [data ['main']['temp'],data ['main']['humidity'],data ['wind']['speed']]
plt.bar(labels,values)
plt.title("weather data of Rajasthan")
plt.show()

# Weather data of Kerala
city_name = 'kerala'
API_key = '94618497d80f0baad7e6c2a646b9dcf3'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
    print('kerala weather', data['weather'][0]['description'])
    print('current temperature is', data['main']['temp'])
    print('current humidity is', data['main']['humidity'])
    print('current wind speed is', data['wind']['speed'])
labels = ['temperature','humidity','wind speed']
values = [data ['main']['temp'],data ['main']['humidity'],data ['wind']['speed']]
plt.bar(labels,values)
plt.title("weather data of Kerala")
plt.show()

states = ['Karnataka','Jammu','Rajasthan','Kerala']
temperature = [ 27.74,33.15,37.37,25.82]
humidity = [94,18,24,80]

# Bar graph
plt.bar(states,temperature)
plt.title ("Temperature of different states")
plt.ylabel('temperature')
plt.show()

# Line graph
plt.plot(states, temperature)
plt.title("Temperature Line chart")
plt.ylabel('temperature')
plt.show()

# Satter plot
plt.scatter(states, temperature)
plt.title("Temperature Scatter plot")
plt.ylabel('temperature')
plt.show()

# Pie Chart
plt.pie(temperature, labels=states,autopct= '%1.1f%%')
plt.title("Temperature Pie chart")
plt.show()








    
