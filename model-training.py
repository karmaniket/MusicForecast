import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, learning_curve, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import pickle
import os

try:
    data_path = 'music_dataset.csv'
    df = pd.read_csv(data_path)
    
    print(f"Dataset shape: {df.shape}")
    print("\nDataset Info:")
    print(df.info())
    print("\nDataset Statistics:")
    print(df.describe())
    duplicates = df.duplicated().sum()
    print(f"\nNumber of duplicate records: {duplicates}")
    
    plt.figure(figsize=(10, 5))
    sns.histplot(df['popularity'])
    plt.title('Distribution of Popularity Scores')
    plt.savefig('assets\popularity_distribution.png')
    plt.close()
    
    initial_rows = df.shape[0]
    df.dropna(inplace=True)
    print(f"\nRemoved {initial_rows - df.shape[0]} rows with missing values")
    
    # new features
    df['duration_minutes'] = df['duration'] / 60
    if 'year' in df.columns:
        df['year_decade'] = (df['year'] // 10) * 10
    
    # One-hot encode categorical features
    df = pd.get_dummies(df, columns=['genre'])
    
    scaler = StandardScaler()
    numerical_features = ['tempo', 'duration', 'year'] if 'year' in df.columns else ['tempo', 'duration']
    df[numerical_features] = scaler.fit_transform(df[numerical_features])
    
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    
    numeric_df = df.select_dtypes(include=[np.number])
    plt.figure(figsize=(10, 5))
    sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Feature Correlation Matrix')
    plt.tight_layout()
    plt.savefig('assets\correlation_matrix.png')
    plt.close()
    
    X = numeric_df.drop(columns=['popularity'])
    y = numeric_df['popularity']
    
    with open('feature.pkl', 'wb') as f:
        pickle.dump(list(X.columns), f)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("\n=== Model Comparison ===")
    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(random_state=42),
        'SVR': SVR()
    }
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        
        results[name] = {
            'r2': r2,
            'mae': mae,
            'mse': mse,
            'rmse': rmse
        }
        print(f"{name}:")
        print(f"  R²: {r2:.4f}")
        print(f"  MAE: {mae:.4f}")
        print(f"  MSE: {mse:.4f}")
        print(f"  RMSE: {rmse:.4f}")
    
    # CV
    print("\n=== Cross-Validation for Linear Regression ===")
    lin_reg = LinearRegression()
    cv_scores = cross_val_score(lin_reg, X, y, cv=5, scoring='r2')
    print(f"CV R² scores: {cv_scores}")
    print(f"Mean CV R² score: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")
    
    # HP tuning
    print("\n=== Hyperparameter Tuning for Linear Regression ===")
    param_grid = {
        'fit_intercept': [True, False],
        'copy_X': [True, False],
        'positive': [True, False]
    }
    grid_search = GridSearchCV(LinearRegression(), param_grid, cv=5, scoring='r2')
    grid_search.fit(X_train, y_train)
    
    print(f"Best parameters: {grid_search.best_params_}")
    
    best_model = grid_search.best_estimator_
    best_model.fit(X_train, y_train)
    
    y_pred_best = best_model.predict(X_test)
    
    mae_best = mean_absolute_error(y_test, y_pred_best)
    mse_best = mean_squared_error(y_test, y_pred_best)
    rmse_best = np.sqrt(mse_best)
    r2_best = r2_score(y_test, y_pred_best)
    
    print("\n=== Best Model Performance ===")
    print(f"R²: {r2_best:.4f}")
    print(f"MAE: {mae_best:.4f}")
    print(f"MSE: {mse_best:.4f}")
    print(f"RMSE: {rmse_best:.4f}")
    
    # Learning curve
    train_sizes, train_scores, test_scores = learning_curve(
        best_model, X, y, cv=5, scoring='r2', train_sizes=np.linspace(0.1, 1.0, 10))
    
    plt.figure(figsize=(10, 5))
    plt.plot(train_sizes, train_scores.mean(axis=1), 'o-', label='Training score')
    plt.plot(train_sizes, test_scores.mean(axis=1), 'o-', label='Cross-validation score')
    plt.xlabel('Training examples')
    plt.ylabel('R² Score')
    plt.title('Learning Curve')
    plt.legend()
    plt.savefig('assets\learning_curve.png')
    plt.close()
    
    coef_df = pd.DataFrame({
        'Feature': X.columns,
        'Coefficient': best_model.coef_
    })
    coef_df = coef_df.sort_values('Coefficient', key=abs, ascending=False)
    
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Coefficient', y='Feature', data=coef_df.head(15))
    plt.title('Top 15 Feature Coefficients')
    plt.tight_layout()
    plt.savefig('assets\Feature_importance.png')
    plt.close()
    
    residuals = y_test - y_pred_best
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.scatter(y_pred_best, residuals)
    plt.axhline(y=0, color='r', linestyle='-')
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.title('Residual Plot')
    
    plt.subplot(1, 2, 2)
    sns.histplot(residuals, kde=True)
    plt.title('Distribution of Residuals')
    plt.tight_layout()
    plt.savefig('assets\Residual_analysis.png')
    plt.close()
    
    with open('model.pkl', 'wb') as f:
        pickle.dump(best_model, f)
    
    def predict_popularity(model_path, scaler_path, feature_path, new_data):
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        
        with open(scaler_path, 'rb') as f:
            scaler = pickle.load(f)
        
        with open(feature_path, 'rb') as f:
            feature = pickle.load(f)

        df_pred = pd.DataFrame([new_data])
        
        if 'genre' in df_pred.columns:
            genre_col = f"genre_{new_data['genre']}"
            for feature in feature:
                if feature.startswith('genre_'):
                    if feature == genre_col:
                        df_pred[feature] = 1
                    else:
                        df_pred[feature] = 0
            
            df_pred.drop('genre', axis=1, inplace=True)
        
        if 'year' in df_pred.columns and 'year_decade' in feature:
            df_pred['year_decade'] = (df_pred['year'] // 10) * 10
        
        if 'duration' in df_pred.columns and 'duration_minutes' in feature:
            df_pred['duration_minutes'] = df_pred['duration'] / 60
        
        numerical_features = ['tempo', 'duration', 'year'] if 'year' in df_pred.columns else ['tempo', 'duration']
        if set(numerical_features).issubset(df_pred.columns):
            df_pred[numerical_features] = scaler.transform(df_pred[numerical_features])

        df_pred = df_pred.reindex(columns=feature, fill_value=0)
        
        return model.predict(df_pred)[0]
    
    print("\n=== Example Prediction ===")
    with open('model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    
    example_data = X_test.iloc[0].values.reshape(1, -1)
    predicted_popularity = loaded_model.predict(example_data)
    actual_popularity = y_test.iloc[0]
    
    print(f"Predicted popularity: {predicted_popularity[0]:.2f}")
    print(f"Actual popularity: {actual_popularity:.2f}")
    print(f"Difference: {abs(predicted_popularity[0] - actual_popularity):.2f}")
    
    print("\nAnalysis completed successfully!")
    print("Saved artifacts: model.pkl, scaler.pkl, feature.pkl")
    print("Saved visualizations: correlation_matrix.png, feature_importance.png, learning_curve.png, residual_analysis.png")
    print("Saved prediction script: predict.py")

except Exception as e:
    print(f"Error occurred: {str(e)}")