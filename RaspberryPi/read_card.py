import time
from mfrc522 import SimpleMFRC522
from RPi import GPIO

if __name__=='__main__':
    reader = SimpleMFRC522()
    try:
        while True:
            print('please hold a tag near the reader.')
            card_id,card_text = reader.read()
            if card_id==385149878668:
                print('open door')
            elif card_id==1046624472318:
                print('card')
            else:
                print(' ID: %s'%card_id)
                print('text:%s'%card_text)
            time.sleep(1)
    except keyboardInterrupt:
        print('bye')
    finally:
        GPIO.cleanup()