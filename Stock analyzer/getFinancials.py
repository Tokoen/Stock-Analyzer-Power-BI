import yfinance as yf
import pandas as pd
import tkinter as tk
from tkinter import simpledialog, messagebox
import os

def get_financials(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    
    # Get stock history (Closing Price)
    stock_history = stock.history(period="5y")
    stock_price = stock_history["Close"].resample("YE").last()
    if(len(stock_price.values) >= 5):
        stock_price = stock_price[-5:-1]
    
    # Get financials (last 4 complete years)
    financials = stock.financials.T
    revenue = financials.get("Total Revenue", pd.Series([0]*4))
    revenueValues = revenue.values[:4][::-1]
    years = revenue.index.year[:4][::-1]
    balance_sheet = stock.balance_sheet.T
    cash_flow = stock.cashflow.T
    dividends = stock.dividends.resample("YE").sum()
    if(len(dividends.values) >= 5):
        dividends = dividends[-5:-1] if not dividends.empty else pd.Series([0]*4, index=stock_price.index)
    
    # Extract relevant data
    data = {
        "Year": years,
        "Stock Price": stock_price.values,
        "Total Revenue": revenueValues,
        "Net Income": financials.get("Net Income", pd.Series([0]*4)).values[:4][::-1],
        "Total Assets": balance_sheet.get("Total Assets", pd.Series([0]*4)).values[:4][::-1],
        "Total Liabilities": balance_sheet.get("Total Liabilities Net Minority Interest", pd.Series([0]*4)).values[:4][::-1],
        "Free Cash Flow": cash_flow.get("Free Cash Flow", pd.Series([0]*4)).values[:4][::-1],
        "Dividend Per Share": dividends.values,
        "Ordinary Shares": balance_sheet.get("Ordinary Shares Number", pd.Series([0]*4)).values[:4][::-1]
    }

    # Ensure each array has length 4 (add zeros in front if not)
    for key in data:
        if key != "Dividend Per Share":
            if len(data[key]) < 4:
                data[key] = [0] * (4 - len(data[key])) + list(data[key])
    
    # Handle missing years for dividends
    if len(data["Dividend Per Share"]) < 4:
        dividend_years = dividends.index.year.values
        dividend_values = dividends.values
        dividend_per_share = [0] * 4
        for i, year in enumerate(years):
            if year in dividend_years:
                dividend_per_share[i] = dividend_values[list(dividend_years).index(year)]
        data["Dividend Per Share"] = dividend_per_share
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Round values
    df["Stock Price"] = df["Stock Price"].round(2)
    df["Dividend Per Share"] = df["Dividend Per Share"].round(2)
    df["Total Revenue"] = df["Total Revenue"].round(0).astype('Int64')
    df["Net Income"] = df["Net Income"].round(0).astype('Int64')
    df["Total Assets"] = df["Total Assets"].round(0).astype('Int64')
    df["Total Liabilities"] = df["Total Liabilities"].round(0).astype('Int64')
    df["Free Cash Flow"] = df["Free Cash Flow"].round(0).astype('Int64')
    df["Ordinary Shares"] = df["Ordinary Shares"].round(0).astype('Int64')
    
    return df

def prompt_for_tickers():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    tickers = simpledialog.askstring("Stock Tickers", "Enter the stock ticker symbols separated by commas:")
    if tickers:
        tickers_list = [ticker.strip().upper() for ticker in tickers.split(',')]
        os.makedirs("Financials", exist_ok=True)
        for ticker in tickers_list:
            try:
                df = get_financials(ticker)
                filename = os.path.join("Financials", f"Financials_{ticker}.csv")
                df.to_csv(filename, index=False, decimal=',')
            except Exception as e:
                messagebox.showerror("Error", f"Failed to fetch data for {ticker}: {e}")
        messagebox.showinfo("Success", "Financial data saved for all tickers.")
    else:
        messagebox.showwarning("Input Required", "No tickers entered!")

if __name__ == "__main__":
    prompt_for_tickers()