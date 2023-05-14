import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')


url = "https://itc.gymkhana.iitb.ac.in/wncc/soc/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())
projects = soup.find_all('div', {'class': 'col-lg-4 col-6 mb-4 shuffle-item'})


data = []
for project in projects:
    project_incomplete_url = project.find('a').get('href')
    complete_url = "https://itc.gymkhana.iitb.ac.in" + project_incomplete_url
    title = project.find('p').text.strip()
    length = len(project.get('data-groups'))
    category = project.get('data-groups')[2:length - 9]


    data.append([title, category, complete_url])

df = pd.DataFrame(data, columns=['Project Title', 'Category', 'URL'])
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.to_csv('soc_projects.csv', index = False)