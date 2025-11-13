from bs4 import BeautifulSoup
from os import system
import os 
import utsfungsi
import requests

def get_details(url):
    souce_code = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    souce_text = souce_code.text
    soup = BeautifulSoup(souce_text, 'html.parser')
    devE = soup.find('div', {'class': 'read__content'})
    if devE:
        utsfungsi.write_to_file('hasil/artikel.doc', devE.text)
        utsfungsi.write_to_file('hasil/artikel.doc', "------------")
    else:
        print("Tidak menemukan isi artikel:", url)

def main_scrapper(url, directory, file):
    utsfungsi.create_directory(directory)
    source_code = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")

    # struktur lama sudah tidak ada, jadi langsung ambil h3.article__title
    articles4 = soup.find_all("h3", class_="article__title")

    if not articles4:
        print("Tidak menemukan artikel pada halaman.")
        return

    for article4 in articles4:
        file_path = os.path.join(directory, file)
        link = article4.a.get("href")
        title = article4.text.strip()
        if not link.startswith("http"):
            link = "https://tekno.kompas.com" + link

        utsfungsi.write_to_file(file_path, "URL: " + link)
        utsfungsi.write_to_file(file_path, "Title: " + title + "\n")
        print("Mengambil:", title)
        get_details(link)

utsfungsi.remove_file("hasil/artikel.txt")
utsfungsi.remove_file("hasil/artikel.doc")
main_scrapper("https://tekno.kompas.com/gadget", "hasil", "artikel.txt")
