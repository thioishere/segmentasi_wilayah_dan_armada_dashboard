
# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Judul Dashboard
# st.set_page_config(page_title="Dashboard Segmentasi & Armada", layout="wide")
# st.title("🚛 Dashboard Segmentasi Wilayah & Jumlah Armada Ideal")

# # Load data
# @st.cache_data
# def load_data():
#     return pd.read_excel("gabungan_segmentasi_armada.xlsx")

# df = load_data()

# # Sidebar filter
# st.sidebar.header("🔍 Filter")
# clusters = sorted(df["cluster"].unique())
# selected_cluster = st.sidebar.multiselect("Pilih Cluster", clusters, default=clusters)

# filtered_df = df[df["cluster"].isin(selected_cluster)]

# # Ringkasan statistik
# st.subheader("📊 Ringkasan Cluster")
# col1, col2, col3 = st.columns(3)
# col1.metric("Jumlah Wilayah", len(filtered_df))
# col2.metric("Total Armada Ideal", int(filtered_df[["arm roll ideal unit", "truk sampah ideal", "dump truck ideal"]].sum().sum()))
# col3.metric("Rata-rata % Sampah Terangkut", f"{filtered_df['persentase_sampah_ditangani'].mean():.2f}%")

# # Tabel data
# st.subheader("📋 Data Wilayah & Armada")
# st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

# # Visualisasi 1: Bar chart jumlah armada per kota
# st.subheader("📉 Jumlah Armada Ideal per Kabupaten/Kota")
# armada_df = filtered_df[["nama_kabupaten_kota", "arm roll ideal unit", "truk sampah ideal", "dump truck ideal"]]
# armada_df = armada_df.set_index("nama_kabupaten_kota")
# st.bar_chart(armada_df)

# # Visualisasi 2: Pie Chart Persentase Sampah Terangkut (Agregat)
# st.subheader("🧮 Distribusi Persentase Sampah Terangkut")
# fig = px.histogram(filtered_df, x="persentase_sampah_ditangani", nbins=20, title="Distribusi % Sampah Terangkut", labels={"persentase_sampah_ditangani": "% Terangkut"})
# st.plotly_chart(fig, use_container_width=True)



# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Set page configuration
# st.set_page_config(page_title="Dashboard Penanganan Sampah", layout="wide")
# st.title("🚛 Dashboard Segmentasi Wilayah & Jumlah Armada Ideal")

# # Load data
# @st.cache_data
# def load_data():
#     return pd.read_excel("gabungan_segmentasi_armada.xlsx")

# df = load_data()

# # Sidebar Navigation
# st.sidebar.title("📌 Navigasi")
# menu = st.sidebar.radio("Pilih Halaman:", ["Clustering KMeans", "Jumlah Armada Ideal"])

# if menu == "Clustering KMeans":
#     st.header("🔍 Hasil Clustering Wilayah dengan KMeans")

#     # Sidebar filter untuk cluster
#     clusters = sorted(df["cluster"].unique())
#     selected_clusters = st.sidebar.multiselect("Pilih Cluster", clusters, default=clusters)
#     cluster_df = df[df["cluster"].isin(selected_clusters)]

#     # Metrik
#     st.subheader("📊 Ringkasan Cluster")
#     col1, col2 = st.columns(2)
#     col1.metric("Jumlah Wilayah (Terfilter)", len(cluster_df))
#     col2.metric("Jumlah Cluster yang Dipilih", len(selected_clusters))

#     # Distribusi jumlah wilayah per cluster
#     st.subheader("📈 Distribusi Jumlah Wilayah per Cluster")
#     cluster_counts = df["cluster"].value_counts().sort_index()
#     fig = px.bar(x=cluster_counts.index, y=cluster_counts.values, labels={"x": "Cluster", "y": "Jumlah Wilayah"})
#     st.plotly_chart(fig, use_container_width=True)

#     # Karakteristik Cluster
#     st.subheader("🧠 Karakteristik Rata-rata Tiap Cluster")

    
#     fitur = [
#         "kepadatan_penduduk", "pdrb_adhk_per_kapita", "persentase_pelayanan",
#         "persentase_sampah_ditangani", "luas_wilayah"
#     ]
    
#     st.write("Kolom-kolom yang ada di df:", df.columns.tolist())
    
#     karakter_df = df.groupby("cluster")[fitur].mean().round(2).reset_index()

    
#     st.dataframe(karakter_df, use_container_width=True)

#     st.markdown("""
#     ### 📝 Interpretasi Cluster

