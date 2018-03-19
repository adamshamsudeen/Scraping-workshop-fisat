import requests
from bs4 import BeautifulSoup

dep= ['computer-science-engineering']
url="http://fisat.ac.in/department/"+str(dep[0])+"/faculty"

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

teachers= soup.find_all("div", class_="row events")
for teacher in teachers:
    url = teacher.a.get('href')
    image_url = teacher.find('img')['src']
    description = teacher.find("div", class_="event-body").p.text
    name = teacher.h2.text 
    designation = teacher.find("div", class_="event-header").p.text
    
    print(url,image_url,name,designation,description)
    # break
    file_path = '{loc}.txt'.format(loc=dep[0])

    with open(file_path, "a") as textfile:

        textfile.write(name)
