import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "randomstring123")
messages = []  # a list to store our messages.

def add_messages(username, message):   # The method used to actually store the messages.
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")  # strftime takes the datetime.now and convert it to a string with the given format of hour:minute:second
    messages_dict = {"timestamp": now, "from": username, "message": message}  # A dictionary(or object in javascript).
    messages.append(messages_dict)  # appends above message to the messages list.

def get_all_messages():  # The metod to collect and add all messages.
    """Get all of the messages and separate them with a `br`"""
    return "<br>".join(messages)

@app.route("/", methods=["GET","POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":  # If post is triggered from this site, run:
        session["username"] = request.form["username"]
        # Store the input from the HTML-element named username in this session-variable called username.

    if "username" in session:   # If input(the username) is stored in session, run:
        return redirect(session["username"]) #Redirects the webbrowser to read the code in the route username below.

    return render_template("index.html")



@app.route("/<username>", methods=["GET", "POST"])  # Whatever is inside of the anglebrackets is a variable.
def user(username):  # user will take the argument of username.
    """Display chat messages"""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_messages(username, message)
        return redirect(session["username"])

    return render_template("chat.html", username=username,
                           chat_messages=messages)

app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "5000")), debug=False)