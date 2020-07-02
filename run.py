import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []  # a list to store our messages.

def add_messages(username, message):   # The method used to actually store the messages.
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")  # strftime takes the datetime.now and convert it to a string with the given format of hour:minute:second
    messages.append("({}) {}: {}".format(now, username, message))

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



@app.route("/<username>")  # Whatever is inside of the anglebrackets is a variable.
def user(username):  # user will take the argument of username.
    """Display chat messages"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages()) # .format()-method adds the username instead of the placeholder, calls on the function get_all_messages


@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)  # calls the function add_messages and passes in the username: and message.
    return redirect("/" + username)  # redirects the user to the url index/username

app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)