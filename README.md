# IP Address Lookup Tool

## Deskripsi
Program ini memungkinkan pengguna untuk mencari informasi terkait alamat IP menggunakan layanan API [ipinfo.io](https://ipinfo.io/). Pengguna dapat memasukkan alamat IP tertentu atau membiarkan kolom kosong untuk mencari informasi tentang IP publik perangkat yang sedang digunakan.

### Fitur:
- Mengambil informasi alamat IP seperti:
  - Alamat IP
  - Hostname
  - Kota
  - Wilayah
  - Negara
  - Lokasi geografis (Latitude, Longitude)
  - Organisasi penyedia alamat IP
- Mendukung pencarian informasi untuk IP tertentu atau IP publik secara otomatis.
  
## Instalasi

1. Pastikan Python sudah terinstal di sistem Anda.
2. Install pustaka `requests` untuk melakukan HTTP request ke API:
    ```bash
    pip install requests
    ```

## Penggunaan

1. **Jalankan Program**: Setelah menginstal `requests`, jalankan program menggunakan Python:
    ```bash
    python ip_lookup.py
    ```

2. **Masukkan Alamat IP**: Program akan meminta Anda untuk memasukkan alamat IP yang ingin dicari informasinya.
    - Jika Anda ingin mencari informasi tentang alamat IP perangkat Anda, cukup tekan `Enter` tanpa memasukkan alamat IP.
    - Jika Anda ingin mencari informasi tentang alamat IP tertentu, masukkan alamat IP tersebut (misalnya: `8.8.8.8`).

3. **Melihat Hasil**: Program akan menampilkan informasi berikut:
    - **IP Address**: Alamat IP yang dicari.
    - **Hostname**: Nama host terkait (jika tersedia).
    - **City**: Kota tempat IP berada (jika tersedia).
    - **Region**: Wilayah tempat IP berada (jika tersedia).
    - **Country**: Negara tempat IP berada.
    - **Location**: Lokasi geografis dalam bentuk koordinat (Latitude, Longitude).
    - **Org**: Organisasi penyedia layanan untuk IP.

### Contoh Penggunaan:
```bash
Masukkan IP address untuk mencari informasi (atau tekan Enter untuk menggunakan IP publik):
8.8.8.8
```

### Output:
```bash
IP Address: 8.8.8.8
Hostname: google-public-dns-a.google.com
City: Mountain View
Region: California
Country: US
Location: 37.4056,-122.0775
Org: AS15169 Google LLC
```

## Catatan
- Program ini menggunakan API **ipinfo.io** yang memiliki batasan jumlah permintaan gratis per hari. Pastikan untuk tidak melebihi batas permintaan yang ditentukan oleh layanan.

