from flask import *
from mongoengine import *
# import mlab

# mlab.connect()
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route("/men's_tops")
def top_men():
  return render_template('top_men.html')



if __name__ == '__main__':
  app.run(debug=True)