# from bs4 import BeautifulSoup

# html = '''
# <html>
#   <body>
#     <div class="class1"></div>
#     <div class="class2"></div>
#     <div class="class3"></div>
#   </body>
# </html>
# '''

# soup = BeautifulSoup(html, 'html.parser')

# hasil = soup.find_all(True, {"class": ["class1", "class2"]})

# print(hasil)

# ===================hbuhb========================
from bs4 import BeautifulSoup
import fungsi1
import requests

def main_scraper(url, directory):
    fungsi1.create_directory(directory)  # Membuat Directory
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, 'html.parser')

    articles2 = soup.find("div", {'class': 'row article__wrap__grid--flex col-offset-fluid mt2'})
    articles2 = soup.find_all(True, {'class': ['article__box']})  # Penulisan Multiple class

    # for article in articles2:
    #     print("URL 1 : " + article.a.get("href"))
    #     print("Judul 1 : " + article.text)
    #     print()

    for article2 in articles2:
        print("URL 2 : " + article2.a.get("href"))
        print("Judul 2 : " + article2.text)
        print()
        

main_scraper("https://tekno.kompas.com/gadget", "Hasil")
