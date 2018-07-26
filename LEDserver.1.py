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

def setRGB(newRgb):
    global rgb
    rgb = newRgb

def setRedLED(newred):
    global red
    red = newred

def setGreenLED(newGreen):
    global green
    green = newGreen

def setBlueLED(newBlue):
    global blue
    blue = newBlue

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
    currentRgb = rgb
    light = True
    while (light):
        if (currentRgb[0] > 1):
            red = currentRgb[0] - 0.3
            setRGB((red, currentRgb[1], currentRgb[2]))
            setRedLED(red - 0.3)
        if (currentRgb[1] > 1):
            green = currentRgb[1] - 0.3
            setRGB((currentRgb[0], green, currentRgb[2]))
        if (currentRgb[2] > 1):
            blue = currentRgb[2] - 0.3
            setRGB((currentRgb[0], currentRgb[1], blue))
        setColors(currentRgb)
        # if (red > 0 and blue > 0 and green > 0):
        if (red < 1 and blue < 1 and green < 1):
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
   