# Optimasi Pemilihan Komponen PC Gaming
**Proyek Makalah Analisis dan Strategi Algoritma — Semester Genap 2025/2026**  
Program Studi S1 Informatika, Universitas Diponegoro

## Judul
Implementasi Algoritma Greedy, Branch and Bound, dan Genetic Algorithm dalam Optimasi Pemilihan Komponen PC Gaming Berdasarkan Budget Mahasiswa

## Deskripsi
Repositori ini berisi implementasi dan eksperimen komputasional dari tiga algoritma optimasi untuk memilih kombinasi komponen PC gaming terbaik dalam batas anggaran tertentu.

## Struktur Repositori
```
├── experiment.py          # Implementasi 3 algoritma + eksperimen utama
├── generate_figures.py    # Pembangkitan grafik dari hasil eksperimen
├── experiment_results.json  # Data hasil eksperimen (output otomatis)
├── README.md
```

## Cara Menjalankan
```bash
# Install dependensi
pip install matplotlib

# Jalankan eksperimen
python experiment.py

# Buat grafik
python generate_figures.py
```

## Lingkungan
- Python 3.11+
- matplotlib 3.x
- Tidak memerlukan dependensi eksternal lainnya

## Algoritma yang Diimplementasikan
1. **Greedy** — Seleksi berbasis rasio performance/price
2. **Branch and Bound** — Pencarian optimal dengan pruning upper bound
3. **Genetic Algorithm** — Optimasi berbasis populasi (pop=60, gen=100, mutasi=0.15)

## Dataset
72 komponen (6 kategori × 12 item): CPU, GPU, RAM, Storage, Motherboard, PSU
Harga representatif pasar Indonesia 2025 dalam satuan Rupiah.
# pc-gaming-optimizer
