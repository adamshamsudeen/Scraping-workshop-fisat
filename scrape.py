import requests
from bs4 import BeautifulSoup


url="http://fisat.ac.in/department/mechanical-engineering/faculty"

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

teachers= soup.find_all("div", class_="row events")
for t in teachers:
    url = t.a.get('href')
    image_url = t.find('img')['src']
    description = t.find("div", class_="event-body").p.text
    name = t.h2.text 
    designation = t.find("div", class_="event-header").p.text
    
    print(url,image_url,name,designation,description)
    # break
