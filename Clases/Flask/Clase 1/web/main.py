from flask import Flask, request, make_response, redirect, render_template, url_for

app = Flask(__name__)

@app.route("/")
def mainRoute():
    user_ip = request.remote_addr
    response = make_response(redirect("login"))
    response.set_cookie("ip", user_ip)
    response.set_cookie("fwfwfp", "wdswdwd")
    return redirect(url_for("loginRoute"))

@app.route("/home")
def homeRoute():
    return render_template("home.html")

@app.route("/login", methods = ["POST","GET"])
def loginRoute():
    if request.method == "POST":
        _username = request.form["username"]
        _password = request.form["password"]

        if (_password == "hola1234"):
            return  redirect(url_for("homeRoute"))

        else:
            return render_template("failedLogin.html")

    else: 
        return render_template("login.html")

@app.route("/personas")
def personasRoute():
    return render_template("personas.html")

@app.route("/lugares")
def lugaresRoute():
    return render_template("lugares.html")

if (__name__ == "__main__"):
    app.run()