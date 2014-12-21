import requests
from bs4 import BeautifulSoup

url = "http://www.civil.northwestern.edu/course_schedule/index.html"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
  if "course_pages" in link.get("href"):
    url1 = str (link.get("href"))
    site = requests.get(url1)
    content = BeautifulSoup(site.content)
    file = open(link.text + '.html',"wb")
    file.writelines(site.content)
    file.close()
