from selenium import webdriver
from bs4 import BeautifulSoup
import fungsi
import os
import time

def main_scraper(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
    }

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # AMBIL SEMUA ITEM BERITA
    items = soup.find_all("div", class_="article__list")

    print("Total artikel ditemukan:", len(items))

    for item in items:
        # Judul
        judul_tag = item.find("a", class_="article__link")
        judul = judul_tag.text.strip() if judul_tag else "-"

        # Isi Card (judul + kategori + tanggal)
        card = item.get_text(strip=True)

        print("Card :", card)
        print("Judul :", judul)
        print("=====================================")

    # SIMPAN HTML KE FILEg
    fungsi.create_directory('hasil')
    file_path = os.path.join('hasil', 'kompasparser.txt')
    fungsi.write_to_file(file_path, html)

    driver.quit()


main_scraper("https://tekno.kompas.com/gadget")
