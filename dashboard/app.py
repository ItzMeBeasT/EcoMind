import streamlit as st
import pandas as pd

st.set_page_config(page_title="EcoMind AI", layout="wide")
st.title("EcoMind AI")
st.caption("Campus Sustainability Intelligence")

df = pd.read_csv("data/energy_data.csv", parse_dates=["timestamp"])

c1, c2, c3 = st.columns(3)
c1.metric("Total Energy", f"{df.energy_kwh.sum():,.0f} kWh")
c2.metric("Average Hourly Energy", f"{df.energy_kwh.mean():.1f} kWh")
c3.metric("Buildings", df.building.nunique())

st.subheader("Energy Consumption")
chart = df.groupby("timestamp", as_index=True)["energy_kwh"].sum()
st.line_chart(chart)

st.subheader("Building Comparison")
building_energy = df.groupby("building")["energy_kwh"].sum().sort_values(ascending=False)
st.bar_chart(building_energy)
