from pymongo import MongoClient
from matplotlib import pyplot

uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(uri)
db = client.get_database()

customers_collection = db["customers"]
events_cus = 0
wom_cus = 0
ads_cus = 0
for st in customers_collection.find():
    if st['ref'] == "events":
        events_cus += 1
    elif st['ref'] == "wom":
        wom_cus += 1
    elif st['ref'] == 'ads':
        ads_cus +=1

cus_refs = [events_cus, wom_cus, ads_cus]
print(cus_refs)

pyplot.pie(cus_refs, labels = ["EVENTS"," WOM","ADS"], autopct = "%.1f%%",shadow = True)
pyplot.axis("equal")
pyplot.title('Customers references percentage')
pyplot.show()

client.close