import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

file_path = "C:\\Users\\Amir\\Downloads\\Sigi.xlsx"
xls = pd.ExcelFile(file_path)

#PDRB
# Data
data_pdrb = {
    "Lapangan Usaha": ["Sektor Primer", "Sektor Sekunder", "Sektor Tersier"],
    "2023": [2.18, 4.09, 4.67],
    "2024": [1.68, 3.5, 5.68]
}
df_pdrb = pd.DataFrame(data_pdrb)

# Analisis
print("Statistik Deskriptif PDRB 2023-2024:")
print(df_pdrb[['2023', '2024']].describe())

# Pertumbuhan/penurunan
df_pdrb['Perubahan'] = df_pdrb['2024'] - df_pdrb['2023']
df_pdrb['Persentase Perubahan'] = (df_pdrb['Perubahan'] / df_pdrb['2023']) * 100
print("\nPerubahan Pertumbuhan:")
print(df_pdrb[['Lapangan Usaha', '2023', '2024', 'Perubahan', 'Persentase Perubahan']])

#Visualisasi
df_pdrb.plot(x='Lapangan Usaha', y=['2023', '2024'], kind='bar', title='Pertumbuhan PDRB per Sektor')
plt.ylabel('Pertumbuhan (%)')
plt.show()

# Line Chart
plt.figure(figsize=(8, 4))
for sector in df_pdrb['Lapangan Usaha']:
    subset = df_pdrb[df_pdrb['Lapangan Usaha'] == sector]
    plt.plot(['2023', '2024'], subset[['2023', '2024']].values[0], label=sector, marker='o')
plt.title('Trend Pertumbuhan PDRB per Sektor (2023 vs 2024)')
plt.ylabel('Pertumbuhan (%)')
plt.legend()
plt.show()

# Heatmap Perubahan
plt.figure(figsize=(6, 2))
sns.heatmap(df_pdrb[['Perubahan']].T, annot=True, cmap='RdYlGn', center=0, 
            yticklabels=['Perubahan (pp)'], xticklabels=df_pdrb['Lapangan Usaha'])
plt.title('Perubahan Pertumbuhan PDRB 2023-2024')
plt.show()

#Kelompok Umur Petani
# Data
data_umur = {
    "Kelompok Umur Petani (tahun)": ["<15", "15–24", "25–34", "35–44", "45–54", "55–64", "65"],
    "Jumlah": [0, 1460, 7147, 12143, 12878, 8482, 4862]
}
df_umur = pd.DataFrame(data_umur)

# Analisis
print("\nStatistik Deskriptif Pengelola Usaha Tani:")
print(df_umur['Jumlah'].describe())

# Distribusi usia
df_umur['Persentase'] = (df_umur['Jumlah'] / df_umur['Jumlah'].sum()) * 100
print("\nDistribusi Usia Petani:")
print(df_umur[['Kelompok Umur Petani (tahun)', 'Jumlah', 'Persentase']])

df_umur.plot(x='Kelompok Umur Petani (tahun)', y='Jumlah', kind='bar', title='Distribusi Usia Petani')
plt.ylabel('Jumlah Petani')
plt.show()

#Jenis Tanaman
# Data
data_tanaman = {
    "Jenis Tanaman": ["Cengkeh", "Kakao", "Karet", "Kelapa Sawit", "Kelapa", "Kemiri", "Kopi", "Lada", "Pinang", "Teh"],
    "Jumlah Tanaman": [1167, 18492, 37, 66, 5043, 6970, 2374, 14, 6, 1]
}
df_tanaman = pd.DataFrame(data_tanaman)

# Analisis
print("\nStatistik Deskriptif Jenis Tanaman:")
print(df_tanaman['Jumlah Tanaman'].describe())

# Tanaman dominan
df_tanaman = df_tanaman.sort_values('Jumlah Tanaman', ascending=False)
df_tanaman['Persentase'] = (df_tanaman['Jumlah Tanaman'] / df_tanaman['Jumlah Tanaman'].sum()) * 100
print("\nDistribusi Jenis Tanaman:")
print(df_tanaman[['Jenis Tanaman', 'Jumlah Tanaman', 'Persentase']])

#Visualisasi Jenis Tanaman
df_tanaman.plot(x='Jenis Tanaman', y='Jumlah Tanaman', kind='bar', title='Distribusi Jenis Tanaman')
plt.ylabel('Jumlah Tanaman')
plt.xticks(rotation=45)
plt.show()

