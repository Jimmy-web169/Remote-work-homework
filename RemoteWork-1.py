from datetime import date
import bs4
import pandas
import urllib.request as req
url = "https://cn.investing.com/equities/apple-computer-inc-historical-data"
# 建立一個Request 物件，附加Request Headers 的資訊
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

root = bs4.BeautifulSoup(data, "html.parser")
# print(root.title.string)

data1 = root.select_one("#results_box")

db = pandas.read_html(data1.prettify())

a = len(db)

a = db[0]

print(a)
