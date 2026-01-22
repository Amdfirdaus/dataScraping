import requests
from bs4 import BeautifulSoup

url = "https://www.detik.com/jatim/berita/indeks"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("article")[:20]

data = []

# Ambil data
for a in articles:
    title = a.find("h3", class_="media__title")
    date = a.find("span", class_="media__date")

    if title:
        judul = title.get_text(strip=True)
        tanggal = date.get_text(strip=True) if date else "-"

        data.append({
            "judul": judul,
            "tanggal": tanggal,
            "panjang": len(judul)
        })

# Hitung rata-rata panjang judul
rata_rata = sum(d["panjang"] for d in data) / len(data)

print(f"Rata-rata panjang judul: {int(rata_rata)} karakter\n")

# Tampilkan hasil
for i, d in enumerate(data, start=1):
    if d["panjang"] >= rata_rata:
        kode = "H"   # Hijau
    else:
        kode = "M"   # Merah

    print(f"{i}. {d['judul']}")
    print(f"   Tanggal : {d['tanggal']}")
    print(f"   Panjang : {d['panjang']} karakter")
    print(f"   Indikator : {kode}")
    print("-" * 60)
