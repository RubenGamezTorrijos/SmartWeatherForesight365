import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

class DatasetModel:
    def __init__(self):
        self.scaler = StandardScaler()
    
    def prepare_dataset(self, city: str) -> tuple:
        """
        Prepare dataset for training
        """
        try:
            # Load historical data
            data = pd.read_csv(f"datasets/{city.lower()}_historical_weather.csv")
            
            # Prepare features and target
            features = ['temp', 'dwpt', 'rhum', 'prcp', 'wdir', 'wspd']
            X = data[features]
            y = data['temp'].shift(-1)  # Next day temperature as target
            
            # Remove last row (NaN target)
            X = X[:-1]
            y = y[:-1]
            
            # Scale features
            X_scaled = self.scaler.fit_transform(X)
            
            return X_scaled, y
            
        except Exception as e:
            raise Exception(f"Error al preparar el dataset: {str(e)}")