import sys

import smbus2
import time
from RPLCD.i2c import CharLCD
sys.modules['smbus'] = smbus2

if __name__ == "__main__":
    lcd = CharLCD('PCF8574', address=0x27, port=1, backlight_enabled=True)
    lcd.clear()
    
    while True:
        timeStamp = time.time()
        timeArray = time.localtime(timeStamp)
        lcd.cursor_pos = (0, 0)
        date=time.strftime('%Y-%m-%d',timeArray)
        lcd.write_string(date)
        lcd.cursor_pos = (1, 0)
        hms=time.strftime('        %H:%M:%S',timeArray)
        lcd.write_string(hms)
        time.sleep(1)
        lcd.clear()
