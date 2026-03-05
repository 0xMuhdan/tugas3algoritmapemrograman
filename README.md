# Kalkulator Geometri - Web Algo Python

> 🚀 **Live Demo:** [https://tugaskalkulatormuhdan.netlify.app/](https://tugaskalkulatormuhdan.netlify.app/)

Sebuah aplikasi web kalkulator yang dikembangkan untuk menghitung dimensi Silinder dan Kerucut (Keliling, Luas Permukaan, dan Volume) dengan mudah dan presisi.

Aplikasi ini dibangun untuk mengimplementasikan fundamental **Core Basic, Input Output, dan Functions** (awalnya dibangun dengan Python, lalu di-porting ke Vanilla JavaScript untuk kebutuhan hosting Netlify), dibalut dengan antarmuka web modern yang estetik menggunakan pendekatan _Glassmorphism_.

## ✨ Fitur Utama

1. **Perhitungan Silinder**: Menghitung Keliling alas, Luas Permukaan, dan Volume Silinder.
2. **Perhitungan Kerucut**: Menghitung Keliling alas, Luas Permukaan, dan Volume Kerucut.
3. **Validasi Input Pintar**: Mengubah otomatis koma (`,`) menjadi titik (`.`) saat user mengetikkan desimal, serta memblokir huruf/simbol agar tidak terjadi _error_.
4. **Animasi Angka**: Transisi angka perhitungan yang responsif dan sangat mulus (60FPS).
5. **UI Premium Glassmorphism**: Desain antarmuka semi-transparan dengan efek visual animasi bola warna (_gradient orbs_) di latar belakang.
6. **100% Static Web Ready**: Sistem backend Python sudah dipindahkan sepenuhnya ke _Frontend_ JS, sehingga aplikasi dapat berjalan langsung di browser tanpa server khusus (Support GitHub Pages, Netlify, Vercel).

## 📂 Struktur Project

- `/index.html` - Tampilan muka web utama (Kalkulator UI).
- `/static/css/style.css` - Tampilan desain animasi, layouting dan gaya _Glassmorphism_.
- `/static/js/app.js` - "Otak" utama pemrosesan Input, Output, dan Rumus Functions geometri (Javascript).
- `/python_backup/` - Berisi file `geometry_calculator.py` dan `app.py` asli dari proses pembuatan backend awal.

---

**Tugas 3** || **Muhdan Firdaus Salam - 2510614067**
