import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/davidirfan/PowerMeterDataAnalysis/refs/heads/main/table_power.csv", parse_dates=['DateTime'])

df = load_data()

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Raw Data"])

# Theme toggle (light/dark)
theme = st.sidebar.selectbox("Select Theme", ["light", "dark"])
if theme == "dark":
    st.markdown("""<style>body { background-color: #111; color: white; }</style>""", unsafe_allow_html=True)

# Dashboard Page
if page == "Dashboard":
    st.title("⚡ Power Monitoring Dashboard")

    # Date range filter
    date_range = st.date_input("Select date range", [df["DateTime"].min(), df["DateTime"].max()])
    if len(date_range) == 2:
        df = df[(df['DateTime'] >= pd.to_datetime(date_range[0])) & (df['DateTime'] <= pd.to_datetime(date_range[1]))]

    # Summary metrics
    st.subheader("🔍 Summary Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average Power (kW)", f"{df['Average Power'].mean():.2f}")
    col3.metric("Total Energy (Cumulative kWh)", f"{df['Cumulative kWh'].max():.2f}")

    # Line Charts
    st.subheader("📈 Time Series: Average Power")
    fig1 = px.line(df, x='DateTime', y='Average Power', title='Average Power Over Time')
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📉 Current and Voltage Comparison")
    fig2 = px.line(df, x='DateTime', y=['Current Phase A', 'Current Phase B', 'Current Phase C'],
                   title='Current per Phase',
                   labels={'value': 'Current (A)'},
                   color_discrete_sequence=['#1f77b4', '#d62728', '#2ca02c'])
    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.line(df, x='DateTime', y=['Voltage Phase A', 'Voltage Phase B', 'Voltage Phase C'],
                   title='Voltage per Phase',
                   labels={'value': 'Voltage (V)'},
                   color_discrete_sequence=['#1f77b4', '#d62728', '#2ca02c'])
    st.plotly_chart(fig3, use_container_width=True)

    # Dual Axis Chart: Average Real Power & Cumulative kWh
    st.subheader("⚡ Average Real Power vs. Cumulative kWh")
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(x=df['DateTime'], y=df['Average Real Power'], name='Average Real Power', yaxis='y1',
                              line=dict(color='#1f77b4')))
    fig4.add_trace(go.Scatter(x=df['DateTime'], y=df['Cumulative kWh'], name='Cumulative kWh', yaxis='y2',
                              line=dict(color='#d62728')))

    fig4.update_layout(
        title="Average Real Power and Cumulative kWh Over Time",
        xaxis=dict(title='DateTime'),
        yaxis=dict(title='Average Real Power (kW)', side='left'),
        yaxis2=dict(title='Cumulative kWh', overlaying='y', side='right'),
        legend=dict(x=0.01, y=0.99),
        margin=dict(l=40, r=40, t=40, b=40),
        width=1400,
        height=600
    )
    st.plotly_chart(fig4, use_container_width=True)

    # Dual Axis Chart: Voltage and Current for phase A
    st.subheader("🔌 Voltage Phase A and Current Phase A Over Time")
    fig5 = go.Figure()
    fig5.add_trace(go.Scatter(x=df['DateTime'], y=df['Voltage Phase A'], name='Voltage Phase A', yaxis='y1',
                              line=dict(color='#1f77b4')))
    fig5.add_trace(go.Scatter(x=df['DateTime'], y=df['Current Phase A'], name='Current Phase A', yaxis='y2',
                              line=dict(color='#d62728')))

    fig5.update_layout(
        title="Average Real Power and Cumulative kWh Over Time",
        xaxis=dict(title='DateTime'),
        yaxis=dict(title='Voltage (V)', side='left'),
        yaxis2=dict(title='Current (A)', overlaying='y', side='right'),
        legend=dict(x=0.01, y=0.99),
        margin=dict(l=40, r=40, t=40, b=40),
        width=1400,
        height=600
    )
    st.plotly_chart(fig5, use_container_width=True)

    # Dual Axis Chart: Voltage and Current for phase B
    st.subheader("🔌 Voltage Phase B and Current Phase B Over Time")
    fig6 = go.Figure()
    fig6.add_trace(go.Scatter(x=df['DateTime'], y=df['Voltage Phase B'], name='Voltage Phase B', yaxis='y1',
                              line=dict(color='#1f77b4')))
    fig6.add_trace(go.Scatter(x=df['DateTime'], y=df['Current Phase B'], name='Current Phase B', yaxis='y2',
                              line=dict(color='#d62728')))

    fig6.update_layout(
        title="Average Real Power and Cumulative kWh Over Time",
        xaxis=dict(title='DateTime'),
        yaxis=dict(title='Voltage (V)', side='left'),
        yaxis2=dict(title='Current (A)', overlaying='y', side='right'),
        legend=dict(x=0.01, y=0.99),
        margin=dict(l=40, r=40, t=40, b=40),
        width=1400,
        height=600
    )
    st.plotly_chart(fig6, use_container_width=True)
    
    # Dual Axis Chart: Voltage and Current for phase C
    st.subheader("🔌 Voltage Phase C and Current Phase C Over Time")
    fig7 = go.Figure()
    fig7.add_trace(go.Scatter(x=df['DateTime'], y=df['Voltage Phase C'], name='Voltage Phase C', yaxis='y1',
                              line=dict(color='#1f77b4')))
    fig7.add_trace(go.Scatter(x=df['DateTime'], y=df['Current Phase C'], name='Current Phase C', yaxis='y2',
                              line=dict(color='#d62728')))

    fig7.update_layout(
        title="Average Real Power and Cumulative kWh Over Time",
        xaxis=dict(title='DateTime'),
        yaxis=dict(title='Voltage (V)', side='left'),
        yaxis2=dict(title='Current (A)', overlaying='y', side='right'),
        legend=dict(x=0.01, y=0.99),
        margin=dict(l=40, r=40, t=40, b=40),
        width=1400,
        height=600
    )
    st.plotly_chart(fig7, use_container_width=True)

# Raw Data Page
elif page == "Raw Data":
    st.title("🗃 Raw Data Viewer")
    st.dataframe(df, use_container_width=True)
    st.download_button("Download Data as CSV", df.to_csv(index=False), "filtered_data.csv")
