from flask import Flask
from sense_emu import SenseHat
sense=SenseHat()

app=Flask(__name__)
@app.route('/')

def hello_world():
    text=str(round(sense.temperature,1))+','+str(round(sense.pressure,1))+','+str(round(sense.humidity))
    return text

@app.route('/temp')
def temp():
    text=str(round(sense.temperature,1))
    return text
@app.route('/pres')
def pres():
    text=str(round(sense.pressure,1))
    return text

@app.route('/humi')
def humi():
    text=str(round(sense.humidity,1))
    return text

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)