import requests
from bs4 import BeautifulSoup

#URL page
url= 'https://auto.ru/'

#Send URL to page
response = requests.get(url)

#Check response success 
if response.status_code == 200:
    #Create object BeautifulSoup for HTML analyz 
    soup = BeautifulSoup(response.content, 'html.parser')

    #Searching for elements with current class or tags and get necessary info
    ###Headers 
    titles = soup.find_all('h3', class_='ListingItemTitle-module--container')

    #Print elements info 
    ###Headers
    for title in titles:
        print(title.text)
else:
    print('Error while getting page:', response.status_code)



