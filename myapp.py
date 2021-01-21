import yfinance as yf
import pandas as pd
import streamlit as st

st.write("""
# SIMPLE STOCK PRICE APP

Displaying the daily **closing price** and **volume** traded of Google

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

st.write("""
## Closing Price

""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume

""")

st.line_chart(tickerDf.Volume)


st.write("""
## Calendar

""")

st.write(tickerData.calendar)


st.write("""
## Recommendations

""")

st.write(tickerData.recommendations)