
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from pathlib import Path


def predict_ml_ppa(features):
    """
    Train a Random Forest model on the generated RTL dataset
    and predict PPA for the uploaded RTL design.
    """

    # Find the project folder
    project_root = Path(__file__).resolve().parent.parent

    # Load dataset
    dataset_path = project_root / "data" / "ppa_dataset.csv"

    df = pd.read_csv(dataset_path)

    # Input features
    feature_columns = [
        "modules",
        "inputs",
        "outputs",
        "registers",
        "always_blocks",
        "case_statements",
        "adders",
        "subtractors",
        "and_operations",
        "or_operations"
    ]

    # Target PPA values
    target_columns = [
        "estimated_area",
        "estimated_power",
        "estimated_performance"
    ]

    X = df[feature_columns]
    y = df[target_columns]

    # Train ML model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    # Convert uploaded RTL features into one row
    input_data = pd.DataFrame(
        [[features[col] for col in feature_columns]],
        columns=feature_columns
    )

    # Predict PPA
    prediction = model.predict(input_data)[0]

    return {
        "ml_area": round(prediction[0], 2),
        "ml_power": round(prediction[1], 2),
        "ml_performance": round(prediction[2], 2)
    }