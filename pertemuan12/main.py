import requests
from bs4 import BeautifulSoup

html_doc = requests.get("https://www.detik.com/jatim/berita/indeks")

soup = BeautifulSoup(html_doc.text, 'html.parser')

populer_area = soup.find(attrs={'class': 'grid-row list-content'})

titles = populer_area.findAll(attrs={'class': 'media__title'})
images = populer_area.findAll(attrs={'class': 'media__image'})
dates = populer_area.findAll(attrs={'class': 'media__date'})

for title, image, date in zip(titles, images, dates):
    judul = title.get_text(strip=True)
    img_url = image.find('a').find('img')['src']
    tanggal = date.get_text(strip=True)
    
    print(f"Title: {judul}")
    print(f"Image URL: {img_url}")
    print(f"Date: {tanggal}")
    print("-" * 40)
     