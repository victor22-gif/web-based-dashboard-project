# 📦 Order Analytics Dashboard

This is a web-based analytics dashboard built using **Python**, **Streamlit**, and **Plotly** to explore and visualize order data.

## 🚀 Features

- Upload or read from a CSV order file
- Parse addresses (ZIP, city, state)
- Visualize:
  - Top-selling products
  - Sales over time
  - Sales by location (map)
- Filter by date range
- Export filtered data

## 📂 Folder Structure


order-dashboard/
│
├── data/ # Contains sample orders.csv
├── order_dashboard.py # Main Streamlit dashboard
├── generate_csv.py # Script to generate sample data
├── requirements.txt # Dependencies
├── README.md # Project info
├── .gitignore # Ignore files in Git
└── LICENSE # Project license (MIT)


## 🛠️ Run the App

```bash
streamlit run order_dashboard.py
