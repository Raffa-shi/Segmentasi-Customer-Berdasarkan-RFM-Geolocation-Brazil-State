# E-Commerce Customer & Geographic Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## Overview
Proyek ini bertujuan untuk menganalisis perilaku pelanggan dan distribusi geografis berdasarkan dataset e-commerce periode 2016–2018.

Analisis difokuskan pada:
- Segmentasi pelanggan menggunakan metode RFM (Recency, Frequency, Monetary)
- Distribusi geografis berdasarkan jumlah order dan total revenue

Hasil analisis divisualisasikan dalam bentuk dashboard interaktif menggunakan Streamlit.

---

## Analysis Approach

### Data Wrangling
- Data Gathering  
- Data Assessing  
- Data Cleaning  

### Exploratory Data Analysis (EDA)
- Analisis distribusi pelanggan  
- Pola transaksi  

### RFM Analysis
- Recency: waktu sejak transaksi terakhir  
- Frequency: jumlah transaksi  
- Monetary: total nilai transaksi  

### Geographical Analysis
- Distribusi order dan revenue per wilayah  
- Analisis konsentrasi pasar  

---

## Key Insights

- Sebagian kecil pelanggan dengan nilai tinggi memberikan kontribusi mayoritas terhadap total revenue.  
- Mayoritas pelanggan memiliki frekuensi transaksi rendah.  
- Distribusi revenue tidak merata dan terkonsentrasi pada wilayah tertentu.  
- Terdapat korelasi antara jumlah order dan total revenue di wilayah utama.  

---

## How to Run the Dashboard

```bash
# 1. Clone repository
git clone <repository-url>
cd submission_raafa

# 2. Buat virtual environment
python -m venv .venv

# 3. Aktifkan virtual environment (Windows)
.venv\Scripts\activate

# (Mac/Linux)
# source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Jalankan Streamlit
streamlit run dashboard/dashboard.py

# Jika terjadi error
# python -m streamlit run dashboard/dashboard.py
