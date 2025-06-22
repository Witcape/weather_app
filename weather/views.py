from django.shortcuts import render
import json
import urllib.request
from urllib.parse import quote

def index(request):
    if request.method == "POST":
        city = request.POST["city"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3f06057bd34c5525c370f120e2db619d"
        res = urllib.request.urlopen(url).read()
        json_data = json.loads(res)
        print(json_data)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city = request.POST["city"]
        data = {}
    return render(request, 'index.html', data)