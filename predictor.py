import joblib
import numpy as np
import pandas as pd

model = joblib.load('model.pkl')
encoders = joblib.load('encoders.pkl')

# Normalize encoder keys
encoders = {k.strip().upper(): {v.strip().upper(): k for k, v in d.items()} for k, d in encoders.items()}

def encode_input(input_dict):
    encoded = []
    for col, val in input_dict.items():
        col_upper = col.strip().upper()
        if col_upper in encoders:
            val_upper = val.strip().upper()
            if val_upper not in encoders[col_upper]:
                raise ValueError(f"Value '{val}' not found in encoder for '{col}'")
            encoded.append(encoders[col_upper][val_upper])
        else:
            encoded.append(val)  # for numeric fields like TARGET
    return np.array(encoded).reshape(1, -1)
def predict_winner(input_dict):
    # Encode input
    X = encode_input(input_dict)

    # Load model
    model = joblib.load('model.pkl')

    # Predict probabilities
    probabilities = model.predict_proba(X)[0]
    classes = model.classes_

    # Build dictionary of team: probability
    prediction_result = {cls: prob for cls, prob in zip(classes, probabilities)}
    team1 = input_dict["TEAM  1"]
    team2 = input_dict["TEAM  2"]

    # Filter to only the two selected teams
    filtered_result = {
        team: prob for team, prob in prediction_result.items()
        if team in [team1, team2]
    }

    # Normalize to make the total = 100%
    total = sum(filtered_result.values())
    normalized_result = {team: prob / total for team, prob in filtered_result.items()}

    return normalized_result
