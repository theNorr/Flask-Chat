import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Main page with instructions"""
    return "To send a message use: /USERNAME/MESSAGE"


@app.route("/<username>")  # Whatever is inside of the anglebrackets is a variable.
def user(username):  # user will take the argument of username.
    return "Hi " + username


@app.route("/<username>/<message>")
def send_message(username, message):
    return "{0}: {1}".format(username, message)  # returns the username and the message.


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)