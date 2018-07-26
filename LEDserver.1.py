import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import pigpio


pi = pigpio.pi()

# ==============================================

app = Flask(__name__)

# =================== Led Control ============== 

homepage = "home.html"
global red 
global green 
global blue
global rgb

setRGB = ((255, 255, 255))

red = 0
green = 0
blue = 0

def setRGB():
    global rgb
    rgb

def getRed():
    global rgb
    return rgb[0]

def getGreen():
    global rgb
    return rgb[1]

def getBlue():
    global rgb
    return rgb[2]

def setRed(newred):
    global rgb
    rgb[0] = newred

def setGreen(newGreen):
    global rgb
    rgb[1] = newGreen

def setBlue(newBlue):
    global rgb
    rgb[2] = newBlue

@app.route("/rednew")
def setRedNew():
    red = (255, 0, 0)
    setColors(red)
    return make_response(render_template("index.html", msg = 'LED set to Red'))


@app.route("/greennew")
def setGreenNew():
    setRedLED(0)
    setGreenLED(255)
    setBlueLED(0)
    setColor()
    resp = make_response(render_template("index.html", msg = 'LED set to Green'))
    return resp

@app.route("/bluenew")
def setBlueNew():
    setRedLED(0)
    setGreenLED(0)
    setBlueLED(255)
    setColor()
    resp = make_response(render_template("index.html", msg = 'LED set to Blue'))
    return resp

@app.route("/")
def getHome():
    return render_template(homepage, msg = '')

@app.route("/red")
def setRed():
    rgbRed = (255, 0, 0)
    setColors(rgbRed)
    return make_response(render_template(homepage, msg = 'LED set to Red'))


@app.route("/green")
def setGreen():
    rgbGreen = (0, 255, 0)
    setColors(rgbGreen)
    resp = make_response(render_template(homepage, msg = 'LED set to Green'))
    return resp

@app.route("/blue")
def setBlue():
    rgbBlue = (0, 0, 255)
    setColors(rgbBlue)
    resp = make_response(render_template(homepage, msg = 'LED set to Blue'))
    return resp

@app.route("/off")
def setOff():
    rgbBlue = (0, 0, 0)
    setColors(rgbBlue)
    resp = make_response(render_template(homepage, msg = 'LED turned off'))
    return resp


@app.route("/yellow")
def setYellow():
    rgbBlue = (255, 128, 0)
    setColors(rgbBlue)
    resp = make_response(render_template(homepage, msg = 'LED set to yellow'))
    return resp

@app.route("/purple")
def setPurple():
    rgbBlue = (154, 19, 212)
    setColors(rgbBlue)
    resp = make_response(render_template(homepage, msg = 'LED set to purple'))
    return resp

@app.route("/orange")
def setOranage():
    rgbBlue = (255, 30, 0)
    setColors(rgbBlue)
    resp = make_response(render_template(homepage, msg = 'LED set to orange'))
    return resp

@app.route("/white")
def setWhite():
    rgbBlue = (255, 255, 255)
    setColors(rgbBlue)
    setRGB(rgbBlue)
    resp = make_response(render_template(homepage, msg = 'LED set to white'))
    return resp

@app.route("/pink")
def setPink():
    rgbBlue = (254, 62, 253)
    setColors(rgbBlue)
    resp = make_response(render_template(homepage, msg = 'LED set to pink'))
    return resp

@app.route("/fadeoff")
def setFadeOff():
    global rgb
    light = True
    while (light):
        if (getRed > 1):
            setRed(getRed - 0.3)
        if (getGreen > 1):
            setGreen(getGreen - 0.3)
        if (getBlue > 1):
            setBlue(getBlue - 0.3)
        setColors(rgb)
        # if (red > 0 and blue > 0 and green > 0):
        if (getRed < 1 and getGreen < 1 and getBlue < 1):
            light = False
            setRGB((0, 0, 0))
    resp = make_response(render_template(homepage, msg = 'LED turned off'))
    return resp


#pi.stop()

def setColors(rgb):
    setRGB(rgb)
    pi.set_PWM_dutycycle(17, rgb[0])
    pi.set_PWM_dutycycle(22, rgb[1])
    pi.set_PWM_dutycycle(24, rgb[2])

def setColor():
    pi.set_PWM_dutycycle(17, red)
    pi.set_PWM_dutycycle(22, green)
    pi.set_PWM_dutycycle(24, blue)

# ================== Server startup ===================

if __name__ == "__main__":
    app.debug = True
    #app.run(host = '127.0.0.101',port=5005)
    app.run(host = '192.168.0.54',port=5005)
   