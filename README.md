# Stock Analyzer in Power BI

## Overview
This Power BI template provides a comprehensive financial overview of individual stocks using data extracted via a Python script. The template consists of three key pages:
1. **Stock Overview** (Dashboard displaying key metrics and historical performance)
2. **Sector Comparison** (Benchmarking against industry peers)
3. **Risk Assessment** (Evaluation of financial risk factors)

## How It Works
### Data Extraction
A Python script is used to generate financial data in CSV format using the `yfinance` library. The script:
- Prompts the user for stock tickers.
- Fetches the last 4 complete years of financial data, including stock price, revenue, net income, assets, liabilities, free cash flow, dividends, and outstanding shares.
- Saves the extracted data as a CSV file in the `Financials` directory.

### Importing Data into Power BI
1. Run the Python script or use the provided executable (`.exe`) file to generate CSV files for stocks in the same sector.
2. Open the Power BI template.
3. Import the generated CSV files into Power BI.
4. Modify the **Stock** table by replacing the words "Ticker" twice with the stock ticker you want to analyze.
5. Do the same for the **Stock Sector** table, however, this table has multiple lines where this can be done. Use the first for the stock you want to analyze, and the remaining ones for the ones you want to compare it to. 
6. Refresh the dataset to populate all visualizations.

## Features
- **Stock Price Trend:** Visualizes price movements over the last four years.
- **Financial Performance:** Tracks revenue, net income, and profit margins.
- **Cash Flow & Dividend Analysis:** Displays free cash flow trends and dividend payouts.
- **Balance Sheet Overview:** Highlights total assets, liabilities, and debt ratio trends.
- **Ordinary Shares Outstanding:** Monitors changes in share count.

## Requirements
- Windows OS (for `.exe` file) or Python 3.10+
- `yfinance`, `pandas` and `tkinter` libraries (if using Python script)
- Power BI Desktop (Free version works)

## Running the Python Script
1. Run the `getFinancials.exe` file.
2. Alternatively, if using Python, install the required libraries:
   ```sh
   pip install yfinance pandas tkinter
   ```
3. Run the script:
   ```sh
   python getFinancials.py
   ```
4. Enter the stock tickers when prompted.
5. The script will generate CSV files in the `Financials` folder.

## Notes
- Ensure the stock tickers are valid before running the script.
- The **Stock Sector** table fits up to 4 stocks, but more can be added by copying the code.
- An example analysis on General Mills (GIS) has been provided as a reference in the 'Analysis' folder, as well as screenshots below.

## Screenshots
- Page 1:
![page 1](https://github.com/user-attachments/assets/be087d87-4b05-4937-a522-1901ca7ce879)

- Page 2: 
![page 2](https://github.com/user-attachments/assets/5cc50988-18f1-4b62-a18c-2255a7a0b8de)

- Page 3: 
![page 3](https://github.com/user-attachments/assets/a7a73ca3-aaf9-44ec-a2a6-4abfe267f310)


**Enjoy analyzing your stocks with Power BI!**

