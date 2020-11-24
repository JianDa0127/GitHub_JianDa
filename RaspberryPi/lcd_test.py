import sys

import smbus2
import time
from RPLCD.i2c import CharLCD
sys.modules['smbus'] = smbus2

if __name__ == "__main__":
    lcd = CharLCD('PCF8574', address=0x27, port=1, backlight_enabled=True)
    lcd.clear()
    t='Hello World!    '
    t1=t
    while True:
        lcd.cursor_pos = (0, 0)
        t=t[1:]+t[:1]
        lcd.write_string(t)
        lcd.cursor_pos = (1, 0)
        t1=t1[-1:]+t1[:-1]
        lcd.write_string(t1)
        time.sleep(0.5)
        lcd.clear()