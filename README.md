# Stock Analyzer Power BI Template

## Overview
This Power BI template provides a comprehensive financial overview of individual stocks using data extracted via a Python script. The template consists of three key pages:
1. **Stock Overview** (Dashboard displaying key metrics and historical performance)
2. **Sector Comparison** (Benchmarking against industry peers)
3. **Risk Assessment** (Evaluation of financial risk factors)

## How It Works
### Data Extraction
A Python script is used to generate financial data in CSV format using the `yfinance` library. The script:
- Prompts the user for a stock ticker.
- Fetches the last 5 years of financial data, including stock price, revenue, net income, assets, liabilities, free cash flow, dividends, and outstanding shares.
- Saves the extracted data as a CSV file in the `Financials` directory.

### Importing Data into Power BI
1. Run the Python script or use the provided executable (`.exe`) file to generate CSV files for the desired stock tickers.
2. Open the Power BI template.
3. Import the generated CSV files into Power BI.
4. Modify the **Stock** and **Stock Sector** tables to reflect the imported stock tickers.
5. Refresh the dataset to populate all visualizations.

## Features
- **Stock Price Trend:** Visualizes price movements over the last four years.
- **Financial Performance:** Tracks revenue, net income, and profit margins.
- **Cash Flow & Dividend Analysis:** Displays free cash flow trends and dividend payouts.
- **Balance Sheet Overview:** Highlights total assets, liabilities, and debt ratio trends.
- **Ordinary Shares Outstanding:** Monitors changes in share count.

## Requirements
- Windows OS (for `.exe` file) or Python 3.10+
- `yfinance` and `pandas` libraries (if using Python script)
- Power BI Desktop

## Running the Python Script
1. If using Python, install the required libraries:
   ```sh
   pip install yfinance pandas tkinter
   ```
2. Run the script:
   ```sh
   python script.py
   ```
3. Alternatively, run the provided `.exe` file.
4. Enter the stock ticker when prompted.
5. The script will generate a CSV file in the `Financials` folder.

## Notes
- Ensure the stock ticker is valid before running the script.
- The template currently supports individual stocks but can be expanded for more complex analysis.
- Additional pages for sector comparison and risk assessment further enhance decision-making.

## Future Enhancements
- Automate stock sector classification.
- Integrate real-time data refresh in Power BI.
- Expand risk assessment metrics.

**Enjoy analyzing your stocks with Power BI!**

