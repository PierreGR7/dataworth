import pandas as pd
from itertools import product
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib

# === Dictionnaires de valeurs possibles === #
options = {
    "data_quality": ["low", "medium", "high"],
    "goal_clarity": ["vague", "moyenne", "claire"],
    "volume": [500, 5000, 50000, 100000, 200000],
    "budget": [1000, 5000, 10000, 20000],
    "model_complexity": ["simple", "intermédiaire", "complexe"],
    "internal_expertise": ["faible", "moyen", "élevé"],
    "estimated_business_value": ["faible", "moyenne", "élevée"],
    "data_structure": ["désordonnée", "semi-structurée", "bien structurée"]
}

# === Fonction de score manuelle (baseline) === #
def compute_score(input_dict):
    mapping = {
        "data_quality": {"low": 0, "medium": 1, "high": 2},
        "goal_clarity": {"vague": -1, "moyenne": 1, "claire": 2},
        "model_complexity": {"simple": 2, "intermédiaire": 1, "complexe": -1},
        "internal_expertise": {"faible": -1, "moyen": 1, "élevé": 2},
        "estimated_business_value": {"faible": 0, "moyenne": 2, "élevée": 4},
        "data_structure": {"désordonnée": -1, "semi-structurée": 1, "bien structurée": 2},
    }

    score = 0
    score += mapping["data_quality"][input_dict["data_quality"]]
    score += mapping["goal_clarity"][input_dict["goal_clarity"]]
    score += mapping["model_complexity"][input_dict["model_complexity"]]
    score += mapping["internal_expertise"][input_dict["internal_expertise"]]
    score += mapping["estimated_business_value"][input_dict["estimated_business_value"]]
    score += mapping["data_structure"][input_dict["data_structure"]]

    if input_dict["volume"] >= 100000:
        score += 2
    elif input_dict["volume"] < 1000:
        score -= 2

    if input_dict["budget"] >= 10000:
        score += 1

    return score

# === Génération de données d'entraînement === #
records = []
for comb in product(*options.values()):
    entry = dict(zip(options.keys(), comb))
    entry["score"] = compute_score(entry)
    records.append(entry)

df = pd.DataFrame(records)

# === Séparation données === #
X = df.drop("score", axis=1)
y = df["score"]

# === Prétraitement + modèle === #
categorical_cols = [col for col in X.columns if X[col].dtype == "object"]
numeric_cols = ["volume", "budget"]

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
    ("num", "passthrough", numeric_cols)
])

pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

# === Entraînement === #
pipeline.fit(X, y)

# === Sauvegarde === #
joblib.dump(pipeline, "dataworth_model.joblib")
print("✅ Modèle sauvegardé sous 'dataworth_model.joblib'")
