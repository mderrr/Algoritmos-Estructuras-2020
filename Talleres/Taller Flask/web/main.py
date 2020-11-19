from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    user_ip = request.remote_addr
    response = make_response(redirect("hello"))
    response.set_cookie("ip", user_ip)
    response.set_cookie("fwfwfp", "wdswdwd")
    return response

@app.route("/hello")
def helloRoute():
    return render_template("hello.html")

if (__name__ == "__main__"):
    
    app.run()