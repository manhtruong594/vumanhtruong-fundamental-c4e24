from mongoengine import *

class Bikes(Document):
    model= StringField()
    fee= IntField()
    image= StringField()
    year= IntField()
    

