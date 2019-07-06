import re,urllib.request

#https://www.weather-forecast.com/locations/Patna/forecasts/latest

city = input("Enter your city: ")
url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
m = re.search('<span class="temp">',data1)
start=m.end()
end=start+4
final = data1[start:end]
print("Current Temperature of "+ city.upper()+ " is "+final+" degree celcius.")
