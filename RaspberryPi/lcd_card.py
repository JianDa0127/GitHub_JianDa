import sys
import time
from mfrc522 import SimpleMFRC522
from RPi import GPIO
import smbus2
import time
from RPLCD.i2c import CharLCD
import threading
sys.modules['smbus'] = smbus2

def run_time():
    while True:
        lcd = CharLCD('PCF8574', address=0x27, port=1, backlight_enabled=True)
        lcd.clear()
        timeStamp = time.time()
        timeArray = time.localtime(timeStamp)
        lcd.cursor_pos = (0, 0)
        t=time.strftime("%Y/%m/%d",timeArray)
        lcd.write_string(t) 
        lcd.cursor_pos = (1, 0)
        t=time.strftime("%H:%M:%S",timeArray)
        lcd.write_string(t)
        time.sleep(1)
        lcd.clear()

rt = threading.Thread(target = run_time)
if __name__ == "__main__":
    lcd = CharLCD('PCF8574', address=0x27, port=1, backlight_enabled=True)
    lcd.clear()
    rt.start()
    reader = SimpleMFRC522()
    try:
        while True:
            card_id,card_text = reader.read()
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            t=time.strftime(str(card_id))
            lcd.write_string(t)
            lcd.cursor_pos = (1, 0)
            t=time.strftime('welcome')
            lcd.write_string(t)
            time.sleep(1)
    except KeyboardInterrupt:
        print('bye')
    finally:
        GPIO.cleanup()
    rt.join()
