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

red = 0
green = 0
blue = 0

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
def setRed():
    red = (255, 0, 0)
    setColor(red)
    return make_response(render_template("index.html", msg = 'LED set to Red'))


@app.route("/greennew")
def setGreen():
    setRedLED(0)
    setGreenLED(255)
    setBlueLED(0)
    setColor()
    resp = make_response(render_template("index.html", msg = 'LED set to Green'))
    return resp

@app.route("/bluenew")
def setBlue():
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
    setRedLED(255)
    setGreenLED(0) 
    setBlueLED(0)
    setColor()
    return make_response(render_template(homepage, msg = 'LED set to Red'))


@app.route("/green")
def setGreen():
    setRedLED(0)
    setGreenLED(255)
    setBlueLED(0)
    setColor()
    resp = make_response(render_template(homepage, msg = 'LED set to Green'))
    return resp

@app.route("/blue")
def setBlue():
    setRedLED(0)
    setGreenLED(0)
    setBlueLED(255)
    setColor()
    resp = make_response(render_template(homepage, msg = 'LED set to Blue'))
    return resp

@app.route("/off")
def setOff():
    setRedLED(0)
    setGreenLED(0)
    setBlueLED(0)
    setColor()
    resp = make_response(render_template(homepage, msg = 'LED turned off'))
    return resp


@app.route("/yellow")
def setYellow():
    setRedLED(255)
    setGreenLED(128)
    setBlueLED(0)
    setColor()
    resp = make_response(render_template(homepage, msg = 'LED set to yellow'))
    return resp

@app.route("/purple")
def setPurple():
    setRedLED(154)
    setGreenLED(19)
    setBlueLED(212)
    setColor()
    resp = make_response(render_template(homepage, msg = 'LED set to purple'))
    return resp

@app.route("/orange")
def setOranage():
    setRedLED(255)
    setGreenLED(30)
    setBlueLED(0)
    setColor()
    resp = make_response(render_template(homepage, msg = 'LED set to orange'))
    return resp

@app.route("/white")
def setWhite():
    setRedLED(255)
    setGreenLED(255)
    setBlueLED(255)
    setColor()
    resp = make_response(render_template(homepage, msg = 'LED set to white'))
    return resp

@app.route("/pink")
def setPink():
    setRedLED(254)
    setGreenLED(62)
    setBlueLED(253)
    setColor()
    resp = make_response(render_template(homepage, msg = 'LED set to pink'))
    return resp

@app.route("/fadeoff")
def setFadeOff():
    light = True
    while (light):
        if (red > 1):
             setRedLED(red - 0.3)
        if (green > 1):
            setGreenLED(green - 0.3)
        if (blue > 1):
            setBlueLED(blue - 0.3)
        setColor()
        # if (red > 0 and blue > 0 and green > 0):
        if (red < 1 and blue < 1 and green < 1):
            light = False
            setRedLED(0)
            setGreenLED(0)
            setBlueLED(0)
    resp = make_response(render_template(homepage, msg = 'LED turned off'))
    return resp




#pi.stop()

def setColor22(red, green, blue):
    pi.set_PWM_dutycycle(17, red)
    pi.set_PWM_dutycycle(22, green)
    pi.set_PWM_dutycycle(24, blue)

def setColor():
    pi.set_PWM_dutycycle(17, red)
    pi.set_PWM_dutycycle(22, green)
    pi.set_PWM_dutycycle(24, blue)

# ================== Server startup ===================

if __name__ == "__main__":
    app.debug = True
    #app.run(host = '127.0.0.101',port=5005)
    app.run(host = '192.168.0.54',port=5005)
   