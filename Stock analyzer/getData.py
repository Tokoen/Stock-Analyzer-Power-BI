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
    stock_price = stock_price[-5:-1]
    
    # Get financials (last 5 complete years)
    financials = stock.financials.T
    balance_sheet = stock.balance_sheet.T
    cash_flow = stock.cashflow.T
    dividends = stock.dividends.resample("YE").sum()
    dividends = dividends[-5:-1] if not dividends.empty else pd.Series([0]*4, index=stock_price.index)
    
    # Extract relevant data
    data = {
        "Year": stock_price.index.year,
        "Stock Price": stock_price.values,
        "Total Revenue": financials.get("Total Revenue", pd.Series([0]*4)).values[:4][::-1],
        "Net Income": financials.get("Net Income", pd.Series([0]*4)).values[:4][::-1],
        "Total Assets": balance_sheet.get("Total Assets", pd.Series([0]*4)).values[:4][::-1],
        "Total Liabilities": balance_sheet.get("Total Liabilities Net Minority Interest", pd.Series([0]*4)).values[:4][::-1],
        "Free Cash Flow": cash_flow.get("Free Cash Flow", pd.Series([0]*4)).values[:4][::-1],
        "Dividend Per Share": dividends.values[:4],
        "Ordinary Shares": balance_sheet.get("Ordinary Shares Number", pd.Series([0]*4)).values[:4][::-1]
    }
    
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

def prompt_for_ticker():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    ticker = simpledialog.askstring("Stock Ticker", "Enter the stock ticker symbol:")
    if ticker:
        try:
            df = get_financials(ticker.upper())
            os.makedirs("Financials", exist_ok=True)
            filename = os.path.join("Financials", f"Financials_{ticker.upper()}.csv")
            df.to_csv(filename, index=False, decimal=',')
            messagebox.showinfo("Success", f"Financial data saved as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data: {e}")
    else:
        messagebox.showwarning("Input Required", "No ticker entered!")

if __name__ == "__main__":
    prompt_for_ticker()