import time
import sheets
import sensor
import stringtime

''' Authorizes with the google drive api using downloaded credentials from
https://console.cloud.google.com/apis/dashboard and opens the sheet <data>.
The sheet specified needs to be shared with the email address in credentials.json.'''
sheets.auth('credentials.json', 'data')

''' Measures temperature and humidity, then passes the values to 
sheets.write(), which writes them to the sheet <data> along with 
the current time. This happens every 5 minutes, as you can see 
in the time.sleep() call. '''
while True:
    humidity, temperature = sensor.measure()
    sheets.write([stringtime.time(), temperature, humidity])
    time.sleep(5*60)
