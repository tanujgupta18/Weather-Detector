from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        json_data = json.loads(res)
        temperature_kelvin = json_data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(round(temperature_celsius, 2)) + '°C',
            "pressure": str(json_data['main']['pressure'])+' mb',
            "humidity": str(json_data['main']['humidity'])+'%',
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
