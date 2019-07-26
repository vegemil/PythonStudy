import json
import time
import urllib.request

import config

API = config.WEATHER_API
LOCATION_ID = 226081


def get_weather(api, location_id):
    url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/%s?apikey=%s&details=true&language=ko-KR' % (location_id, api)

    print(url)
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    print(data)

    return (data['Headline']['Text'],
            data['DailyForecasts'][0]['Temperature']['Minimum']['Value'],
            data['DailyForecasts'][0]['Temperature']['Maximum']['Value'],
            data['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Value'],
            data['DailyForecasts'][0]['RealFeelTemperature']['Maximum']['Value'],
            data['DailyForecasts'][0]['Day']['LongPhrase'],
            data['DailyForecasts'][0]['Day']['PrecipitationProbability'],
            data['DailyForecasts'][0]['Day']['ThunderstormProbability'],
            data['DailyForecasts'][0]['Day']['RainProbability'],
            data['DailyForecasts'][0]['Day']['SnowProbability'],
            data['DailyForecasts'][0]['Day']['IceProbability'],
            data['DailyForecasts'][0]['Night']['LongPhrase'],
            data['DailyForecasts'][0]['Night']['PrecipitationProbability'],
            data['DailyForecasts'][0]['Night']['ThunderstormProbability'],
            data['DailyForecasts'][0]['Night']['RainProbability'],
            data['DailyForecasts'][0]['Night']['SnowProbability'],
            data['DailyForecasts'][0]['Night']['IceProbability'],



            data)



timestamp = time.time()

headline, highTemperature, lowTemperature, feelHighTemperature, feelLowTemperature, \
    Day_LongPhrase, Day_Precipitation, Day_Thunder, Day_Rain, Day_Snow, Day_Ice, \
    Night_LongPhrase, Night_Precipitation, Night_Thunder, Night_Rain, Night_Snow, Night_Ice, raw \
    = get_weather(API, LOCATION_ID)

print("")
print("----------------- PARSE DATA ------------------")
print(headline)
print(highTemperature)
print(lowTemperature)
print(feelHighTemperature)
print(feelLowTemperature)
print("-------------------------")
print(Day_LongPhrase)
print(Day_Precipitation)
print(Day_Thunder)
print(Day_Rain)
print(Day_Snow)
print(Day_Ice)
print("-------------------------")
print(Night_LongPhrase)
print(Night_Precipitation)
print(Night_Thunder)
print(Night_Rain)
print(Night_Snow)
print(Night_Ice)
