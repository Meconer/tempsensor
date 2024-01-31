import time
import board
import adafruit_dht
import requests
import logging
from blynkToken import blynkToken


FORMAT = '%(asctime)s %(message)s'

logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")


# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D18)

def send(pin:str, value:float) : 
    url = "https://fra1.blynk.cloud/external/api/update"
    token = blynkToken
    params = {'pin' : pin, 'value' : value, 'token' : token}
    _ = requests.get(url=url, params=params)

def sendTemp(temp : float) :
    send('V0', temp)

def sendHumidity( humidity : float ) :
    send('V1', humidity)

temperature_c = dhtDevice.temperature
humidity = dhtDevice.humidity
logging.info( "Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity) )
sendTemp(temperature_c)
time.sleep(1.0)
sendHumidity(humidity)


