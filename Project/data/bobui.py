from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

# DOWNLOAD PAGE >>>>>>>>>>>>>>>>
url = "https://bobui.vn/shop"
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
ul = soup.find("div", "archive-products")
# print(ul.prettify())


# EXTRACT DATA >>>>>>>>>
li_list = ul.find_all("li")
# print(li_list)

# for li in li_list:
#     print(li.prettify())

news_list = []
for st in li_list:
    a = st.img
    image = a['src']
    name = st.h3.string
    price = st.span.string
    print(price)
    print(name)
    # h4 = li.h4
    # a = h4.a            # or a = li.h4.a or a = li.a
    # title = a.string    # extract title
    # # print(title)
    # link = url + a["href"]    # extract href
    # # print(link)
    print(image)

    # news = OrderedDict({
    #     "Name": name,
    #     "Image": image,
    # })
    # news_list.append(news)
    # print("__________________")
# print(news_list)

# # SAVE DATA TO EXCEL >>>>>>>>>>>>>>>>
# pyexcel.save_as(records= news_list, dest_file_name = "data.xlsx")