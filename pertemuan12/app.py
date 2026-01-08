from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def format_tanggal(tanggal_raw):
    if not tanggal_raw:
        return "Tanggal tidak tersedia"

    # contoh: "Selasa, 7 Jan 2026 10:30 WIB"
    # kita potong jamnya
    parts = tanggal_raw.split(" ")
    if len(parts) >= 4:
        return " ".join(parts[:4])
    return tanggal_raw


@app.route("/")
def index():
    url = "https://www.detik.com/jatim/berita/indeks"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    html_doc = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_doc.text, "html.parser")

    data = []

    articles = soup.find_all("article")

    for a in articles:
        title = a.find("h3", class_="media__title")
        image = a.find("div", class_="media__image")
        date = a.find("span", class_="media__date")

        if title and image:
            img_tag = image.find("img")
            img_url = img_tag.get("data-src") or img_tag.get("src")

            tanggal_raw = date.get_text(strip=True) if date else ""
            tanggal = format_tanggal(tanggal_raw)

            data.append({
                "judul": title.get_text(strip=True),
                "gambar": img_url,
                "tanggal": tanggal
            })

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
