from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://en.wikipedia.org/wiki/Randall_Road'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

print(page_soup.prettify())