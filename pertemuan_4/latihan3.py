# import requests
# from bs4 import BeautifulSoup 
# import fungsi  

# result = requests.get("https://www.detik.com/")
# print(result)
# print(result.encoding)
# print(result.status_code)
# print(result.elapsed)
# print(result.url)
# print(result.history)
# print(result.headers["Content-Type"])

# # LOGIC
# def main_scraper(url, directory):
#     fungsi.create_directory(directory)  
#     source_code = requests.get(url)
#     source_text = source_code.text
#     soup = BeautifulSoup(source_text, "html.parser")  

#     # print(soup.find_all("div", {"class": "media media--image-radius block-link"}))
    
#     products = soup.find_all("div", class_="media_image")

#     for p in products:
#         title = p.find("a", class_="title").get_text(strip=True)
#         price = p.find("span", class_="price").get_text(strip=True)
#         print(f"Nama: {title} | Harga: {price}")

# # Jalankan fungsi utama
# main_scraper("https://www.detik.com/", "hasil")


import requests
from bs4 import BeautifulSoup
import pertemuan4.fungsi as fungsi

def main_scraper(url, directory):
    fungsi.create_directory(directory)

    # Ambil halaman web
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Cari semua artikel yang sesuai class
    articles = soup.find_all("article", class_="list-content__item column-4 recommendation_firstrow")

    print(f"🔍 Ditemukan {len(articles)} artikel dengan class tersebut.\n")

    # Loop setiap artikel
    for art in articles:
        a_tag = art.find("a", class_="media__link")
        if a_tag:
            link = a_tag.get("href")
            title_div = art.find("div", class_="media__title")
            image_tag = art.find("img")

            title = title_div.get_text(strip=True) if title_div else "Tidak ada judul"
            image = image_tag.get("src") if image_tag else "Tidak ada gambar"

            print(f" Judul : {title}")
            print(f" Link  : {link}")
            print(f" Gambar: {image}")
            print("-" * 80)

main_scraper("https://www.detik.com/", "Hasil")
