# Laporan Praktikum Kriptografi
Minggu ke-: 6 
Topik: [judul praktikum]  
Nama: [Naufal Raaid]  
NIM: [230202771]  
Kelas: [5IKRB]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Mengimplementasikan algoritma **DES** untuk blok data sederhana.  
2. Menerapkan algoritma **AES** dengan panjang kunci 128 bit.  
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma **RSA**.  

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

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
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
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
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil aes](screenshots/aes.png)
![Hasil des](screenshots/des.png)
![Hasil rsa ](screenshots/rsa.png)
)

---

## 7. Jawaban Pertanyaan
1. Apa perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan?
Jawab:Inti perbedaan:
DES & AES menggunakan satu kunci rahasia bersama (simetris).
RSA menggunakan dua kunci berbeda (asimetris):
Kunci publik untuk enkripsi.
Kunci privat untuk dekripsi.
AES jauh lebih aman dibanding DES karena memiliki panjang kunci yang lebih besar dan struktur matematis yang lebih kompleks.  
2. Mengapa AES lebih banyak digunakan dibanding DES di era modern?  
jawab:Beberapa alasan utama:

Keamanan:
DES hanya memiliki 56 bit key, yang bisa dipecahkan dalam hitungan jam atau bahkan menit dengan hardware modern.
AES memiliki minimal 128 bit key, yang sangat sulit dipecahkan bahkan dengan superkomputer.
Efisiensi:
AES dioptimalkan untuk perangkat keras dan lunak modern, sehingga cepat dan ringan.
DES menggunakan banyak operasi bit-level yang kurang efisien di prosesor modern.
Standarisasi:
AES ditetapkan oleh NIST (National Institute of Standards and Technology) sebagai standar enkripsi sejak tahun 2001, menggantikan DES.
3. Mengapa RSA dikategorikan sebagai algoritma asimetris, dan bagaimana proses pembangkitan kuncinya? 
Jawab:Karena RSA menggunakan dua kunci berbeda:
Kunci publik (Public Key) → untuk mengenkripsi.
Kunci privat (Private Key) → untuk mendekripsi.
Hanya pemilik kunci privat yang bisa membuka pesan yang dienkripsi dengan kunci publiknya.

---

## 8. Kesimpulan
Di era modern, AES digunakan untuk mengenkripsi data, sedangkan RSA digunakan untuk mengamankan distribusi kunci AES.
Kombinasi keduanya membentuk dasar keamanan pada sistem seperti HTTPS, VPN, dan aplikasi pesan terenkripsi.
---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
