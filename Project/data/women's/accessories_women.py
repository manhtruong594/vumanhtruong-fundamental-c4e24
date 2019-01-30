from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

# DOWNLOAD PAGE >>>>>>>>>>>>>>>>
url = "https://topodesigns.com/collections/womens-accessories"
conn = urlopen(url)             # Open connection to server
raw_data = conn.read()          # Read data
page_content = raw_data.decode("utf8")   # Decode data
# print(page_content)

# f = open("dantri.html", "wb")       # w: write, b: save file in raw data
# f.write(raw_data)
# f.close()

# EXTRACT ROI (Region of interest) >>>>>>>>>>>>>>
soup = BeautifulSoup(page_content, "html.parser")
# print(soup.prettify())
div = soup.find("div", "site-content col-sm-12", role="main")
# print(ul.prettify())


# EXTRACT DATA >>>>>>>>>
li_list = div.find_all("img")
# print(li_list)
span_list = div.find_all("span", "price")

# for st in span_list:
#     print(st.prettify()) 

# for li in li_list:
#     print(li.prettify())

news_list = []
for st in li_list:
    image = st['src']
    name = st['alt']
    print(name)
    print(image)

    news = OrderedDict({
        "Name": name,
        "Image": image,
    })
    news_list.append(news)
    # print("__________________")

price_list = []
for st in span_list:
    price = st.string
    price_list.append(price)
print(price_list)


# SAVE DATA TO EXCEL >>>>>>>>>>>>>>>>
pyexcel.save_as(records= news_list, dest_file_name = "women_accessories.xlsx")