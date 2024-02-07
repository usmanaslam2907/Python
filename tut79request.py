# import requests
# r= requests.get("https://www.google.com")
# print(r.text)
# print(r.status_code)
#  get used for get data from url and post work with API

# Video 82 JSON
import json
# json there have no comments and work with qote
data = '{"var":"harry","var2":56}'
print(data)
parsed=json.loads(data)
print(parsed['var'])
print(type(parsed))
# Json.load kia karta ha
# json.

data2={
    "channel":"codewithharry",
    "cars":['bmw','audi8','ferrari'],
    "fridge":('roti',540),
    "isbad":False


}

jscomp=json.dumps(data2)