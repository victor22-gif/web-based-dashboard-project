import streamlit as st
import pandas as pd
import plotly.express as px
import pgeocode

# 1. Page Setup
st.set_page_config(page_title="📦 Order Analytics Dashboard", layout="wide")
st.title("📦 Order Analytics Dashboard")

# 2. Load CSV
df = pd.read_csv("data/orders.csv")

# 3. Preprocess 
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['zip'] = df['address'].str.extract(r'(\d{5})')

# 4. Get lat/lon from ZIP
nomi = pgeocode.Nominatim('us')
df['lat'] = df['zip'].apply(lambda x: nomi.query_postal_code(str(x)).latitude if pd.notna(x) else None)
df['lon'] = df['zip'].apply(lambda x: nomi.query_postal_code(str(x)).longitude if pd.notna(x) else None)

# 5. Sidebar filters
st.sidebar.header("🔍 Filler")
date_min = df['order_date'].min()
date_max = df['order_date'].max()
date_range = st.sidebar.date_input("Select Date Range", [date_min, date_max])

if len(date_range) == 2:
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    df = df[(df['order_date'] >= start_date) & (df['order_date'] <= end_date)]

# 6. Show Data Preview
st.subheader("🗃️Filtered Data")
st.dataframe(df)

# 7. Top Products
st.subheader("🏆 Top Selling Products")
top_products = df.groupby('product')['quantity'].sum().sort_values(ascending=False).reset_index()
fig_top = px.bar(top_products, x='product', y='quantity', title='Top Products by Quantity')
st.plotly_chart(fig_top, use_container_width=True)

# 8. Sales Over Time
st.subheader("📈 Sales Over Time")
daily_sales = df.groupby('order_date')['total'].sum().reset_index()
fig_time = px.line(daily_sales, x='order_date', y='total', title='Daily Sales')
st.plotly_chart(fig_time, use_container_width=True)

# 9. Sales Map
st.subheader("🗺️ Sales by ZIP Code (Map)")
map_data = df.groupby(['zip', 'lat', 'lon'])['total'].sum().reset_index()
map_data = map_data.dropna(subset=['lat', 'lon'])

fig_map = px.scatter_mapbox(
    map_data,
    lat='lat',
    lon='lon',
    size='total',
    color='total',
    hover_name='zip',
    mapbox_style='carto-position',
    title='Sales Heatmap by ZIP'
)
st.plotly_chart(fig_map, use_container_width=True)

# 10. Export Button
st.subheader('⬇️ Export Filtered Data')
st.download_button('Download CSV', df.to_csv(index=False), 'filtered_orders.csv', 'text/csv')