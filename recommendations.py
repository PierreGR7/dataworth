def get_recommendation(score):
    if score >= 10:
        return "Projet très prometteur : lancez-vous avec un plan structuré !"
    elif 5 <= score < 10:
        return "Projet intéressant mais à cadrer davantage. Recommandé : une phase de cadrage ou POC."
    else:
        return "Projet risqué : clarifiez vos objectifs et renforcez vos données avant d'investir."

def explain_score(inputs):
    msg = ""

    if inputs["goal_clarity"] == "vague":
        msg += "- 🎯 Les objectifs business sont flous. Clarifiez ce que vous attendez de ce projet.\n"
    if inputs["data_quality"] == "low":
        msg += "- 🧹 Vos données sont de mauvaise qualité. Envisagez un nettoyage ou audit avant modélisation.\n"
    if inputs["model_complexity"] == "complexe" and inputs["internal_expertise"] == "faible":
        msg += "- ⚠️ Attention : modèle complexe avec peu d’expertise en interne = risque élevé.\n"
    if inputs["estimated_business_value"] == "faible":
        msg += "- 📉 La valeur business potentielle semble faible : ce projet vaut-il le coup ?\n"
    if inputs["data_structure"] == "désordonnée":
        msg += "- 📂 Vos données sont désorganisées. Structurez-les avant de faire du ML.\n"
    if msg == "":
        msg = "- ✅ Aucun risque majeur détecté. Vous êtes sur la bonne voie !"

    return msg
