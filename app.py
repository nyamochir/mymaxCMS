# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:00:34 2020

@author: nyamo
"""

from flask import Flask, render_template
from data import contacts
app = Flask(__name__)
# or 

Contacts = contacts()
@app.route("/")
def index():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html", contacts = Contacts)


@app.route("/contacts/<string:Employee_code>/")
def contact(Employee_code):
    return render_template("contact.html", Employee_code = Employee_code )


if __name__ == "__main__":
    app.run(debug = True)# always running the server while updating
    