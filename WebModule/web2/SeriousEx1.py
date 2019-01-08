from flask import Flask, render_template, flash, request
from mongoengine import *
import mlab

mlab.connect()

class Account(Document):
    fullname = StringField(required = True)
    email = EmailField(required = True)
    username = StringField(max_length = 30, min_length = 6, required = True)
    password = StringField(max_length = 30, min_length = 6, required = True)

serious = Flask(__name__)

# @serious.route("/register")
# def register():
#     return render_template('register.html')

@serious.route("/register", methods = ['GET','POST'])
def register():
    """Add a new account"""

    if request.method == 'POST':
        new_account = Account(fullname = request.form['fullname'],
                                email = request.form['email'],
                                username = request.form['username'],
                                password = request.form['password'])
       
        new_account.save()
        return "Welcome"
    else:
        return render_template('register.html')

if __name__ == '__main__':
    serious.run(debug = True)