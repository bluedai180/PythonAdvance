import requests
from collections import Iterator, Iterable

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def get_weather(self, city):
        r = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=" + city)
        data = r.json()['data']['forecast'][0]
        return "%s: %s, %s" % (city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


if __name__ == "__main__":
    test_cities = ['北京', '沈阳', '成都', '上海']
    iterable = WeatherIterable(test_cities)
    print(iterable)
    for x in iterable:
        print(x)
