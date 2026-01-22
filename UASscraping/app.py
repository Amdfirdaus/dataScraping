from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://www.detik.com/jatim/berita/indeks"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article")[:20]

    temp_data = []

    # === Ambil SEMUA data (judul, gambar, tanggal) ===
    for a in articles:
        title = a.find("h3", class_="media__title")
        image = a.find("div", class_="media__image")
        date = a.find("span", class_="media__date")

        if title and image:
            img_tag = image.find("img")
            img_url = img_tag.get("data-src") or img_tag.get("src")

            judul = title.get_text(strip=True)
            tanggal = date.get_text(strip=True) if date else "-"

            temp_data.append({
                "judul": judul,
                "gambar": img_url,
                "tanggal": tanggal,
                "panjang": len(judul)
            })

    # === Hitung rata-rata panjang judul ===
    rata_rata = sum(d["panjang"] for d in temp_data) / len(temp_data)

    # === Tentukan warna & indikator ===
    data = []
    for d in temp_data:
        if d["panjang"] >= rata_rata:
            warna = "table-success"  # hijau
            indikator = "H"
        else:
            warna = "table-danger"   # merah
            indikator = "M"

        data.append({
            "judul": d["judul"],
            "gambar": d["gambar"],
            "tanggal": d["tanggal"],
            "panjang": d["panjang"],
            "warna": warna,
            "indikator": indikator
        })

    return render_template(
        "index.html",
        data=data,
        rata_rata=int(rata_rata)
    )

if __name__ == "__main__":
    app.run(debug=True)
