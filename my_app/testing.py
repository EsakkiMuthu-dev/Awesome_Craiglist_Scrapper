import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup
url='https://chennai.craigslist.org/d/services/search/bbb?query=computer&sort=rel'
image_url = requests.get('https://bangalore.craigslist.org/hss/d/best-budget-interior-designers-in/7376300020.html')
soup = BeautifulSoup(image_url.text,'html.parser')
l = soup.find('div',class_='slide first visible')
image_url = l.find('img')
print(image_url)
print(image_url['src'])