#     - **Cluster 0**: Kepadatan penduduk tinggi, PDRB sedang, persentase pelayanan sedang,
#       persentase sampah ditangani tertinggi, luas wilayah kecil

#     - **Cluster 1**: Kepadatan penduduk rendah, PDRB kecil, persentase pelayanan sedang,
#       persentase sampah ditangani paling rendah, luas wilayah besar

#     - **Cluster 2**: Kepadatan penduduk tinggi, PDRB tinggi, persentase pelayanan sedang,
#       persentase sampah ditangani sedang, luas wilayah sedang

#     #### 💡 Rekomendasi Solusi:
#     - Cluster 0: Fokus pada peningkatan efisiensi armada di wilayah padat dan kecil
#     - Cluster 1: Perluas akses layanan di wilayah luas dan berpenduduk jarang
#     - Cluster 2: Perkuat integrasi manajemen karena dukungan ekonomi tinggi
#     """)

# elif menu == "Jumlah Armada Ideal":
#     st.header("🚛 Jumlah Armada Ideal per Wilayah")

#     # Sidebar filter
#     kabkot_list = sorted(df["nama_kabupaten_kota"].unique())
#     selected_kabkot = st.sidebar.multiselect("Pilih Kabupaten/Kota", kabkot_list, default=kabkot_list)
#     selected_clusters = st.sidebar.multiselect("Pilih Cluster", sorted(df["cluster"].unique()), default=clusters)

#     filtered_armada = df[
#         df["nama_kabupaten_kota"].isin(selected_kabkot) &
#         df["cluster"].isin(selected_clusters)
#     ]

#     # Metrik
#     st.subheader("📦 Total Armada Ideal Berdasarkan Filter")
#     total_armroll = int(filtered_armada["arm roll ideal unit"].sum())
#     total_truck = int(filtered_armada["truk sampah ideal"].sum())
#     total_dump = int(filtered_armada["dump truck ideal"].sum())

#     col1, col2, col3 = st.columns(3)
#     col1.metric("Arm Roll Ideal", total_armroll)
#     col2.metric("Truk Sampah Ideal", total_truck)
#     col3.metric("Dump Truck Ideal", total_dump)

#     # Tabel data
#     st.subheader("📋 Tabel Wilayah & Detail Armada Ideal")
#     st.dataframe(filtered_armada[[
#         "nama_kabupaten_kota", "cluster", "arm roll ideal unit",
#         "truk sampah ideal", "dump truck ideal"
#     ]].reset_index(drop=True), use_container_width=True)

#     # Visualisasi Bar Chart
#     st.subheader("📉 Visualisasi Armada per Wilayah")
#     visual_df = filtered_armada[[
#         "nama_kabupaten_kota", "arm roll ideal unit",
#         "truk sampah ideal", "dump truck ideal"
#     ]]
#     visual_df = visual_df.set_index("nama_kabupaten_kota")
#     st.bar_chart(visual_df)


# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Page config
# st.set_page_config(page_title="Dashboard Sampah", layout="wide")
# st.title("♻️ Dashboard Segmentasi Wilayah & Armada Ideal")

# # Load data
# @st.cache_data
# def load_data():
#     df = pd.read_excel("gabungan_segmentasi_armada.xlsx")
#     df = df[df['cluster'].isin([0, 1, 2])]  # hanya cluster 0, 1, 2
#     return df

# df = load_data()

# # Sidebar
# st.sidebar.title("Navigasi")
# menu = st.sidebar.radio("Pilih Halaman:", ["Segmentasi Wilayah", "Jumlah Armada Ideal"])

# # ===============================
# # 🟢 MENU 1: Segmentasi Wilayah
# # ===============================
# if menu == "Segmentasi Wilayah":
#     st.header("📊 Segmentasi Wilayah Berdasarkan K-Means Clustering")

#     # Tampilkan jumlah wilayah per cluster
#     cluster_counts = df["cluster"].value_counts().sort_index()
#     fig1 = px.bar(
#         x=cluster_counts.index,
#         y=cluster_counts.values,
#         labels={"x": "Cluster", "y": "Jumlah Wilayah"},
#         title="Distribusi Jumlah Wilayah per Cluster"
#     )
#     st.plotly_chart(fig1, use_container_width=True)

#     # Rata-rata karakteristik tiap cluster
#     fitur = ['kepadatan_penduduk', 'luas_wilayah']
#     mean_char = df.groupby("cluster")[fitur].mean().round(2).reset_index()
#     st.subheader("📋 Karakteristik Rata-rata per Cluster")
#     st.dataframe(mean_char, use_container_width=True)

