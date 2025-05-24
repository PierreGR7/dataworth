def get_recommendation(score):
    if score >= 10:
        return "🚀 Projet très prometteur : lancez-vous avec un plan structuré et une équipe solide."
    elif 5 <= score < 10:
        return "🤔 Projet intéressant mais à cadrer davantage. Envisagez une phase de cadrage ou POC pour réduire les risques."
    else:
        return "⚠️ Projet risqué : clarifiez vos objectifs, travaillez vos données et impliquez les parties prenantes avant d'investir."

def explain_score(inputs):
    messages = []

    if inputs["goal_clarity"] == "vague":
        messages.append("🎯 *Les objectifs business sont flous.* Clarifiez ce que vous attendez de ce projet.")
    if inputs["data_quality"] == "low":
        messages.append("🧹 *Les données sont de faible qualité.* Un audit ou nettoyage est essentiel avant toute modélisation.")
    if inputs["model_complexity"] == "complexe" and inputs["internal_expertise"] == "faible":
        messages.append("🧠 *Modèle complexe + faible expertise interne* = haut risque. Optez pour un modèle plus simple ou formez l'équipe.")
    if inputs["estimated_business_value"] == "faible":
        messages.append("📉 *Faible valeur business attendue.* Le projet aura-t-il un impact suffisant ?")
    if inputs["data_structure"] == "désordonnée":
        messages.append("📂 *Données désorganisées.* Structurez-les avant d'envisager une phase d'analyse ou de modélisation.")
    if inputs["budget"] < 2000:
        messages.append("💰 *Budget très limité.* Cela peut restreindre vos choix technologiques ou humains.")
    if inputs["volume"] < 1000:
        messages.append("📊 *Très peu de données.* Envisagez un projet exploratoire plutôt qu’un modèle complexe.")

    if not messages:
        messages.append("✅ *Aucun signal de risque majeur détecté.* Vous êtes sur la bonne voie !")

    return "\n".join(f"- {m}" for m in messages)
