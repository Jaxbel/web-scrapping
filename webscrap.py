from bs4 import BeautifulSoup
import requests



url= "https://mx.computrabajo.com/trabajo-de-python"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

html_text = requests.get(url, headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')


jobs = soup.find('article', class_= 'box_offer')
company_name = jobs.find('p', class_= 'fs16 fc_base mt5 mb5').text
job_offer = jobs.find('h2', class_="fs18 fwB").text
published_date= jobs.find('p', class_='fs13 fc_aux').text



print(f'''
Job offer: {job_offer}
Company: {company_name.split()[0]}
Published date: {published_date}

''')
