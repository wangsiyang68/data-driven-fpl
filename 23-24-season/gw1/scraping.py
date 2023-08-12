from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://fbref.com/en/comps/9/2021-2022/stats/2021-2022-Premier-League-Stats"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")