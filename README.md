# Stock-Market-Forecasting
This project aims to predict stock market prices using advanced Deep Learning and Machine Learning techniques. 

# This project is currently under development and is a work in progress.


### Use 'pip install -r requirements.txt' to install required libraries.


# 📈 Stock Price Prediction using SVR and XGBoost

This project compares the performance of two machine learning models: **Support Vector Regression (SVR)** and **XGBoost Regressor**, in forecasting stock prices. Both models are trained on historical data for AAPL and tested on several major tech stocks to evaluate their predictive accuracy and generalization ability.

---

## 📘 Part 1: Support Vector Regression (SVR)

### 🔍 Overview

The SVR model is trained using 15 years of historical closing prices of AAPL. The input features are engineered to include 60-day lag values and moving averages (7-day and 30-day). The trained model is then tested on a selection of other tech stocks to assess generalization.

### ⚙️ Methodology

- **Training stock**: AAPL (2010–2024)
- **Features**:
  - Lagged closing prices (up to 60 days)
  - 7-day moving average
  - 30-day moving average
- **Model**: SVR with RBF kernel (`scikit-learn`)
- **Scaler**: StandardScaler
- **Test stocks**: GOOG, MSFT, META, AMZN, NVDA, QCOM, AMD, TSLA, NFLX, IBM
- **Evaluation metric**: RMSE (Root Mean Squared Error)

### 📊 Results

- The trained SVR model was able to **predict with high accuracy** on the following stocks:
  - GOOG, AMZN, NVDA, QCOM, AMD, IBM
- All test stocks were plotted with actual vs. predicted prices.
- RMSE was printed for each stock directly on the plot.

### 💡 Key Insight

Despite being trained on a single stock (AAPL), the SVR model generalized surprisingly well to other tech stocks. This suggests potential similarities in the temporal behavior of companies in the tech sector.

---

## 📗 Part 2: XGBoost Regressor

### 🔍 Overview

XGBoost is applied to the same prediction task using the same feature set as the SVR model. The model is trained on AAPL stock and evaluated primarily on AAPL.

### ⚙️ Methodology

- **Training stock**: AAPL (2014–2024)
- **Features**:
  - Lagged closing prices (up to 60 days)
  - 7-day moving average
  - 30-day moving average
- **Model**: XGBRegressor (`xgboost`)
- **Scaler**: StandardScaler
- **Evaluation metric**: RMSE

### 📊 Results

- Results presented in the notebook are based on AAPL stock.
- Despite testing on other stocks and experimenting with different parameter settings (e.g., number of trees, max depth, learning rate), the model did not generalize as well as SVR.
- The RMSE for AAPL was moderate, but performance on other stocks was inconsistent.

### ⚠️ Observations

Tree-based models like XGBoost may struggle with noisy, volatile time series data unless enhanced with external features or hybrid approaches.

---

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- [yfinance](https://pypi.org/project/yfinance/) – historical stock data
- [scikit-learn](https://scikit-learn.org/) – SVR, preprocessing, evaluation
- [xgboost](https://xgboost.readthedocs.io/) – gradient boosting
- `pandas`, `numpy` – data manipulation
- `matplotlib` – visualization



