# Stock Price Prediction

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Compare **SVR**, **XGBoost**, and **LSTM** models for forecasting tech stock closing prices from historical data. Trained on Apple (AAPL) and evaluated across major tech tickers.

> **Disclaimer:** This project is for learning and research only. It is not financial advice.

## Table of contents

- [Project structure](#project-structure)
- [Quick start](#quick-start)
- [Notebooks](#notebooks)
- [Model comparison](#model-comparison)
- [SVR model](#svr-model)
- [XGBoost model](#xgboost-model)
- [LSTM model](#lstm-model)
- [Tools and libraries](#tools-and-libraries)
- [Contributors](#contributors)
- [Attribution](#attribution)

## Project structure

```text
stock-price-prediction/
├── README.md
├── LICENSE
├── requirements.txt
├── requirements-minimal.txt
├── docs/
│   └── images/              # README screenshots (add exported plots here)
└── notebooks/
    ├── 01_svr_stock_prediction.ipynb
    ├── 02_xgboost_stock_prediction.ipynb
    └── 03_lstm_stock_prediction.ipynb
```

## Quick start

```bash
git clone https://github.com/danishb7/stock-price-prediction.git
cd stock-price-prediction
pip install -r requirements.txt
jupyter notebook
```

Open notebooks in order under `notebooks/`. For SVR and XGBoost only, you can use `pip install -r requirements-minimal.txt` plus the LSTM dependencies listed in that file.

## Notebooks

| # | Notebook | Model |
|---|----------|--------|
| 01 | [`notebooks/01_svr_stock_prediction.ipynb`](notebooks/01_svr_stock_prediction.ipynb) | Support Vector Regression |
| 02 | [`notebooks/02_xgboost_stock_prediction.ipynb`](notebooks/02_xgboost_stock_prediction.ipynb) | XGBoost |
| 03 | [`notebooks/03_lstm_stock_prediction.ipynb`](notebooks/03_lstm_stock_prediction.ipynb) | LSTM (deep learning) |

## Model comparison

| Model | Best suited for | Generalization on test tickers |
|-------|-----------------|--------------------------------|
| **SVR** | Lag + moving-average features | Strong on GOOG, AMZN, NVDA, QCOM, AMD, IBM |
| **XGBoost** | Structured tabular features | Inconsistent; sensitive to price volatility |
| **LSTM** | Raw sequential closes | Strong trend capture; less manual feature engineering |

### SVR RMSE highlights (trained on AAPL)

| Ticker | RMSE |
|--------|------|
| AAPL | 1.58 |
| GOOG | 1.45 |
| AMZN | 2.05 |
| NVDA | 1.18 |
| QCOM | 2.10 |
| AMD | 2.20 |
| IBM | 1.71 |

Lower RMSE on several tickers suggests similar patterns across many tech stocks after training on AAPL.

---

## SVR model

### Overview

The SVR model was trained using 15 years of Apple (AAPL) stock data. The training features included 60-day lag values (previous closing prices), a 7-day moving average, and a 30-day moving average.

After training the model on AAPL, it was tested on several other tech companies to see if the model could generalize well.

### Key details

- Training stock: AAPL
- Test stocks: GOOG, MSFT, META, AMZN, NVDA, QCOM, AMD, TSLA, NFLX, IBM
- Features: Lag values (60), 7-day MA, 30-day MA
- Evaluation: RMSE (Root Mean Squared Error)

### Results

The model gave accurate results for most of the test stocks. Especially for GOOG, AMZN, NVDA, QCOM, AMD, and IBM, the RMSE values were low, and the predicted prices followed the actual trend closely.

---

## XGBoost model

### Overview

XGBoost was also trained using the same AAPL data and the same set of features as the SVR model. It is a gradient boosting method known for performing well on structured data.

### Key details

- Training stock: AAPL
- Features: Lag values (60), 7-day MA, 30-day MA
- Model tuning: Different settings for trees, depth, and learning rate
- Evaluation: RMSE

### Results

The XGBoost model struggled to give accurate results on AAPL as well as other stocks. Even after adjusting different model parameters and trying other stocks, the predictions were not very consistent. This may be because XGBoost is less suited for handling the type of fluctuations that are common in stock prices.

---

## LSTM model

### Overview

- Built an LSTM (Long Short-Term Memory) network to capture sequential dependencies in stock prices.
- Trained on the same 15-year AAPL dataset.
- Input sequences: 90 days of past closing prices.
- Features: raw closing prices (normalized), no manual lag or moving-average features needed.

### Methodology

1. **Data preparation**
   - Download AAPL closing prices.
   - Normalize the series to the [0, 1] range.
   - Create overlapping sequences of length 90 as inputs and the next day’s price as the target.
   - Split into 80% training and 20% testing sets.

2. **Model architecture**
   - Dropout layers to reduce overfitting.
   - Dense output layer for price prediction.

3. **Training**
   - Loss: Mean Squared Error
   - Optimizer: Adam
   - Epochs: 30

4. **Evaluation**
   - Compute RMSE on the test set.
   - Plot actual vs. predicted prices over time.

### Results

- The LSTM model captured longer-term trends better than the other two methods in many cases.
- RMSE on AAPL was comparable to or lower than SVR and XGBoost after sufficient training.
- Shows that deep sequential models can leverage temporal patterns directly, without manual feature engineering.

---

## Tools and libraries

- Python
- Jupyter Notebook
- [yfinance](https://github.com/ranaroussi/yfinance) (stock data)
- pandas, numpy (data handling)
- matplotlib (visualization)
- scikit-learn (SVR and preprocessing)
- xgboost (gradient boosting)
- scipy, cvxpy (optimization utilities in LSTM notebook)
- TensorFlow, Keras, PyTorch (deep learning)

## Contributors

- **Danish Bhatkar**  
  [GitHub](https://github.com/danishb7) | [LinkedIn](https://www.linkedin.com/in/danish-bhatkar)

- **Mohammad Alshurbaji**  
  [GitHub](https://github.com/Mohammadalshurbaji) | [LinkedIn](https://www.linkedin.com/in/mohammadalshurbaji)

## Attribution

Forked from [Mohammadalshurbaji/Stock-Market-Forecasting](https://github.com/Mohammadalshurbaji/Stock-Market-Forecasting). Original collaboration under the Infinity Team learning project.
