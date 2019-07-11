from SWTApp import app

from flask import render_template,redirect,url_for,request,flash


@app.route('/')
def index():    
    return render_template("SWTIndex.html")


@app.route('/caddis')
def caddis():
    return render_template("caddisBug.html")


@app.route('/chironomids')
def chironomids():
    return render_template("chironomidBug.html")


@app.route('/damsels')
def damsels():
    return render_template("damselBug.html")


@app.route('/dragons')
def dragons():
    return render_template("dragonBug.html")


@app.route('/leeches')
def leeches():
    return render_template("leechBug.html")


@app.route('/mayflies')
def mayflies():
    return render_template("mayflyBug.html")


@app.route('/scuds')
def scuds():
    return render_template("scudBug.html")


# begin the patterns

@app.route('/caddis_patterns')
def caddis_pattern():
    return render_template("caddisPatterns.html")


@app.route('/chironomid_patterns')
def chironomidPattern():
    return render_template("chironomidPatterns.html")


@app.route('/damsel_patterns')
def damselPattern():
    return render_template("damselPattern.html")


@app.route('/dragon_patterns')
def dragonPattern():
    return render_template("dragonPattern.html")


@app.route('/leech_patterns')
def leechPattern():
    return render_template("leechPattern.html")


@app.route('/mayfly_patterns')
def mayflyPattern():
    return render_template("mayflyPattern.html")


@app.route('/scud_patterns')
def scudPattern():
    return render_template("scudPattern.html")


# begin technique pages
@app.route('/fishing_deep')
def deep():
    return render_template("deep.html")


@app.route('/sink_float')
def sink():
    return render_template("sinkFloat.html")


@app.route('/indicator')
def indicatr():
    return render_template("indicator.html")


@app.route('/knots')
def knots():
    return render_template("knots.html")

# begin gear views
@app.route('/boats')
def boats():
    return render_template("boats.html")


@app.route('/motors')
def motors():
    return render_template("motors.html")


@app.route('/rods')
def rods():
    return render_template("rods.htm")


@app.route('/reels')
def reels():
    return render_template("reels.html")


@app.route('/gear')
def gear():
    return render_template("gear.html")