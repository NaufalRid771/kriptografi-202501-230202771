# Laporan Praktikum Kriptografi
Minggu ke-: 14 
Topik: analisis-serangan  
Nama: Naufal Raa'id  
NIM: 230202771  
Kelas: 5IKRB  

---

## Tujuan Pembelajaran
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.  
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.  
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan
---

## 2. Dasar Teori
Konsep Dasar Analisis Serangan Analisis serangan (attack analysis) dalam keamanan siber didefinisikan sebagai proses sistematis untuk mengidentifikasi, meninjau, dan menafsirkan anomali atau pola lalu lintas jaringan yang mencurigakan guna memahami metode, tujuan, dan dampak dari sebuah ancaman siber. Analisis ini bertujuan untuk menentukan vector serangan (jalur masuknya serangan), kerentanan (vulnerability) yang dieksploitasi, serta potensi kerusakan pada aset informasi. Dalam konteks keamanan data, analisis ini krusial untuk membedakan antara aktivitas jaringan yang sah (legitimate traffic) dan aktivitas berbahaya (malicious traffic).

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
=
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

![Hasil Eksekusi](screenshots/contoh.png)
)

---

## 7. Jawaban Pertanyaan
1. Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?
Jawab: Sistem lama sering kali dirancang pada era di mana daya komputasi belum secepat sekarang dan kesadaran keamanan siber belum setinggi saat ini. Kerentanan utama mereka terhadap serangan tebak sandi ini disebabkan oleh tiga faktor fundamental:

Absennya Mekanisme Rate Limiting: Sistem modern membatasi jumlah percobaan login (misalnya: akun terkunci sementara setelah 3-5 kali salah memasukkan password). Sistem legacy sering kali tidak memiliki fitur ini, mengizinkan penyerang untuk mencoba ribuan kombinasi password per detik tanpa hambatan.

Algoritma Hashing yang Lemah & Tanpa Salt: Sistem lama sering menyimpan password menggunakan algoritma hash yang sudah usang dan cepat (seperti MD5 atau SHA-1) tanpa menambahkan salt (data acak tambahan). Hal ini memungkinkan penyerang menggunakan Rainbow Table (tabel hash yang sudah dihitung sebelumnya) untuk memecahkan password secara instan.

Kebijakan Password yang Lemah: Sistem lama sering mengizinkan penggunaan password yang sangat pendek atau hanya berupa angka, yang sangat mudah ditebak oleh dictionary attack (serangan menggunakan daftar kata-kata umum).

2. Apa bedanya kelemahan algoritma dengan kelemahan implementasi?
Jawab:Perbedaan mendasarnya terletak pada sumber masalahnya: apakah kegagalan terjadi pada desain matematika (teori) atau pada penulisan kode program (praktik).

Kelemahan Algoritma (Teoritis): Terjadi ketika logika matematika atau desain kriptografinya sendiri yang cacat atau sudah tidak memadai untuk standar komputasi saat ini. Meskipun programmer menulis kode dengan sempurna, sistem tetap tidak aman.

Contoh: Algoritma DES (Data Encryption Standard) memiliki ruang kunci (key space) yang terlalu kecil (56-bit), sehingga mudah dijebol dengan metode brute force menggunakan komputer modern, bukan karena kodenya salah, tapi karena algoritmanya sudah "kalah" oleh perkembangan hardware.

Kelemahan Implementasi (Praktis): Terjadi ketika algoritmanya sebenarnya aman dan teruji (seperti AES-256), tetapi cara penerapannya dalam software salah atau ceroboh.

Contoh: Menggunakan algoritma AES yang sangat kuat, tetapi kuncinya disimpan dalam bentuk teks biasa (plain text) di dalam kode program (hardcoded keys), atau penggunaan Random Number Generator (RNG) yang polanya bisa diprediksi. 
3. Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa 
depan?
Jawab:Mengingat ancaman siber terus berkembang (termasuk potensi ancaman komputer kuantum yang mampu memecahkan enkripsi saat ini), organisasi harus menerapkan strategi proaktif:

Penerapan Crypto-Agility: Membangun arsitektur sistem yang fleksibel di mana algoritma kriptografi dapat diganti atau diperbarui dengan mudah tanpa harus merombak seluruh infrastruktur aplikasi. Jika satu standar enkripsi dinyatakan usang, sistem bisa beralih ke standar baru dengan cepat.

Persiapan Post-Quantum Cryptography (PQC): Organisasi harus mulai memetakan data sensitif jangka panjang dan bertransisi ke algoritma yang tahan terhadap serangan komputer kuantum (quantum-resistant algorithms) sesuai standar terbaru (misalnya standar NIST).

Manajemen Siklus Hidup Kunci (Key Lifecycle Management): Keamanan bukan hanya soal algoritma, tapi juga kunci. Organisasi harus memastikan kunci enkripsi diganti (rotated) secara berkala, disimpan dalam modul keamanan perangkat keras (HSM), dan dimusnahkan dengan aman saat tidak lagi digunakan.

---

## 8. Kesimpulan
Berdasarkan analisis yang dilakukan, tingginya tingkat keberhasilan serangan brute force pada sistem legacy disebabkan oleh absennya mekanisme pembatasan akses (rate limiting) dan penggunaan algoritma hashing usang tanpa salt. Selain itu, keamanan sistem terbukti tidak hanya bergantung pada kekuatan matematis algoritma kriptografi, melainkan sangat dipengaruhi oleh ketepatan implementasinya untuk mencegah celah logis. Oleh karena itu, organisasi wajib menerapkan konsep crypto-agility dan pembaruan manajemen kunci secara berkala untuk memitigasi ancaman siber yang terus berkembang.

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
