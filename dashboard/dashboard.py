import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.load_data import load_data

# Page config
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

# Load data
rfm_df, segment_analysis, geo_df = load_data()

# HEADER
st.title("E-Commerce Customer & Geographic Analysis")
st.markdown("Analisis segmentasi pelanggan dan distribusi geografis")

# SIDEBAR FILTER
st.sidebar.header("Filter")

# Filter segment
selected_segment = st.sidebar.multiselect(
    "Pilih Segment",
    options=rfm_df['segment'].unique(),
    default=rfm_df['segment'].unique()
)

# Filter Top N state
top_n = st.sidebar.slider(
    "Top N State (Revenue)",
    min_value=5,
    max_value=20,
    value=10
)

# APPLY FILTER
filtered_rfm = rfm_df[rfm_df['segment'].isin(selected_segment)]

# Recalculate segment analysis based on filter
filtered_segment = filtered_rfm.groupby('segment').agg({
    'customer_id':'count',
    'monetary':'sum',
    'frequency':'mean'
}).rename(columns={
    'customer_id':'total_customer',
    'monetary':'total_revenue'
})

# KPI (dynamic)
total_revenue = filtered_segment['total_revenue'].sum()
total_customer = filtered_rfm['customer_id'].nunique()

col1, col2 = st.columns(2)
col1.metric("Total Revenue", f"{total_revenue:,.0f}")
col2.metric("Total Customers", f"{total_customer:,}")

st.divider()

# RFM SECTION
st.subheader("Customer Segmentation (RFM)")

col1, col2 = st.columns(2)

# Distribusi segment
with col1:
    fig, ax = plt.subplots()
    filtered_rfm['segment'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title("Customer Segment Distribution")
    st.pyplot(fig)

# Revenue per segment
with col2:
    fig, ax = plt.subplots()
    filtered_segment['total_revenue'].plot(kind='bar', ax=ax)
    ax.set_title("Revenue per Segment")
    st.pyplot(fig)

# GEO SECTION
st.subheader("Geographical Analysis")

col1, col2 = st.columns(2)

# Top state dynamic
top_state = geo_df.sort_values(by='total_revenue', ascending=False).head(top_n)

# Top state revenue
with col1:
    fig, ax = plt.subplots()
    top_state.set_index('state_name')['total_revenue'].plot(kind='bar', ax=ax)
    ax.set_title(f"Top {top_n} State by Revenue")
    st.pyplot(fig)

# Revenue share
with col2:
    fig, ax = plt.subplots()
    top_state.set_index('state_name')['revenue_share'].plot(kind='bar', ax=ax)
    ax.set_title("Revenue Share")
    st.pyplot(fig)
    
selected_state = st.sidebar.multiselect(
    "Filter State",
    options=geo_df['state_name'].unique(),
    default=geo_df['state_name'].unique()
)

# Styling

# Load Font Awesome + CSS + Font
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
    background-color: #f6fff8;
}

h1 {
    color: #1b5e20;
    font-weight: 600;
}

.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    text-align: center;
}

.metric-title {
    font-size: 14px;
    color: #777;
    margin-bottom: 5px;
}

.metric-value {
    font-size: 28px;
    font-weight: bold;
    color: #2e7d32;
}

.section-title {
    font-size: 20px;
    font-weight: 600;
    color: #1b5e20;
    margin-top: 30px;
    margin-bottom: 10px;
}

.icon {
    margin-right: 8px;
    color: #2e7d32;
}
</style>
""", unsafe_allow_html=True)


# Header
st.markdown("""
<h1><i class="fa-solid fa-chart-line icon"></i>E-Commerce Dashboard</h1>
<p style='color:#555;'>Customer Segmentation & Geographic Analysis</p>
""", unsafe_allow_html=True)


# KPI Cards
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
            <i class="fa-solid fa-dollar-sign icon"></i>Total Revenue
        </div>
        <div class="metric-value">{total_revenue:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
            <i class="fa-solid fa-users icon"></i>Total Customers
        </div>
        <div class="metric-value">{total_customer:,}</div>
    </div>
    """, unsafe_allow_html=True)


# Section RFM
st.markdown('<div class="section-title"><i class="fa-solid fa-chart-pie icon"></i>Customer Segmentation (RFM)</div>', unsafe_allow_html=True)

fig, ax = plt.subplots()
filtered_rfm['segment'].value_counts().plot(
    kind='bar',
    color='#66bb6a',
    ax=ax
)
ax.set_title("Customer Segment Distribution")
st.pyplot(fig)


# Section GEO
st.markdown('<div class="section-title"><i class="fa-solid fa-globe icon"></i>Geographical Analysis</div>', unsafe_allow_html=True)


# Sidebar
st.sidebar.markdown("## <i class='fa-solid fa-sliders icon'></i>Filter Dashboard", unsafe_allow_html=True)
st.sidebar.markdown("---")