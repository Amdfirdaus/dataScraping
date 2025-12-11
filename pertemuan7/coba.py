from bs4 import BeautifulSoup
import fungsi1
import requests
import os


def main_scraper(url, directory, filename):
    fungsi1.create_directory(directory)
    print("Folder sudah dibuat:", directory)

    filepath = f"{directory}/{filename}"
    print("File output:", filepath)

    # Hapus file lama biar tidak menumpuk
    fungsi1.remove_file(filepath)
    fungsi1.create_new_file(filepath)

    # Ambil halaman utama
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text, "html.parser")

    # Cari semua artikel di halaman
    articles = soup.find_all("div", {"class": "article__box"})
    print("Jumlah artikel ditemukan:", len(articles))

    for article in articles:
        title_tag = article.find("div", {"class": "article_list_title"})
        asset_tag = article.find("div", {"class": "article__asset"})

        if not title_tag or not asset_tag or not asset_tag.a:
            continue

        judul = title_tag.text.strip()
        link = asset_tag.a.get("href")

        # Tulis judul dan URL ke file
        fungsi1.write_to_file(filepath, f"Judul : {judul}")
        fungsi1.write_to_file(filepath, f"URL   : {link}")

        print(f"Tulis: {judul}")
        print(f"URL  : {link}\n")

        # Ambil isi artikel lewat fungsi di fungsi1
        fungsi1.get_details(link, filepath)

    print("Selesai scraping semua artikel.")


# Jalankan program
main_scraper("https://tekno.kompas.com/gadget", "berita kompas", "artikel.doc")
