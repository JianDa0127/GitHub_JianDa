from sense_emu import SenseHat
sense=SenseHat()

text = str(round(sense.pressure,1))
sense.show_message(text)