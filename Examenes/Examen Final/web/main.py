from flask import Flask, request, make_response, redirect, render_template, url_for

app = Flask(__name__)

@app.route("/")
def mainRoute():
    return redirect(url_for("homeRoute"))

@app.route("/home")
def homeRoute():
    return render_template("home.html")

@app.route("/patients")
def doctorsRoute():
    return render_template("patients.html")

@app.route("/doctors")
def servicesRoute():
    return render_template("doctors.html")

@app.route("/aboutus")
def aboutRoute():
    return render_template("aboutus.html")

@app.route("/contact")
def contactRoute():
    return render_template("contact.html")

@app.route("/fact")
def factRoute():
    return render_template("fact.html")

if (__name__ == "__main__"):
    app.run()