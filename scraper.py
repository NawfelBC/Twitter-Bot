import requests
from bs4 import BeautifulSoup as bs
import json
import time

def scrape_to_json():

    titles_list = []
    release_dates_list = []
    images_list = []
    rates_list = []

    for i in range(1,26):
    
        URL = f"https://www.listchallenges.com/top-1000-movies-of-the-21st-century-tspdt/list/{i}"

        page = requests.get(URL)
        soup = bs(page.content, "html.parser")

        titles = soup.find_all('div', class_="item-name")
        for movie in titles:
            #Get titles
            titles_list.append(movie.getText().split(' (')[0])

            #Get release dates
            release_dates_list.append(movie.getText().split(' (')[1].replace(')',''))

        # Get rates
        rates = soup.find_all('div', class_='rt-score')
        for rate in rates:
            if rate.getText() != '':
                rates_list.append(rate.getText().split('  ')[1].replace('%',''))
            else:
                rates_list.append('N/A')

        # Get images
        images = soup.find_all('img', alt = True)
        for image in images[1:41]:
            if image.has_attr('data-src'):
                images_list.append('http://www.listchallenges.com'+image['data-src'])
            else:
                images_list.append('http://www.listchallenges.com'+image['src'])

        print(f'Page {i} done !')  
        time.sleep(1)

    #Clean the data
    titles_list = [x.replace('\r','').replace('\n','').replace('\t','') for x in titles_list]
    release_dates_list = [x.replace('\r','').replace('\n','').replace('\t','') for x in release_dates_list]

    #Create JSON
    collection = []

    for i in range(len(titles_list)):
        data = {'title': titles_list[i], 'release_date': release_dates_list[i], 'rate': rates_list[i], 'image': images_list[i]}
        collection.append(data)

    with open('data.json', mode='w', encoding='utf-8') as file:
        json.dump(collection, file, ensure_ascii=False)

# scrape_to_json()