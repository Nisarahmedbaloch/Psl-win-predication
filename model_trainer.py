import pandas as pd
from sklearn.ensemble import RandomForestClassifier

import joblib

def train_model(filepath):
    df = pd.read_csv(filepath)

    # Clean up column names (remove extra spaces)
    df.columns = df.columns.str.strip()

    # Print cleaned column names to debug
    print("Cleaned Columns:", df.columns.tolist())

    # Define feature and target columns (match your actual CSV)
    feature_cols = ['TEAM  1', 'TEAM  2', 'VENUE', 'TOSS_WINNER', 'BAT FIRST', 'TARGET']
    target_col = 'WIN'

    # Clean values (strip and upper-case for consistency)
    for col in feature_cols:
        if df[col].dtype == object:
            df[col] = df[col].astype(str).str.strip().str.upper()
            df[col] = df[col].astype('category')

    df[target_col] = df[target_col].astype(str).str.strip().str.upper()

    X = df[feature_cols]
    y = df[target_col]

    # Save encoders (mapping category codes back to original)
    encoders = {col: dict(enumerate(X[col].cat.categories)) for col in X.select_dtypes(['category']).columns}

    # Replace categories with codes for model training
    X_encoded = X.apply(lambda col: col.cat.codes if col.dtype.name == 'category' else col)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_encoded, y)

    # Save model and encoders
    joblib.dump(model, 'model.pkl')
    joblib.dump(encoders, 'encoders.pkl')

# Run the training
train_model("E:/excelldata/Pslalldata.csv")
