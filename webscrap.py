from bs4 import BeautifulSoup
import requests
import time


url= "https://mx.computrabajo.com/trabajo-de-python"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}



def find_jobs():
    html_text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')


    jobs = soup.find_all('article', class_= 'box_offer')

    for job in jobs:
        published_date= job.find('p', class_='fs13 fc_aux').text
        if 'horas' in published_date:
            company_name = job.find('p', class_= 'fs16 fc_base mt5 mb5').text
            job_offer = job.find('h2', class_="fs18 fwB").text
            job_link = job.find('a')['href'].strip().split('/')[-2]
            link = "{}/{}".format(url, job_link)
        
        
            print(f'Company: {company_name.split()[0].strip()}') 
            print(f'Job offer: {job_offer.strip()}')
            print(f'Published date: {published_date.strip()}')
            print(f"Link: {link}")
            print("")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} seconds ...')
        time.sleep(time_wait)
