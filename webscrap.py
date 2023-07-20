from bs4 import BeautifulSoup
import requests



url= "https://mx.computrabajo.com/trabajo-de-python"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

html_text = requests.get(url, headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')


jobs = soup.find_all('article', class_= 'box_offer')

for job in jobs:
    published_date= job.find('p', class_='fs13 fc_aux').text
    if 'horas' in published_date:
        company_name = job.find('p', class_= 'fs16 fc_base mt5 mb5').text
        job_offer = job.find('h2', class_="fs18 fwB").text
       
        print(f'Company: {company_name.split()[0]}') 
        print(f'Job offer: {job_offer.strip()}')
        print(f'Published date: {published_date.strip()}')
        print("")