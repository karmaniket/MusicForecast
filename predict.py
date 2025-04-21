import pickle
import pandas as pd

def predict_popularity(model_path, scaler_path, feature_path, new_data):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
    
    with open(feature_path, 'rb') as f:
        features = pickle.load(f)
    
    df_pred = pd.DataFrame([new_data])
    
    # One-hot encode genre
    if 'genre' in df_pred.columns:
        genre_col = f"genre_{new_data['genre']}"
        for feat in features:
            if feat.startswith('genre_'):
                if feat == genre_col:
                    df_pred[feat] = 1
                else:
                    df_pred[feat] = 0
        
        df_pred.drop('genre', axis=1, inplace=True)
    
    if 'year' in df_pred.columns and 'year_decade' in features:
        df_pred['year_decade'] = (df_pred['year'] // 10) * 10
    
    if 'duration' in df_pred.columns and 'duration_minutes' in features:
        df_pred['duration_minutes'] = df_pred['duration'] / 60
    
    numerical_features = ['tempo', 'duration', 'year'] if 'year' in df_pred.columns else ['tempo', 'duration']
    if set(numerical_features).issubset(df_pred.columns):
        df_pred[numerical_features] = scaler.transform(df_pred[numerical_features])

    df_pred = df_pred.reindex(columns=features, fill_value=0)
    
    return model.predict(df_pred)[0]

# Predict popularity of new song
if __name__ == "__main__":
    predict_pplrt = {
        'tempo': 120,       # Beat speed
        'duration': 180,    # Length in seconds
        'year': 2030,       # Release year
        'genre': 'pop'     # Music genre
    }
    try:
        prediction = predict_popularity(
            'model.pkl',
            'scaler.pkl',
            'feature.pkl',
            predict_pplrt
        )
        print(f"Predicted popularity: {prediction:.2f}")
    except Exception as e:
        print(f"Error occurred during prediction: {str(e)}")