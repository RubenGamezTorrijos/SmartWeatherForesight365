from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

class TrainingModel:
    def __init__(self):
        self.model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )
    
    def train_model(self, dataset: tuple):
        """
        Train the prediction model using historical data
        """
        try:
            X, y = dataset
            
            # Split dataset
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Train model
            self.model.fit(X_train, y_train)
            
            # Save model
            self._save_model()
            
            return self.model
            
        except Exception as e:
            raise Exception(f"Error en el entrenamiento del modelo: {str(e)}")
    
    def _save_model(self):
        """Save trained model"""
        os.makedirs("models", exist_ok=True)
        joblib.dump(self.model, "models/weather_model.joblib")