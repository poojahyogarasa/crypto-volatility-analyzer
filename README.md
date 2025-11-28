# 📊 Cryptocurrency Volatility Analyzer
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-brightgreen)
![Status](https://img.shields.io/badge/Status-Live-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)


A simple, interactive **Streamlit web app** to explore the **risk & volatility** of a cryptocurrency using historical price data.

Upload a CSV file with `Date` and `Close` columns, and the app will compute daily returns, rolling volatility windows, and visualize both the price and volatility over time.

🔗 **Live App:**  
https://crypto-volatility-analyzer-7dkmke7gg77pqgypvrzhft.streamlit.app/

---
![Home](home.png)
![Dashboard](dashboard.png)
![Charts](charts.png)

---

## 🚀 Features

- 📁 **CSV Upload**  
  - Accepts a CSV file with `Date` and `Close` columns  
  - Example: Bitcoin (BTC) or Ethereum (ETH) daily closing prices

- 📈 **Volatility Metrics** (based on daily returns)
  - 7-day volatility (short-term noise)
  - 30-day volatility (medium-term risk)
  - 90-day volatility (long-term view – shown when enough data)
  - Overall **Risk Level** badge (Low / Medium / High) based on 30D volatility

- 📉 **Visualizations**
  - Price over time line chart  
  - Rolling 30-day volatility chart  

- 📋 **Last 10 Records Table**
  - Shows Date, Close, Return, and rolling volatility values (7D, 30D, 90D)

- 🧪 **Sample Dataset**
  - Included example file `btc_sample.csv` for quick testing

---

## 📂 Project Structure

```text
crypto-volatility-analyzer/
├─ crypto_vol_app.py        # Main Streamlit app
├─ btc_sample.csv           # Sample BTC data (Date, Close)
├─ requirements.txt         # Python dependencies
└─ README.md                # Project documentation (this file)

```
---
## 🧠 How It Works (High Level)

This app analyzes cryptocurrency volatility using the following steps:

1. **Upload CSV File**
   - User uploads a CSV containing `Date` and `Close` price columns.

2. **Data Preparation**
   - Dates are converted to datetime format.
   - Dataset is sorted in chronological order.

3. **Daily Returns Calculation**
   - Computes day-to-day percentage changes in closing price.

4. **Rolling Volatility**
   - Calculates the standard deviation of returns over:
     - 7-day window (short-term)
     - 30-day window (medium-term)
     - 90-day window (long-term)

5. **Risk Level Classification**
   - Based on 30D volatility:
     - **Low Risk** → < 2%
     - **Medium Risk** → moderate
     - **High Risk** → above threshold

6. **Visual Output**
   - Price Over Time chart
   - Rolling 30D Volatility chart
   - Volatility metric summary (7D, 30D, 90D)
   - Last 10 records table with returns & volatility values

---

## 🛠️ Tech Stack

- Python 3.11  
- Streamlit  
- Pandas  
- NumPy  
- Matplotlib  

---

## 💻 Run Locally

### 1️⃣ Clone Repository
```bash
git clone https://github.com/poojahyogarasa/crypto-volatility-analyzer.git
cd crypto-volatility-analyzer
````
### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate

python3 -m venv venv
source venv/bin/activate

```
### 3️⃣ Install Requirements

````bash
pip install -r requirements.txt

````
### 4️⃣ Run App

````bash
streamlit run crypto_vol_app.py

````
---
## 📥 CSV Format

Your uploaded CSV file **must contain** the following columns:

```text
Date, Close
2024-01-01, 42568.32
2024-01-02, 43210.55
2024-01-03, 42877.12
````
Date → Daily timestamp (YYYY-MM-DD or similar)

Close → Daily closing price of the cryptocurrency
Works for BTC, ETH, or any asset with daily OHLC data.

---
## 🌱 Future Enhancements

- Add support for multiple cryptocurrencies  
- Integrate candlestick chart visualizations  
- Add machine learning models to forecast volatility  
- Allow user-defined rolling window sizes  
- Include additional metrics (Sharpe Ratio, VaR, CVaR)  
- Add comparison mode for BTC vs ETH or any two assets  
- Add downloadable charts and result summaries  
- Implement database support for storing past analyses  
- Add dark/light theme toggle  
- Deploy mobile-friendly responsive UI  
---

## 👩‍💻 Author

**Poojah Yogarasa**  
Computer Engineering Undergraduate  
University of Jaffna, Sri Lanka  

🔗 **GitHub:** https://github.com/poojahyogarasa  
🔗 **LinkedIn:** https://www.linkedin.com/in/poojahyogarasa  

Passionate about software engineering, AI, data science, and building real-world tech projects.

---



