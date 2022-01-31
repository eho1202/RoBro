import Adafruit_DHT


def temperature():
    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4
    WAIT_TIME = 2

    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    if temperature is not None and humidity is not None:
        if (temperature >= 20.0):
            print("Nice and warm")
        elif (temperature < 20.0):
            print("It's so cold")
        else:
            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(
                temperature, humidity))
    else:
        temperature()


temperature()
