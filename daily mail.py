#1st step install and import modules
import requests
from bs4 import BeautifulSoup as bs
import csv
from itertools import zip_longest
news_titles = []

#2nd step use requests to fetch the url
URL = "https://www.dailymail.co.uk/news/russia-ukraine-conflict/index.html?page="

#3rd step save page content/markup
for page in range(1,10):
      # pls note that the total number of
    # pages in the website is more than 5000 so i'm only taking the
    # first 10 as this is just an example
  
    req = requests.get(URL + str(page))
    soup = bs(req.text, 'html.parser')
  
    titles = soup.find_all('h2',attrs={'class':'linkro-darkred'})
  
    for title in titles:
        news_titles.append(title.text)
print(news_titles)
        
#4th step create soup object to parse content

#5th step find the elements containing info we need
#-- job titles, job skills, company names, location names الحاجات اللى احنا عايزينها

#6th step loop over returned lists to extract needed info into other lists

    

#7th step create csv file and fill it with values
file_list = [news_titles]
exported = zip_longest(*file_list) #دي الفانكشن اللى بتجيب واحد من كل ليسته جنب بعض 
with open("E:/programming/web scraping/news_dailymail.csv" , "w" ) as myfile :
    wr = csv.writer(myfile)
    wr.writerow(["Russia Ukranie news"])
    wr.writerows(exported)