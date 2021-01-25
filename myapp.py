import yfinance as yf
import pandas as pd
import streamlit as st
from PIL import Image

image = Image.open('logo.png')
st.image(image, use_column_width=True)

st.write("""
# SIMPLE STOCK PRICE APP

Displaying the daily **closing price** and **volume** traded of stock

***
""")

# Input text box
st.header("Enter ticker symbol of stock ")
ticker_input = 'MSFT'
tickerSymbol = st.text_area("Ticker Symbol", ticker_input, height=50)

tickerSymbol = tickerSymbol.upper()

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