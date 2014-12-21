import requests
from bs4 import BeautifulSoup

url = "http://www.medill.northwestern.edu/imc/full-time/curriculum/"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
  if "imc-course-" in link.get("href"):
    ending = str (link.get("href").lstrip('../../'))
    url1 = str("http://www.medill.northwestern.edu/imc/%s"  % ending)
    site = requests.get(url1)
    content = BeautifulSoup(site.content)
    title = link.find("strong").text
    file = open(title + '.html',"wb")
    file.writelines(site.content)
    file.close()

