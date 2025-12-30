# Laporan Praktikum Kriptografi
Minggu ke-: 12 
Topik: Aplikasi TLS & E-commerce  
Nama: Naufal Raaid  
NIM: 230202771  
Kelas: 5IKRB

---

## 1. Tujuan
Tujuan dari praktikum ini adalah untuk menganalisis penerapan kriptografi pada komunikasi digital, khususnya penggunaan SSL/TLS pada email dan website e-commerce, memahami peran enkripsi dalam melindungi transaksi online, serta mengevaluasi isu etika dan privasi yang muncul dalam penggunaan kriptografi di kehidupan sehari-hari.

---

## 2. Dasar Teori
Transport Layer Security (TLS) merupakan protokol keamanan yang digunakan untuk melindungi komunikasi data di jaringan komputer, terutama pada aplikasi web dan email. TLS menyediakan tiga aspek utama keamanan, yaitu kerahasiaan (confidentiality) melalui enkripsi, integritas data (integrity) melalui message authentication code (MAC), dan autentikasi melalui sertifikat digital. TLS merupakan pengembangan dari Secure Sockets Layer (SSL) yang kini sudah tidak direkomendasikan karena kelemahan keamanannya.

Pada website, TLS diimplementasikan melalui protokol HTTPS (HTTP Secure). HTTPS menggunakan sertifikat digital yang diterbitkan oleh Certificate Authority (CA) untuk memverifikasi identitas server. Sertifikat ini berisi informasi seperti nama domain, masa berlaku, serta algoritma kriptografi yang digunakan (misalnya RSA untuk pertukaran kunci dan AES untuk enkripsi data).

Dalam konteks e-commerce dan email, kriptografi berperan penting dalam melindungi informasi sensitif seperti kredensial login, data pribadi, dan informasi pembayaran. Tanpa enkripsi, data tersebut rentan terhadap penyadapan dan serangan seperti Man-in-the-Middle (MitM).
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `Aplikasi TLS & E-commerce.py` di folder `praktikum/week12-E-commerce/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/hasil.png)

---

## 7. Jawaban Pertanyaan
1. Apa perbedaan utama antara HTTP dan HTTPS? 
Jawab: HTTP tidak menggunakan enkripsi sehingga data dikirim dalam bentuk plaintext, sedangkan HTTPS menggunakan TLS untuk mengenkripsi komunikasi, memastikan kerahasiaan, integritas, dan autentikasi data.

2. Mengapa sertifikat digital menjadi penting dalam komunikasi TLS?
Jawab: Sertifikat digital digunakan untuk memverifikasi identitas server dan mencegah pemalsuan identitas. Sertifikat memastikan bahwa pengguna benar-benar terhubung ke server yang sah.

3. Bagaimana kriptografi mendukung privasi dalam komunikasi digital, tetapi sekaligus menimbulkan tantangan hukum dan etika?
Jawab:Kriptografi melindungi privasi pengguna dengan enkripsi, namun juga menimbulkan dilema etika ketika digunakan untuk menyembunyikan aktivitas ilegal atau saat pemerintah dan perusahaan ingin melakukan pengawasan demi keamanan.
---

## 8. Kesimpulan
TLS dan kriptografi memainkan peran penting dalam menjaga keamanan komunikasi digital, khususnya pada email dan e-commerce. Penggunaan HTTPS dan sertifikat digital mampu melindungi data sensitif pengguna. Namun, penerapan kriptografi juga perlu diimbangi dengan kebijakan etika dan hukum yang jelas.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
```
commit 0eddc2fc29e631453d540d7888e752799ce6eae0 (HEAD -> main, origin/main, origin/HEAD)
Author: Naufal Raaid <nraid834@gmail.com>
Date:   Tue Dec 30 11:40:24 2025 +0700

    week12-aplikasi-tls
```
