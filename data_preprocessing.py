import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    # Example preprocessing, more steps are necessary for a real application
    features = data.drop(columns=['outcome'])
    labels = data['outcome']
    
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    X_train, X_test, y_train, y_test = train_test_split(features_scaled, labels, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
