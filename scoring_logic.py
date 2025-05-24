from model_loader import load_model

def evaluate_project(inputs):
    model = load_model()

    # Formatage des données en DataFrame
    import pandas as pd
    input_df = pd.DataFrame([inputs])

    # Prédiction du score
    score = model.predict(input_df)[0]
    return round(score, 2)
