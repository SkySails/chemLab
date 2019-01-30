import Adafruit_DHT


def measure():
    try:
        return Adafruit_DHT.read_retry(11, 4)
    except RuntimeError as e:
        import stringtime
        with open('log', 'a') as logfile:
            logfile.write('{} Reading error occured: {} '.format(stringtime.time(), e))
