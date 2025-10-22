from bs4 import BeautifulSoup
import fungsi1
import requests

def main_scraper(url, directory):
    fungsi1.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text,'html.parser')
    
    articlepop = soup.find("div", {'class': 'mostList -mostlist -mostArticle most_side'})
    articlepop = soup.find_all(True,{'class': ['mostItem']})
    
    
    for articlepop in articlepop:
        print("URL : " + articlepop.a.get("href"))
        print("Judul : " + articlepop.text)

main_scraper("https://www.kompas.com/nusaraya?source=navbar", "Hasil")