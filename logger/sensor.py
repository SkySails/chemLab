import Adafruit_DHT


def measure():
    return Adafruit_DHT.read_retry(11, 4)

