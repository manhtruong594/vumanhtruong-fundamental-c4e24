from mongoengine import *
import mlab
from flask import *
from models.bike import Bikes
app = Flask(__name__)

mlab.connect()

@app.route('/')
def home():
    return 'Welcome'

@app.route('/new-bike', methods=["GET", "POST"])
def add_bike():
  if request.method == 'GET':
    return render_template('bike.html')
  elif request.method == 'POST':
    form = request.form
    model = form['model']
    fee = form['fee']
    image= form['image']
    year= form['year']
    print(model, fee, year)
    new_bike = Bikes(model = model, fee = fee, image = image, year = year)
    new_bike.save()
    return 'OK!!'
  

if __name__ == '__main__':
  app.run(debug=True)