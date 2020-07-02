import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []  # a list to store our messages.

def add_messages(username, message):   # The method used to actually store the messages.
    """Add messages to the `messages` list"""
    messages.append("{}: {}".format(username, message))

def get_all_messages():  # The metod to collect and add all messages.
    """Get all of the messages and separate them with a `br`"""
    return "<br>".join(messages)

@app.route("/")
def index():
    """Main page with instructions"""
    return "To send a message use: /USERNAME/MESSAGE"


@app.route("/<username>")  # Whatever is inside of the anglebrackets is a variable.
"""Display chat messages"""
def user(username):  # user will take the argument of username.
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages()) # .format()-method adds the username instead of the placeholder, calls on the function get_all_messages


@app.route("/<username>/<message>")
"""Create a new message and redirect back to the chat page"""
def send_message(username, message):
    add_messages(username, message)  # calls the function add_messages and passes in the username: and message.
    return redirect("/" + username)  # redirects the user to the url index/username

app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)