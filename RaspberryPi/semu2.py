from sense_emu import SenseHat
sense=SenseHat()
white=(255,0,255)
pixels=[]
for i in range(64):
    pixels.append(white)
sense.set_pixels(pixels)