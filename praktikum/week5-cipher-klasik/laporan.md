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
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

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
