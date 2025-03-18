import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/fransiskaartha/Bike-Sharing-dataset/refs/heads/main/day.csv")


day_df = pd.read_csv("https://raw.githubusercontent.com/fransiskaartha/Bike-Sharing-dataset/refs/heads/main/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/fransiskaartha/Bike-Sharing-dataset/refs/heads/main/hour.csv")

day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Bagian Streamlit layout
st.title("Bike Sharing Dashboard")
st.sidebar.header("Filter Data")

# Bagian Sidebar filters
start_date = st.sidebar.date_input("Start Date", day_df['dteday'].min())
end_date = st.sidebar.date_input("End Date", day_df['dteday'].max())

season_options = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
season = st.sidebar.multiselect("Season", options=list(season_options.keys()), format_func=lambda x: season_options[x], default=list(season_options.keys()))

weather_options = {1: "Clear", 2: "Cloudy", 3: "Light Rain/Snow", 4: "Heavy Rain/Snow"}
weather = st.sidebar.multiselect("Weather", options=list(weather_options.keys()), format_func=lambda x: weather_options[x], default=list(weather_options.keys()))

temp_range = st.sidebar.slider("Temperature Range (normalized)", float(day_df['temp'].min()), float(day_df['temp'].max()), (float(day_df['temp'].min()), float(day_df['temp'].max())))

# Filtering data
filtered_df = day_df[
    (day_df['dteday'] >= pd.to_datetime(start_date)) &
    (day_df['dteday'] <= pd.to_datetime(end_date)) &
    (day_df['season'].isin(season)) &
    (day_df['weathersit'].isin(weather)) &
    (day_df['temp'].between(temp_range[0], temp_range[1]))
]

# Bagian Plot Tren Penyewaan Sepeda
st.subheader("Tren Penyewaan Sepeda Sepanjang Tahun")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(filtered_df['dteday'], filtered_df['cnt'], marker='o', linestyle='-', color='#FF69B4')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Tren Penyewaan Sepeda")
st.pyplot(fig)

# Bagian Heatmap Korelasi
st.subheader("Heatmap Korelasi Antar Faktor")
fig, ax = plt.subplots(figsize=(10, 6))
corr_matrix = filtered_df.corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
st.pyplot(fig)
