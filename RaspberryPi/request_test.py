import requests
from sense_emu import SenseHat
import time
sense=SenseHat()

temp = requests.get('http://10.21.12.164:8000/temp')
temp = int(round((float(temp.text)+30)/135*8,0))
pres = requests.get('http://10.21.12.164:8000/pres')
pres = int(round((float(pres.text)-260)/125,0))
humi = requests.get('http://10.21.12.164:8000/humi')
humi = int(round(float(humi.text)/12.5,0))
print(str(temp),str(pres),str(humi))

red = (255, 0, 0)
green = (0,255, 0)
blue = (0, 0, 255)
white=(0,0,0)

pixels =[]

for i in range(0,64):
    j=i%8
    k=i/8
    if (j==1 or j==0) and temp+k>=8:
        pixels.append(red)
    elif (j==4 or j==3) and pres+k>=8:
        pixels.append(green)
    elif (j==6 or j==7) and humi+k>=8:
        pixels.append(blue)
    else:
        pixels.append(white)
sense.set_pixels(pixels)
    