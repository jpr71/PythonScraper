import requests
from bs4 import BeautifulSoup

url = "http://www.mech.northwestern.edu/courses/index.html"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
  if "descriptions/" in link.get("href"):
    ending = str(link.get("href"))
    url1 = str("http://www.mech.northwestern.edu/courses/%s"  %ending)
    site = requests.get(url1)
    content = BeautifulSoup(site.content)
    file = open(link.text + '.html',"wb")
    file.writelines(site.content)
    file.close()


