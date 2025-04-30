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

## Part 3: LSTM Model

### Overview
- Built an LSTM (Long Short-Term Memory) network to capture sequential dependencies in stock prices.
- Trained on the same 15-year AAPL dataset.
- Input sequences: 30 days of past closing prices.
- Features: raw closing prices (normalized), no manual lag or moving-average features needed.

### Methodology
1. **Data Preparation**  
   - Download AAPL closing prices.  
   - Normalize the series to the [0, 1] range.  
   - Create overlapping sequences of length 90 as inputs and the next day’s price as the target.  
   - Split into 80% training and 20% testing sets.

2. **Model Architecture**  
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


## Tools and Libraries Used

- Python  
- Jupyter Notebook  
- yfinance (to get stock data)
- pandas, numpy (data handling and numerical operations)
- matplotlib (data visualization) 
- scikit-learn (for SVR and preprocessing)  
- xgboost (for gradient boosting)  
- scipy (optimization utilities)
- cvxpy (convex optimization)
- tensorflow and keras (DL experiments)
- torch (PyTorch-based modeling)



