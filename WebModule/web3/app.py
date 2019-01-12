from flask import *
from mongoengine import *
# from models.service import Service
import mlab

mlab.connect()

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome !!'

@app.route('/Africa_rivers')
def Africa():
    africa_rivers = River.objects(continent__icontains='Africa')
    return render_template('river.html',africa_rivers = africa_rivers)

@app.route('/S_america_rivers')
def SAmerica():
    s_america_rivers = River.objects(continent__icontains='S. America', length_lt= 1000)
    return render_template('river2.html', s_america_rivers = s_america_rivers)


if __name__ == '__main__':
  app.run(debug=True)