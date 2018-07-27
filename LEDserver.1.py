import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import pigpio

pi = pigpio.pi()

# ==============================================

app = Flask(__name__)

# =================== Global Variables - Getter and Setters =================== 

homepage = "index.html"

global rgb
rgb = [255, 255, 255]

def setRGB(newRGB):
    global rgb
    rgb = [newRGB[0], newRGB[1], newRGB[2]]

def getRed():
    global rgb
    return rgb[0]

def getGreen():
    global rgb
    return rgb[1]

def getBlue():
    global rgb
    return rgb[2]

def setRedLED(newred):
    global rgb
    rgb[0] = newred

def setGreenLED(newGreen):
    global rgb
    rgb[1] = newGreen

def setBlueLED(newBlue):
    global rgb
    rgb[2] = newBlue

# =================== Control Page Rendering =================== 

@app.route("/")
def getHome():
    return render_template(homepage, msg = '', pagecolor = 'off')

@app.route("/red")
def setRedNew():
    setColors((255, 0, 0))
    return make_response(render_template(homepage, msg = 'LED set to Red', pagecolor = 'red'))

@app.route("/green")
def setGreenNew():
    setColors((0, 255, 0))
    return make_response(render_template(homepage, msg = 'LED set to Green', pagecolor = 'green'))
     

@app.route("/blue")
def setBlueNew():
    setColors((0, 0, 255))
    return make_response(render_template(homepage, msg = 'LED set to Blue', pagecolor = 'blue'))

@app.route("/off")
def setOff():
    setColors((0, 0, 0))
    return make_response(render_template(homepage, msg = 'LED turned off', pagecolor = 'off'))

@app.route("/yellow")
def setYellow():
    setColors((255, 128, 0))
    return make_response(render_template(homepage, msg = 'LED set to yellow', pagecolor = 'amber'))

@app.route("/purple")
def setPurple():
    setColors((154, 19, 212))
    return make_response(render_template(homepage, msg = 'LED set to purple'))

@app.route("/orange")
def setOranage():
    setColors((255, 30, 0))
    return make_response(render_template(homepage, msg = 'LED set to orange', pagecolor = 'orange'))

@app.route("/white")
def setWhite():
    setColors((255, 255, 255))
    return make_response(render_template(homepage, msg = 'LED set to white'))

@app.route("/pink")
def setPink():
    setColors((254, 62, 253))
    return make_response(render_template(homepage, msg = 'LED set to pink', pagecolor = 'pink'))

@app.route("/fadeoff")
def setFadeOff():
    global rgb
    light = True
    while (light):
        if (getRed() > 1):
            red = getRed() - 0.3
            setRedLED(red)
        if (getGreen() > 1):
            green = getGreen() - 0.3 
            setGreenLED(green)
        if (getBlue() > 1):
            setBlueLED(getBlue() - 0.3)
        setGlobalColors()
        # if (red > 0 and blue > 0 and green > 0):
        if (getRed() < 1 and getGreen() < 1 and getBlue() < 1):
            light = False
            setRGB((0, 0, 0))
    return make_response(render_template(homepage, msg = 'LED turned off', pagecolor = 'off'))

#pi.stop()

# =================== LED Control =================== 

def setColors(rgb):
    setRGB(rgb)
    pi.set_PWM_dutycycle(17, rgb[0])
    pi.set_PWM_dutycycle(22, rgb[1])
    pi.set_PWM_dutycycle(24, rgb[2])

def setGlobalColors():
    global rgb
    pi.set_PWM_dutycycle(17, rgb[0])
    pi.set_PWM_dutycycle(22, rgb[1])
    pi.set_PWM_dutycycle(24, rgb[2])

# =================== Server startup ===================

if __name__ == "__main__":
    app.debug = True
    #app.run(host = '127.0.0.101',port=5005)
    app.run(host = '192.168.0.54',port=5005)
   