import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# load dataset
df = pd.read_csv("house_data.csv")

print("\nShowing some data:\n")
print(df.head())

print("\nChecking if any values are missing:\n")
print(df.isnull().sum())

# selecting input and output
X = df[['area', 'bedrooms', 'age']]
y = df['price']

# IMPORTANT: keep this exactly same for stable results
Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# training the model
lr = LinearRegression()
lr.fit(Xtr, ytr)

# predictions on test data
preds = lr.predict(Xte)

# evaluation
mse = mean_squared_error(yte, preds)
rmse = np.sqrt(mse)
r2 = r2_score(yte, preds)

print("\nModel performance:")
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)

print("\nActual vs Predicted:")
print("Actual:", list(yte))
print("Predicted:", preds)

# user input loop
while True:
    print("\nEnter house details (within valid range)")
    print("Area: 800–2000 | Bedrooms: 1–4 | Age: 1–15")

    try:
        a = float(input("Area: "))
        b = int(input("Bedrooms: "))
        c = int(input("Age: "))

        # simple checks
        if a < 800 or a > 2000:
            print("Area out of range")
            continue
        if b < 1 or b > 4:
            print("Bedrooms out of range")
            continue
        if c < 1 or c > 15:
            print("Age out of range")
            continue

        # prediction
        inp = pd.DataFrame([[a, b, c]],
                           columns=['area', 'bedrooms', 'age'])

        price = lr.predict(inp)[0]

        print("\nPredicted price (raw):", price)
        print("Nice format: ₹{:,.0f}".format(price))

    except:
        print("Invalid input, try again")

    again = input("\nTry again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for using the predictor!")
        break
