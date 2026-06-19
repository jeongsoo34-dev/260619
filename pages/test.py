import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Global Market Cap Top10 Dashboard",
    layout="wide"
)

st.title("🌎 Global Market Cap Top10 Stocks")
st.caption("최근 1년 주가 변화 비교")

# 글로벌 시가총액 Top10
stocks = {
    "NVIDIA": "NVDA",
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Amazon": "AMZN",
    "Alphabet": "GOOGL",
    "Meta": "META",
    "Broadcom": "AVGO",
    "Tesla": "TSLA",
    "TSMC": "TSM",
    "Saudi Aramco": "2222.SR"
}

end_date = datetime.today()
start_date = end_date - timedelta(days=365)

@st.cache_data
def load_data():
    all_data = pd.DataFrame()

    for company, ticker in stocks.items():
        try:
            df = yf.download(
                ticker,
                start=start_date,
                end=end_date,
                progress=False,
                auto_adjust=True
            )

            if len(df) > 0:
                df = df[["Close"]]
                df.columns = [company]

                if all_data.empty:
                    all_data = df
                else:
                    all_data = all_data.join(df, how="outer")

        except Exception:
            pass

    return all_data

prices = load_data()

# 정규화 (시작일 = 100)
normalized = prices.div(prices.iloc[0]).mul(100)

fig = go.Figure()

for col in normalized.columns:
    fig.add_trace(
        go.Scatter(
            x=normalized.index,
            y=normalized[col],
            mode="lines",
            name=col,
            hovertemplate=
            "<b>%{fullData.name}</b><br>" +
            "Date: %{x|%Y-%m-%d}<br>" +
            "Index: %{y:.2f}<extra></extra>"
        )
    )

fig.update_layout(
    title="1-Year Stock Performance (Base = 100)",
    template="plotly_white",
    height=700,
    hovermode="x unified",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ),
    xaxis_title="Date",
    yaxis_title="Normalized Return"
)

st.plotly_chart(fig, use_container_width=True)

# 수익률 테이블
returns = (
    (prices.iloc[-1] / prices.iloc[0] - 1) * 100
).sort_values(ascending=False)

st.subheader("📈 최근 1년 수익률")

result = pd.DataFrame({
    "Return (%)": returns.round(2)
})

st.dataframe(
    result,
    use_container_width=True
)
