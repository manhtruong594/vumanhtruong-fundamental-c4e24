from pymongo import MongoClient

uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(uri)
db = client.get_database()

post_collection = db["posts"]
new_post = {
    "title": "Đúng người đúng thời điểm",
    "author": "manhtruong",
    "content": '''Title hơi xàm, thật ra thời điểm là hơi sai, giá như mình nhận ra mình thích lập trình sớm hơn.
                Bây giờ đi làm, ảnh hưởng rất nhiều tới việc học, thật sự ko muốn chút nào, nhưng thôi, muộn còn hơn không
                lớp học thật sự rất vui, rất nhiệt tình, triệu like !!! '''
}

# post_collection.insert_one(new_post)
# client.close()
for st in post_collection.find():
    print(st)