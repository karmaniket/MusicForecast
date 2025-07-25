<h1 align="center">Music Forecast</h1>

**MusicForecast** is developed to predict the popularity of songs based on their attributes, such as tempo, duration, genre and release year. The project uses a dataset of real-world songs and applies various machine learning techniques to train a predictive model.

## Features

- **Dataset Generation**: A dataset of songs is created with attributes like artist, title, genre, tempo, duration and popularity
- **Data Preprocessing**: Includes handling missing values, feature engineering (one-hot encoding genres, creating decade-based features), and scaling numerical features
- **Model Training**: Compares multiple machine learning models (Linear Regression, Random Forest, SVR) to find the best-performing model
- **Hyperparameter Tuning**: Optimizes the model using GridSearchCV
- **Visualization**: Generates visualizations for data distribution, feature importance, correlation matrix, learning curves and residual analysis
- **Prediction**: Provides a function to predict the popularity of new songs based on their attributes

## Visualizations

<table><tr><td>
      <h3 align="center">Heatmap of feature correlations matrix</h3>
      <i>Shows the correlation coefficients between numerical features. Highlights relationships between features, helping to identify multicollinearity or key predictors of popularity.</i><br><br>
      <img width="auto" src="assets/correlation_matrix.png">
    </td><td>
      <h3 align="center">Bar plot of feature importance</h3>
      <i>A bar plot of the top 15 features ranked by their coefficients (for linear models) or importance scores (for tree-based models). Highlights the most influential features in the model.</i><br><br>
      <img width="auto" src="assets/Feature_importance.png">  </td>
  </tr>
    <tr><td>
      <h3 align="center">Learning curve of the best model</h3>
      <i>A line plot showing the training and cross-validation R² scores as the training size increases. Evaluates the model's learning behavior, helping to detect underfitting or overfitting.</i><br><br>
      <img width="auto" src="assets/learning_curve.png">
    </td><td>
      <h3 align="center">Popularity distribution</h3>
      <i>A histogram showing the distribution of song popularity scores in the dataset. Helps visualize how popularity values are spread, identify patterns and detect outliers or imbalances.</i><br><br>
      <img width="auto" src="assets/popularity_distribution.png">
    </td></tr>
</table>
<h3 align="center">Residual Analysis</h3>
      <i> 1. Residual Plot: A scatter plot of predicted values vs. residuals, with a horizontal line at zero. <br>
          2. Residual Distribution: A histogram with a kernel density estimate (KDE) showing the distribution of residuals. <br>
          3. Residual Analysis: Evaluates the model's prediction errors, checking for patterns or biases in residuals.</i><br><br>
      <img width="auto" src="assets/Residual_analysis.png">

## Project Structure

```bash
.
├── dataframe.py                # Script to generate the dataset
├── music_dataset.csv           # Generated dataset
├── model-training.py           # Script to train the model and generate visualizations
├── model.pkl
├── scaler.pkl
├── feature.pkl
├── predict.py                  # Script to predict the popularity of new songs
├── assets/                     # Generated plots and results
├── requirements.txt            # Required libraries
```

## Setup

### 1. Clone the repository

```bash
    git clone https://github.com/karmaniket/MusicForecast.git
    cd MusicForecast
```

### 2. Create & Activate virtual environment

```bash
    python -m venv venv
    venv\Scripts\activate.bat  
```

> [!IMPORTANT]
> Python 3.8 - 3.12

### 3. Install dependencies

```bash
    pip freeze > requirements.txt
    pip install -r requirements.txt
    #or
    pip install pandas numpy matplotlib seaborn scikit-learn
```

### 4. Running the Project

Run `dataframe.py` to generate the `.csv` file

```bash
  python dataframe.py
```

Run `model-training.py` to train the `model`, generate `visualizations` and `.pkl` files

```bash
  python model-training.py
```

Run `predict.py` to predict the popularity of new song

```bash
  python predict.py
```

To predict the popularity of a new song, modify the `predict_pplrt` dictionary in `predict.py` with the song's attributes

```python
  predict_pplrt = {
    'tempo': 120,
    'duration': 180,
    'year': 2030,
    'genre': 'pop'
  }
```

### 5. Data Splitting

> [!Note]
> The training and testing split can be configured prior to creating the `.pkl` files.
This project uses `80:20 train_test_split` ratio, with consistent results due to the fixed `random_state`.

```python
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

## Results & Future Improvements

- The best-performing model is selected based on metrics like R², MAE, MSE, and RMSE
- Hyperparameter tuning ensures optimal model performance
- Visualizations provide insights into the dataset and model behavior
- Add more features to improve prediction accuracy
- Experiment with additional machine learning algorithms
- Incorporate deep learning models for better performance

## License

This project is licensed under the MIT License. Feel free to use, modify and distribute with attribution.
