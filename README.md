# Stock-Market-Forecasting
This project aims to predict stock market prices using advanced Deep Learning and Machine Learning techniques. 

# This project is currently under development and is a work in progress.


### Use 'pip install -r requirements.txt' to install required libraries.


# Stock Price Prediction using SVR, XGBoost and LSTM

This project compares two machine learning models (Support Vector Regression (SVR) and XGBoost) and a deep learning model (LSTM) for predicting stock prices. All the models use historical closing prices of tech companies, with the goal of forecasting future prices based on patterns in past data.

---

## Part 1: SVR Model

### Overview

The SVR model was trained using 15 years of Apple (AAPL) stock data. The training features included 60-day lag values (previous closing prices), a 7-day moving average, and a 30-day moving average.

After training the model on AAPL, it was tested on several other tech companies to see if the model could generalize well.

### Key Details

- Training stock: AAPL  
- Test stocks: GOOG, MSFT, META, AMZN, NVDA, QCOM, AMD, TSLA, NFLX, IBM  
- Features: Lag values (60), 7-day MA, 30-day MA  
- Evaluation: RMSE (Root Mean Squared Error)

### Results

The model gave accurate results for most of the test stocks. Especially for GOOG, AMZN, NVDA, QCOM, AMD, and IBM, the RMSE values were low, and the predicted prices followed the actual trend closely. This suggests that many tech stocks might follow similar price patterns, making it easier for the model to generalize from one stock to others.

---

## Part 2: XGBoost Model

### Overview

XGBoost was also trained using the same AAPL data and the same set of features as the SVR model. It is a gradient boosting method known for performing well on structured data.

### Key Details

- Training stock: AAPL  
- Features: Lag values (60), 7-day MA, 30-day MA  
- Model tuning: Tried different settings for the number of trees, depth, and learning rate  
- Evaluation: RMSE  

### Results

The XGBoost model struggled to give accurate results on AAPL as well as other stocks. Even after adjusting different model parameters and trying other stocks, the predictions were not very consistent. This may be because XGBoost is less suited for handling the type of fluctuations that are common in stock prices.

---

## Tools and Libraries Used

- Python  
- Jupyter Notebook  
- yfinance (to get stock data)  
- scikit-learn (for SVR and preprocessing)  
- xgboost (for gradient boosting)  
- pandas, numpy, matplotlib



