import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Microsoft!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol1 = 'MSFT'
tickerSymbol2 = 'GOOGL'
#get data on this ticker
tickerData1 = yf.Ticker(tickerSymbol1)
tickerData2 = yf.Ticker(tickerSymbol2)
#get the historical prices for this ticker
tickerDf1 = tickerData1.history(period='1d', start='2011-1-1', end='2021-1-1')
tickerDf2 = tickerData2.history(period='1d', start='2011-1-1', end='2021-1-1')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

#tickerDf
#tickerData1.info
#tickerData1.calendar
#tickerData1.recommendations
st.line_chart(tickerDf1.Close)
st.line_chart(tickerDf2.Close)
st.line_chart(tickerDf1.Volume)