#     # Tampilkan deskripsi dan rekomendasi
#     st.subheader("📌 Rekomendasi Penanganan Sampah per Cluster")
#     solusi_clusters = {
#         0: """🔷 Cluster 0:
# - Wilayah padat penduduk, luas kecil
# - Ekonomi sedang
# - Pelayanan & penanganan sedang
# ✅ Fokus: rute optimal, edukasi warga, tambah TPS""",
#         1: """🔷 Cluster 1:
# - Wilayah luas, penduduk jarang
# - Ekonomi rendah
# - Penanganan paling rendah
# ✅ Fokus: akses ke pelosok, insentif, intervensi dana""",
#         2: """🔷 Cluster 2:
# - Padat penduduk, ekonomi tinggi
# - Pelayanan & penanganan sedang
# ✅ Fokus: teknologi & integrasi layanan"""
#     }

#     for clust_id in sorted(solusi_clusters):
#         st.markdown(solusi_clusters[clust_id])
#         st.markdown("---")

# # ===============================
# # 🔵 MENU 2: Armada Ideal
# # ===============================
# elif menu == "Jumlah Armada Ideal":
#     st.header("🚛 Analisis Jumlah Armada Ideal")

#     selected_clusters = st.sidebar.multiselect(
#         "Pilih Cluster", sorted(df["cluster"].unique()), default=[0, 1, 2]
#     )

#     filtered_df = df[df["cluster"].isin(selected_clusters)]

#     st.subheader("📊 Tabel Data Wilayah")
#     st.dataframe(filtered_df[[
#         'nama_kabupaten_kota', 'cluster',
#         'arm roll ideal unit', 'truk sampah ideal', 'dump truck ideal'
#     ]].reset_index(drop=True), use_container_width=True)

#     st.subheader("📈 Visualisasi Rata-rata Armada Ideal per Cluster")
#     avg_df = filtered_df.groupby("cluster")[[
#         'arm roll ideal unit', 'truk sampah ideal', 'dump truck ideal'
#     ]].mean().round(2).reset_index().melt(id_vars='cluster', var_name='Jenis Armada', value_name='Rata-rata Unit')

#     fig2 = px.bar(
#         avg_df,
#         x="Jenis Armada",
#         y="Rata-rata Unit",
#         color=avg_df['cluster'].astype(str),
#         barmode="group",
#         labels={"cluster": "Cluster"},
#         title="Rata-rata Jumlah Armada Ideal per Jenis dan Cluster"
#     )
#     st.plotly_chart(fig2, use_container_width=True)

#     st.subheader("📤 Unduh Data")
#     st.download_button(
#         label="⬇️ Download Data Gabungan (Excel)",
#         data=filtered_df.to_excel(index=False, engine='openpyxl'),
#         file_name="gabungan_segmentasi_armada_filtered.xlsx",
#         mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#     )




############ YANG BARU LAGI WKWKWK ##########

import streamlit as st
import pandas as pd
import plotly.express as px

# --- Load Data ---
df_cluster = pd.read_excel("hasil_kmeans.xlsx")

# Menyaring hanya kolom yang dibutuhkan
kolom_ditampilkan = [
    'nama_kabupaten_kota',
    'persentase_pelayanan',
    'kepadatan_penduduk',
    'pdrb_adhk_per_kapita',
    'persentase_sampah_ditangani',
    'luas_wilayah',
    'cluster'
]

df_cluster = df_cluster[kolom_ditampilkan]
# Ubah nama kolom ke Title Case
df_cluster.columns = df_cluster.columns.str.replace('_', ' ').str.title()

df_armada = pd.read_excel("hasil_armada_ideal.xlsx")
df_gabungan = pd.read_excel("gabungan_segmentasi_armada.xlsx")
df_penggabungan = pd.read_excel("penggabungan.xlsx")

# Bulatkan jumlah armada ideal
if 'Jumlah Armada Ideal' in df_armada.columns:
    df_armada['Jumlah Armada Ideal'] = df_armada['Jumlah Armada Ideal'].round(0).astype(int)

# --- Page Setup ---
st.set_page_config(page_title="Dashboard Penanganan Sampah", layout="wide")
st.title("🗑️ Dashboard Penanganan Sampah Berdasarkan Segmentasi Wilayah & Armada Ideal")

