import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Stock Explorer", layout="wide", page_icon="📈")

st.title("📈 Stock Price Explorer")
st.caption("Prices are indexed to 1.00 at the start, so each line shows growth since Jan 2018.")

st.info("💡 Did you know? The original Apple I computer was sold for $666.66 — not for any sinister reason, but simply because Steve Wozniak liked repeating digits. He later said he had no idea the number had any other connotations. (Source: Wikipedia)")

@st.cache_data
def load_data():
    df = px.data.stocks()
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()
tickers = [c for c in df.columns if c != "date"]

# ── Sidebar ──────────────────────────────────────────────────────────────────
st.sidebar.header("⚙️ Controls")
chosen = st.sidebar.multiselect("Choose stocks", tickers, default=["AAPL", "MSFT", "GOOG"])

if not chosen:
    st.warning("Pick at least one stock from the sidebar.")
    st.stop()

# Date-range slider
min_date = df["date"].min().date()
max_date = df["date"].max().date()
date_range = st.sidebar.slider(
    "📅 Date range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    format="MMM YYYY",
)
mask = (df["date"].dt.date >= date_range[0]) & (df["date"].dt.date <= date_range[1])
dff = df[mask].copy()

# ── Top KPI row ───────────────────────────────────────────────────────────────
st.subheader("📊 Performance Summary")
cols = st.columns(len(chosen) + 2)

growths = {}
for col, t in zip(cols, chosen):
    start = dff[t].iloc[0]
    end   = dff[t].iloc[-1]
    growth = (end - start) / start * 100
    growths[t] = growth
    col.metric(t, f"{end:.2f}x", f"{growth:+.1f}%")

best = max(growths, key=growths.get)
cols[len(chosen)].metric("🏆 Best Performer", best, f"{growths[best]:+.1f}%")

volatilities = {t: dff[t].pct_change().std() * 100 for t in chosen}
most_volatile = max(volatilities, key=volatilities.get)
cols[len(chosen) + 1].metric("⚡ Most Volatile", most_volatile, f"σ = {volatilities[most_volatile]:.2f}%")

st.divider()

# ── Line chart ────────────────────────────────────────────────────────────────
st.subheader("📈 Normalized Price Over Time")
fig_line = px.line(
    dff, x="date", y=chosen,
    title="Normalized stock price (base = 1.00)",
    labels={"value": "Price (indexed)", "date": "Date", "variable": "Ticker"},
    template="plotly_white",
)
fig_line.update_traces(line=dict(width=2))
fig_line.update_layout(hovermode="x unified", legend_title_text="Ticker")
st.plotly_chart(fig_line, use_container_width=True)

# ── Bar chart ─────────────────────────────────────────────────────────────────
st.subheader("📊 Total Growth % by Stock")
growth_df = pd.DataFrame({"Ticker": list(growths.keys()), "Growth (%)": list(growths.values())})
fig_bar = px.bar(
    growth_df, x="Ticker", y="Growth (%)",
    color="Growth (%)",
    color_continuous_scale="RdYlGn",
    text_auto=".1f",
    title="Total growth % in selected period",
    template="plotly_white",
)
fig_bar.update_layout(coloraxis_showscale=False)
st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# ── Investment calculator ─────────────────────────────────────────────────────
st.subheader("💰 What if I invested…?")
inv_col1, inv_col2 = st.columns(2)
with inv_col1:
    inv_stock = st.selectbox("Pick a stock", chosen)
with inv_col2:
    inv_amount = st.number_input("Amount ($)", min_value=1, value=1000, step=100)

start_price = dff[inv_stock].iloc[0]
end_price   = dff[inv_stock].iloc[-1]
worth = inv_amount * (end_price / start_price)
profit = worth - inv_amount

result_col1, result_col2, result_col3 = st.columns(3)
result_col1.metric("Invested", f"${inv_amount:,.2f}")
result_col2.metric("Worth today", f"${worth:,.2f}", f"{profit:+,.2f}")
result_col3.metric("Return", f"{growths[inv_stock]:+.1f}%")
