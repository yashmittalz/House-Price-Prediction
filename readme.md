# House Price Prediction

## Overview
This project demonstrates how machine learning algorithms can be utilized to predict house prices using multiple linear regression. By analyzing historical data, the model identifies relationships between various features of a house and its price, allowing for accurate predictions of future values.

## Project Goals
1. **Machine Learning Application**: Explore how machine learning algorithms help in predicting house prices.
2. **Dataset Usage**: Utilize a small dataset for initial testing, with the capability to scale to larger, more complex datasets.
3. **Model Development**: Build a predictive model using the `sklearn.linear_model` module.

## Predictive Examples
The model can predict sale prices for the following properties:
- A house with 230 square meters, 4 rooms, and 10 years of building age.
- A house with 230 square meters, 6 rooms, and 0 years of building age (new building).
- A house with 355 square meters, 3 rooms, and 20 years of building age.

## Definition of Multiple Linear Regression
Multiple linear regression is a statistical technique used to model the relationship between one dependent variable and two or more independent variables.

### Equation
The model is typically expressed as:

𝑌 = 𝛽0 + 𝛽1𝑋1 + 𝛽2𝑋2 + ... + 𝛽𝑛𝑋𝑛 + 𝜀

Where:
- 𝑌 is the dependent variable.
- 𝑋 is the independent variables.
- 𝛽 represents the coefficients.
- 𝜀 is the error term.

### Objective
The primary goal is to predict the value of the dependent variable based on the values of the independent variables by minimizing the difference between the predicted and actual values.

### Assumptions
Key assumptions include:
- Linearity
- Independence of errors
- Homoscedasticity (constant variance of errors)
- Normality of error terms

### Applications
Widely used in various fields such as economics, social sciences, and real estate to analyze the influence of multiple factors on a single outcome.

## Features
- Predicts house prices based on area, number of rooms, and building age.
- Utilizes linear regression for analysis.
- User-friendly command-line interface for input.

## Requirements
- Python 3.x
- Pandas
- Scikit-learn

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yashmittalz/house-price-prediction.git
   cd house-price-prediction
   ```

2. Install the required packages:
   ```bash
   pip install pandas scikit-learn
   ```

3. Ensure you have the dataset `housepricesdataset.csv` in the `House Price Prediction` directory.

## Usage
1. Run the application using the following command:
    ```bash
    python main.py 
    ```
    
2. Follow the prompts to enter the area, number of rooms, and building age to receive a predicted house price.

## Contributing
Feel free to submit issues or pull requests if you have suggestions for improvements or new features.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Developed by Yash Mittal. Version 1.0