# --- Sidebar ---
st.sidebar.header("Pilih Menu")
menu = st.sidebar.radio("Navigasi", ["Segmentasi Wilayah", "Jumlah Armada Ideal"])

# --- Segmentasi Wilayah ---
if menu == "Segmentasi Wilayah":
    st.subheader("📊 Segmentasi Wilayah berdasarkan Clustering")

    cluster_0 = df_cluster[df_cluster['Cluster'] == 0]
    cluster_1 = df_cluster[df_cluster['Cluster'] == 1]
    cluster_2 = df_cluster[df_cluster['Cluster'] == 2]


    jumlah_cluster_0 = cluster_0.shape[0]
    jumlah_cluster_1 = cluster_1.shape[0]
    jumlah_cluster_2 = cluster_2.shape[0]

    tab0, tab1, tab2 = st.tabs(["Cluster 0", "Cluster 1", "Cluster 2"])

    with tab0:
        st.markdown(f"""
        ### Cluster 0
                    
        📄 **Karakteristik**: 
        - Kepadatan Penduduk = Tinggi
        - Produk Domestik Regional Bruto (PDRB) = Sedang
        - Persentase Pelayanan = Sedang
        - Persentase Sampah Ditangani = Sedang (tertinggi diantara semua cluster)
        - Luas Wilayah = Kecil
                            
        📍 **Jumlah Wilayah Cluster 0**: {jumlah_cluster_0} Wilayah

        ✅ **Rekomendasi Penanganan Cluster 0**:
        - Wilayah padat penduduk dengan luas kecil → Optimalkan rute pengangkutan dan frekuensi layanan.
        - Ekonomi sedang → Perkuat peran swasta/UMKM dalam pengelolaan sampah sehingga penanganan sampah meningkat
        - Pelayanan dan penanganan sampah sedang → Menambah jumlah TPS eksisting di lokasi strategis serta pemberian edukasi kepada warga agar lebih aktif memilah sampah.
        """)         
                
        # Tambahkan jarak dan judul sebelum tabel
        st.markdown("---")  # garis pemisah horizontal, bisa juga pakai <br><br> untuk spacing
        st.markdown("#### 📊 Daftar Wilayah pada Cluster 0")  # Judul sebelum tabel

        # Tampilkan tabelnya
        st.dataframe(cluster_0)

               

    with tab1:
        (f"""
        ### Cluster 1
                    
        📄 **Karakteristik**: 
        - Kepadatan Penduduk = rendah
        - Produk Domestik Regional Bruto (PDRB) = Kecil
        - Persentase Pelayanan = Sedang
        - Persentase Sampah Ditangani = Sedang (terkecil diantara semua cluster)
        - Luas Wilayah = Tinggi
                            
        📍 **Jumlah Wilayah Cluster 1**: {jumlah_cluster_1} Wilayah

        ✅ **Rekomendasi Penanganan Cluster 1**:
        - Wilayah luas dan berpenduduk jarang → Fokus pada penyediaan akses layanan ke pelosok dengan sistem zona.
        - Ekonomi rendah → Melakukan intervensi dana pemerintah untuk infrastruktur dasar pengelolaan sampah.
        - Pelayanan dan penanganan sampah sedang → Menambah jumlah TPS eksisting di lokasi strategis serta pemberian edukasi kepada masyarakat melalui edukasi dan program insentif.
        """)         
                
        # Tambahkan jarak dan judul sebelum tabel
        st.markdown("---")  # garis pemisah horizontal, bisa juga pakai <br><br> untuk spacing
        st.markdown("#### 📊 Daftar Wilayah pada Cluster 1")  # Judul sebelum tabel

        # # Tampilkan tabelnya
        st.dataframe(cluster_1)

    with tab2:
        (f"""
        ### Cluster 2
                    
        📄 **Karakteristik**: 
        - Kepadatan Penduduk = Tinggi
        - Produk Domestik Regional Bruto (PDRB) = tinggi
        - Persentase Pelayanan = Sedang
        - Persentase Sampah Ditangani = Sedang
        - Luas Wilayah = Sedang
                            
        📍 **Jumlah Wilayah Cluster 2**: {jumlah_cluster_2} Wilayah

        ✅ **Rekomendasi Penanganan Cluster 2**:
        - Wilayah padat penduduk dan luas wilayah sedang → Optimalkan rute pengangkutan sampah dengan teknologi (misalnya, aplikasi tracking armada atau GPS).
        - Ekonomi tinggi → Implementasi teknologi pintar dalam pengangkutan dan pemantauan sampah.
        - Pelayanan dan penanganan sampah sedang → Membuat jadwal angkut berbasis zona yang efisien dan transparan serta digitalisasi layanan kebersihan seperti aplikasi pelaporan wargang → Menambah jumlah TPS eksisting di lokasi strategis serta pemberian edukasi kepada warga agar lebih aktif memilah sampah.
        """)         
                
        # Tambahkan jarak dan judul sebelum tabel
        st.markdown("---")  # garis pemisah horizontal, bisa juga pakai <br><br> untuk spacing
        st.markdown("#### 📊 Daftar Wilayah pada Cluster 2")  # Judul sebelum tabel

        # Tampilkan tabelnya
        st.dataframe(cluster_2)

