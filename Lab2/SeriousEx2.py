from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#1 DOWNLOAD ----------------------
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)             # Open connection to server
raw_data = conn.read()          # Read data
page_content = raw_data.decode("utf8")   # Decode data

#2 --------------------------
soup = BeautifulSoup(page_content, "html.parser")
ul = soup.find("table", id="tableContent")
# print(ul.prettify())
tr_list = ul.find_all("tr")

#3 ---------------------------
data_list = []
one_line = []
for tr in tr_list:
    td_list = tr.find_all("td")
    for td in td_list:
        td_content = {
            "content": td.string
        }
        data_list.append(td_content)
print(data_list)
pyexcel.save_as(records=data_list,dest_file_name="cafef.xlsx")
