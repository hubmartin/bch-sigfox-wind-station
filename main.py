from flask import Flask, request
app = Flask(__name__)

import json
import binascii
import struct
import requests


# Sigfox Belov
#{"snr": 14.99, "time": 1501504818, "rssi": -136.0, "device": "21DF4E", "data": "aabbccddeeff"}

#curl -X POST http://localhost:5000 -d "{\"data\": \"01000200\"}" -H"Content-Type: application/json"

# cd /var/ftp
#forever start -c python your_script.py
#forever stop your_script.py


url = "https://api.thingspeak.com/update"
param = {"api_key": "your_thingspeak_api_key"}

@app.route("/", methods = ['GET', 'POST'])
def main():
	if request.json != None:
		j = request.json
		print(json.dumps(j))
		result = bytearray.fromhex(j['data'])
		speed = struct.unpack("<h", result[0:2])[0] * 0.1
		speedMaximum = struct.unpack("<h", result[2:4])[0] * 0.1
		direction = struct.unpack("<h", result[4:6])[0]
		battery = struct.unpack("<h", result[6:8])[0]
		param["field1"] = speed
		param["field2"] = direction
		param["field3"] = battery
		param["field4"] = speedMaximum
		r = requests.get(url, param)
		print(r) 
		returnString = "Wind: " + str(speed) + " max:" + str(speedMaximum) + ", Direction: " + str(direction) + ", Battery: " + str(battery);
		print(returnString)
		return returnString
	else:
		print("No JSON")
		return "No JSON"
		
def parseData(data):
	data = "aabbccddeeff"


app.run(host="0.0.0.0")