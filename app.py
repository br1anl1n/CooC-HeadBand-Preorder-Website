import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from datetime import datetime
# from flask_mail import Mail


# Configure application
app = Flask(__name__)

"""
app.config['MAIL_SERVER']='smtp.gmail.com'
app.mapp.config['MAIL_PORT'] = 465
app.mapp.config['MAIL_USERNAME'] = 'cooc.hreadband@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

"""


# Configure session to use filesystem (instead of signed cookies)
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///cooc.db")

# Direct to homepage
@app.route("/")
def index():
    # SQL to get the name and adress
    return render_template("home.html")
    '''
    name = db.execute("SELECT name FROM users")
    msg = Message('Order Receipt', sender ='cooc.headhand@gmail.com', recipients = name)
    msg.body = recipients, "thank you for your order of Cooc Headband!"
    mail.send(msg)
    return "Message sent!"
    

    if __name__ == '__main__':
        app.run(debug = True)
    '''



# Direct to product page
@app.route("/product")
def product():
    return render_template("product.html")

# Direct to support page
@app.route("/support")
def support():
    return render_template("support.html")

# Direct to preorder page
@app.route("/preorder", methods=["GET", "POST"])
def preorder():
    if request.method == "POST":

        #Assign values to variables from the input from the form
        name = request.form.get("name")
        email = request.form.get("email")
        quantity = request.form.get("quantity")
        address = request.form.get("address")
        phone = request.form.get("phone")

        #To understand the following code, here's .schema of the database
        #There are two tables: users and preorders

        """
        CREATE TABLE users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        address TEXT,
        phone_number TEXT
        );

        CREATE TABLE preorders (
        user_id INTEGER,
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        quantity INTEGER,
        time DATETIME,
        FOREIGN KEY(user_id) REFERENCES users(user_id));
        """

        #Insert value into user database to get information about all the users
        db.execute("INSERT INTO users(name, email, address, phone_number) VALUES(?, ?, ?, ?)", name, email, address, phone)

        #Select the most recent user_id, which is the one right now
        id = db.execute("SELECT user_id FROM users")
        user_id = id[-1]["user_id"]

        #Insert the data into the preorder forms. 
        db.execute("INSERT INTO preorders(user_id, quantity, time) VALUES(?, ?, ?)", user_id, quantity, datetime.now())
        
        #redirect to preorder form
        return render_template("thankyou.html")

    else:
        #if method is get, render preorder
        return render_template("preorder.html")
