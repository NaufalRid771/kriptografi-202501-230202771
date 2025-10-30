# Laporan Praktikum Kriptografi
Minggu ke-: 5
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)
Nama: [Naufal Raaid]  
NIM: 230202771  
Kelas: 5IKRB   


---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menerapkan algoritma **Caesar Cipher** untuk enkripsi dan dekripsi teks.  
2. Menerapkan algoritma **Vigenère Cipher** dengan variasi kunci.  
3. Mengimplementasikan algoritma transposisi sederhana.  
4. Menjelaskan kelemahan algoritma kriptografi klasik.  

---

## 2. Dasar Teori
<think>
Pertama, pengguna meminta "buatkan secara detail tapi ringkas" – ini berarti "buatkan secara detail tapi ringkas" dalam bahasa Indonesia. Mereka ingin versi yang lebih detail namun tetap ringkas dari penjelasan sebelumnya tentang cipher klasik, modular aritmetika, dan cipher Caesar, Vigenère, Transposisi.

</think>### Definisi Cipher Klasik
Cipher klasik adalah metode enkripsi manual pra-komputer yang mengubah plaintext (pesan asli) menjadi ciphertext (pesan terenkripsi) menggunakan substitusi (penggantian huruf) atau transposisi (pengaturan ulang urutan). Mereka bergantung pada kerahasiaan algoritma dan kunci, bukan komputasi. Contoh: Caesar (substitusi sederhana), Vigenère (substitusi polialfabetik), Transposisi (pengaturan ulang). Keamanan rendah terhadap analisis modern seperti frekuensi huruf atau brute-force, tapi penting untuk memahami dasar kriptografi.

### Konsep Modular Aritmetika
Modular aritmetika adalah aritmetika sisa pembagian, di mana operasi dilakukan modulo n (sisa saat dibagi n). Notasi: a ≡ b mod n jika a - b kelipatan n. Operasi:
- Penjumlahan: (a + b) mod n
- Pengurangan: (a - b) mod n
- Perkalian: (a × b) mod n
Dalam kriptografi, sering digunakan untuk alfabet 26 huruf (A=0, B=1, ..., Z=25), memungkinkan shift siklik (mis., 25 + 3 = 28 mod 26 = 2, yaitu C). Ini mencegah nilai melebihi batas dan memfasilitasi enkripsi/dekripsi reversibel.

### Dasar Teori Caesar Cipher
**Prinsip**: Substitusi monoalfabetik dengan shift tetap kunci (biasanya 3) pada alfabet 26 huruf. Setiap huruf plaintext digeser maju kunci posisi; dekripsi geser mundur.
**Rumus Enkripsi**: C_i = (P_i + K) mod 26, di mana P_i adalah posisi plaintext (A=0), K adalah kunci.
**Rumus Dekripsi**: P_i = (C_i - K) mod 26.
**Contoh**: Plaintext "ABC" (0,1,2), K=3 → Ciphertext "DEF" (3,4,5). Dekripsi: "DEF" -3 → "ABC".
**Kelemahan**: Hanya 25 kunci; rentan analisis frekuensi (huruf umum seperti E sering muncul).

### Dasar Teori Vigenère Cipher
**Prinsip**: Substitusi polialfabetik menggunakan kata kunci berulang. Kata kunci diulang hingga panjang plaintext; setiap huruf plaintext digeser berdasarkan huruf kunci (A=0 shift).
**Rumus Enkripsi**: C_i = (P_i + K_i) mod 26, di mana K_i adalah posisi huruf kunci ke-i.
**Rumus Dekripsi**: P_i = (C_i - K_i) mod 26.
**Contoh**: Plaintext "ATTACK" (0,19,19,0,2,10), Kunci "LEMON" (11,4,12,14,13) diulang: L E M O N L (11,4,12,14,13,11) → Ciphertext "LXFOPV" (11,23,5,14,15,21).
**Kelemahan**: Rentan analisis Kasiski (deteksi panjang kunci via pola ulang) atau metode statistik; lebih aman dari Caesar tapi pecah dengan komputer.

### Dasar Teori Transposition Cipher
**Prinsip**: Mengatur ulang urutan huruf plaintext tanpa mengubahnya, menggunakan grid atau pola berdasarkan kunci. Contoh umum: Columnar Transposition – tulis plaintext dalam kolom sesuai kunci, lalu baca kolom dalam urutan kunci.
**Langkah Enkripsi**:
1. Tulis plaintext dalam grid dengan kolom sebanyak panjang kunci.
2. Urutkan kolom berdasarkan alfabet kunci.
3. Baca ciphertext baris per baris dari kolom terurut.
**Langkah Dekripsi**: Balik proses – tulis ciphertext dalam kolom terurut, lalu baca baris per baris.
**Contoh**: Plaintext "HELLO WORLD" (11 huruf), Kunci "ABC" (3 kolom: A=1, B=2, C=3). Grid:
- Kolom A: H E L
- Kolom B: L O W
- Kolom C: O R D
Urut kolom: A, B, C → Baca: H E L L O W O R D → Ciphertext "HELLOWORLD" (tanpa spasi).
**Kelemahan**: Rentan jika pola grid terdeteksi; frekuensi huruf tetap sama, sehingga analisis statistik bisa membantu. Lebih sulit dari substitusi sederhana tapi kurang aman dari cipher modern.  

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

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?
jawab:Kelemahan Utama Caesar Cipher dan Vigenère Cipher
Caesar Cipher:

Kunci terbatas: Hanya 25 kemungkinan shift (kunci 1-25), sehingga mudah dipecahkan dengan brute-force (mencoba semua kunci).
Rentan analisis frekuensi: Pola frekuensi huruf tetap sama seperti plaintext, karena substitusi monoalfabetik (setiap huruf selalu diganti dengan huruf yang sama).
Tidak aman untuk pesan panjang: Pola ulang mudah terdeteksi, dan tidak ada variasi per huruf.
Vigenère Cipher:

Rentan analisis Kasiski: Jika panjang kunci diketahui (melalui pola ulang dalam ciphertext), bisa dipecah menjadi beberapa Caesar cipher sederhana.
Analisis frekuensi masih efektif: Meski polialfabetik, jika kunci pendek, frekuensi huruf dalam blok yang sama bisa dianalisis.
Kunci harus diingat dan dibagikan: Sulit untuk komunikasi aman tanpa kesalahan, dan rentan jika kunci bocor atau salah tebak panjangnya.
Kedua cipher ini lebih aman dari yang tidak terenkripsi, tapi mudah dipecahkan dengan metode modern atau komputer.

2. Mengapa cipher klasik mudah diserang dengan analisis frekuensi?
jawab:Cipher klasik (seperti Caesar atau substitusi sederhana) mudah diserang analisis frekuensi karena distribusi huruf dalam bahasa alami tidak acak. Huruf seperti E, T, A sering muncul (frekuensi tinggi), sedangkan Q, Z jarang. Dalam ciphertext:

Jika cipher hanya mengganti huruf (substitusi monoalfabetik), frekuensi huruf tetap sama, sehingga penyerang bisa memetakan huruf ciphertext ke plaintext berdasarkan frekuensi umum.
Contoh: Huruf paling sering di ciphertext kemungkinan adalah E. Ini tidak berlaku untuk cipher polialfabetik seperti Vigenère (jika kunci panjang), tapi masih rentan jika kunci pendek.
Analisis ini dikembangkan oleh ahli seperti Al-Kindi pada abad ke-9, dan efektif karena bahasa manusia memiliki pola statistik yang dapat diprediksi tanpa kunci.

3. Bandingkan kelebihan dan kelemahan cipher substitusi vs transposisi.
jawab:Cipher Substitusi (mengganti huruf, e.g., Caesar, Vigenère):

Kelebihan: Lebih aman dari analisis frekuensi sederhana karena mengubah identitas huruf (frekuensi berubah jika polialfabetik). Vigenère lebih kompleks dengan kunci berulang, menambah variasi.
Kelemahan: Rentan brute-force jika kunci kecil (Caesar), atau analisis Kasiski (Vigenère). Sulit untuk pesan panjang tanpa kesalahan manusia, dan frekuensi masih bisa dianalisis jika pola terdeteksi.
Cipher Transposisi (mengatur ulang urutan, e.g., Columnar):

Kelebihan: Frekuensi huruf tetap sama seperti plaintext, sehingga analisis frekuensi dasar tidak langsung membantu; fokus pada urutan. Lebih sederhana untuk implementasi manual dan tidak mengubah huruf.
Kelemahan: Rentan jika pola grid atau kunci terdeteksi (mis., melalui uji coba urutan). Lebih lemah dari substitusi karena tidak mengubah identitas huruf, sehingga kombinasi dengan substitusi (seperti dalam cipher modern) lebih disarankan. Mudah dipecahkan dengan anagram atau analisis statistik urutan. 

## 8. Kesimpulan
Kesimpulan
Cipher klasik, seperti Caesar, Vigenère, dan Transposisi, merupakan fondasi kriptografi manual yang bergantung pada substitusi atau pengaturan ulang huruf, dengan modular aritmetika sebagai basis matematika untuk operasi siklik pada alfabet. Caesar sederhana namun rentan brute-force dan analisis frekuensi karena shift tetap; Vigenère lebih kompleks dengan kunci berulang, tapi masih pecah melalui analisis Kasiski jika panjang kunci terdeteksi. Transposisi menyembunyikan urutan tanpa mengubah huruf, lebih tahan frekuensi dasar tapi lemah jika pola grid diketahui.

Secara umum, cipher klasik mudah diserang analisis frekuensi karena pola statistik bahasa manusia (frekuensi huruf seperti E/T) tetap terlihat, terutama pada substitusi monoalfabetik. Substitusi lebih kuat melawan frekuensi tapi rentan brute-force, sedangkan transposisi lebih sederhana namun kurang aman tanpa kombinasi. Meski historis penting, mereka tidak cukup untuk keamanan modern, yang memerlukan algoritma komputasional seperti AES. Pemahaman ini membantu dalam evolusi kriptografi saat ini.

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
