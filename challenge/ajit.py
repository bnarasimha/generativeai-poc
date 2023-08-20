import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
# Load your dataset (assuming it has columns 'ds' for timestamps and 'y' for values)
# Example dataset:
data = pd.read_csv('../assets/Go_Sales_Stock_Forecast.csv')
# Rename columns to fit the expected format of 'prophet' library
data.rename(columns={'Product': 'ds', 'Stock proposed for next year': 'y'}, inplace=True)
# Initialize and fit the model
model = Prophet()
model.fit(data)
# Create a dataframe for future predictions
future = model.make_future_dataframe(periods=365)  # Forecasting for 365 days into the future
# Generate forecasts
forecast = model.predict(future)
# Plot the forecast
fig = model.plot(forecast)
plt.title('Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()