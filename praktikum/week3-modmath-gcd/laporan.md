# Laporan Praktikum Kriptografi
Minggu ke-: 3 
Topik: [judul praktikum]  
Nama: Naufal Raa'id
NIM: 230202771  
Kelas:5IKRB   

---

## 1. Tujuan
1.Menyelesaikan operasi aritmetika modular.
2.Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3.Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Aritmetika modular merupakan sistem aritmetika yang menggunakan operasi berdasarkan sisa hasil pembagian. Dalam sistem ini, dua bilangan dianggap kongruen jika memiliki sisa pembagian yang sama terhadap suatu modulus. Operasi modular banyak digunakan dalam kriptografi, terutama pada algoritma seperti RSA dan Diffie-Hellman.

Algoritma Euclidean digunakan untuk mencari pembagi bersama terbesar (GCD) antara dua bilangan. Versi Extended Euclidean Algorithm memungkinkan kita menemukan invers modular, yaitu bilangan 
𝑥x yang memenuhi 𝑎×x≡
(mod𝑛)a×x≡1(modn).

Logaritma diskrit merupakan kebalikan dari eksponensiasi modular, yaitu mencari 
𝑥x pada persamaan 𝑎𝑥≡𝑏(mod𝑛)ax≡b(modn). Masalah ini sangat sulit diselesaikan untuk modulus besar, dan karenanya menjadi dasar keamanan banyak sistem kriptografi modern.
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
)

---

## 7. Jawaban Pertanyaan
Perannya antara lain:

-Menyediakan ruang bilangan terbatas (mod n) tempat operasi matematika dilakukan, sehingga hasil operasi selalu “terbungkus” di dalam kisaran tertentu.
-Memungkinkan fungsi satu arah (one-way function), yaitu operasi yang mudah dilakukan tetapi sulit dibalik (misalnya, mengalikan dua bilangan prima besar mudah, tetapi memfaktorkan hasilnya sangat sulit).
Digunakan untuk operasi enkripsi, dekripsi, tanda tangan digital, dan pertukaran kunci melalui operasi seperti perpangkatan modular:
𝐶 = 𝑀<sup>𝑒</sup> mod 𝑛 di mana 𝑀M adalah pesan, 𝑒e eksponen publik, dan 𝑛n modulus.

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
