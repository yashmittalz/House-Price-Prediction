# Pridicting House Prices Using Mutliple Linear Regression
'''In this Project we are gonna see how machine learning algorithms help us predict house prices. 
Linear recreation is model of predicting new future data by using the existing correlation between the old data. 
Here, machine learning helps us identify the relationship between feature data and output, so we can predict future values.'''

# House Price Prediction Application
import pandas as pd
from sklearn import linear_model

# Load the dataset
df = pd.read_csv("House Price Prediction/housepricesdataset.csv", sep=';')

# Define the feature set and output
X = df[['area', 'roomcount', 'buildingage']]
y = df['price']

# Create and train the linear regression model
reg = linear_model.LinearRegression()
reg.fit(X, y)

def predict_price(area, roomcount, buildingage):
    """Predict the price of a house based on its features."""
    # Create a DataFrame with the same feature names
    input_data = pd.DataFrame([[area, roomcount, buildingage]], columns=['area', 'roomcount', 'buildingage'])
    return reg.predict(input_data)[0]  # Use the DataFrame for prediction

def main():
    print("Welcome to the House Price Prediction App!\n")
    print("Predicts house prices using machine learning algorithms.\n")
    print("Utilizes linear regression to analyze historical data correlations.\n")
    print("Aims to be a step towards Yash's 50 projects showcasing data science applications.\n")
    print("Developed by Yash Mittal. Version 1.0")

    while True:
        try:
            area = float(input("Enter the area of the house (in square meters): "))
            roomcount = int(input("Enter the number of rooms: "))
            buildingage = int(input("Enter the age of the building (in years): "))
            
            predicted_price = predict_price(area, roomcount, buildingage)
            print(f"The predicted price of the house is: ${predicted_price:,.2f}")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        
        cont = input("Do you want to make another prediction? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()