if menu == "Jumlah Armada Ideal":
    # Filter cluster ditampilkan hanya di halaman ini
    st.sidebar.header("Filter Cluster")
    selected_cluster = st.sidebar.selectbox("Pilih Cluster", sorted(df_penggabungan["cluster"].unique()))

       

    # Filter berdasarkan cluster
    df_filtered = df_penggabungan[df_penggabungan["cluster"] == selected_cluster]

    # Pilih kolom yang ditampilkan
    tampilkan_kolom = [
        "nama_kabupaten_kota", "cluster",
        "arm roll ideal unit", "truk sampah ideal", "dump truck ideal"
    ]
    df_clustered = df_filtered[tampilkan_kolom].copy()

    # Format kolom tabel
    df_clustered.columns = [
        f"{' '.join(col.replace('_', ' ').split()).title()}"
        for col in df_clustered.columns
    ]

    # --- Judul dan Tabel ---
    st.markdown(f"### 🚛 Jumlah Armada Ideal untuk Wilayah Cluster {selected_cluster}")
    st.markdown("""
    Perhitungan jumlah armada ideal dilakukan berdasarkan volume timbulan sampah dan distribusi standar pengangkutan.
    Berikut adalah kebutuhan armada ideal pada kabupaten/kota yang tergolong dalam klaster ini:
    """)
    st.dataframe(df_clustered, use_container_width=True)

    # --- Statistik Rata-rata ---
    st.markdown("---")
    
    st.markdown("### 📊 Visualisasi Rata-rata Jumlah Armada Ideal")

    import plotly.express as px
    import pandas as pd

    rata_rata_df = pd.DataFrame({
        "Jenis Armada": ["Arm Roll", "Truk Sampah", "Dump Truck"],
        "Jumlah Rata-rata": [
            round(df_filtered["arm roll ideal unit"].mean()),
            round(df_filtered["truk sampah ideal"].mean()),
            round(df_filtered["dump truck ideal"].mean())
        ]
    })

    
    fig_avg = px.bar(
        rata_rata_df,
        x="Jenis Armada",
        y="Jumlah Rata-rata",
        text="Jumlah Rata-rata",
        color="Jenis Armada",
        color_discrete_sequence=px.colors.qualitative.Set2,
        title=f"Rata-rata Kebutuhan Armada Ideal di Cluster {selected_cluster}"
    )

    fig_avg.update_traces(textposition='outside')
    fig_avg.update_layout(
        yaxis_title="Jumlah Armada",
        xaxis_title="Jenis Armada",
        title_x=0.3,
        height=500
    )

    st.plotly_chart(fig_avg, use_container_width=True)
    
    
    # # --- Visualisasi ---
    # st.markdown("### Distribusi Kebutuhan Armada per Kabupaten/Kota")
    # fig = px.bar(
    #     df_filtered,
    #     x="nama_kabupaten_kota",
    #     y=["arm roll ideal unit", "truk sampah ideal", "dump truck ideal"],
    #     barmode="group",
    #     title=f"Kebutuhan Armada Ideal per Jenis di Cluster {selected_cluster}",
    #     labels={"value": "Jumlah Armada", "variable": "Jenis Armada"},
    #     color_discrete_sequence=px.colors.qualitative.Set2
    # )
    # fig.update_layout(xaxis_title="Kabupaten/Kota", yaxis_title="Jumlah Armada")
    # st.plotly_chart(fig, use_container_width=True)

    # --- Gabungan (opsional tambahan) ---

    df_gabungan.columns = [
        f"{' '.join(col.replace('_', ' ').split()).title()}"
        for col in df_gabungan.columns
    ]
    st.markdown("""
    ---
    ### 📌 Data Gabungan Segmentasi dan Armada Ideal
    """)
    st.dataframe(df_gabungan)
