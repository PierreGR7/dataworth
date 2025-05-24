# Importation des bibliothèques nécessaires
import streamlit as st
from scoring_logic import evaluate_project
from recommendations import get_recommendation, explain_score

# Configuration de la page Streamlit
st.set_page_config(page_title="Data Worth Advisor", page_icon="📊")

# En-tête de l'application
st.title("📊 Data Worth Advisor")
st.markdown("Évaluez la **rentabilité** et la **faisabilité** de vos projets data.")

# Création du formulaire principal pour la saisie des informations du projet
with st.form("project_form"):
    st.header("🔍 Détaillez votre projet")

    # Section 1: Informations sur les données
    data_quality = st.selectbox("Qualité des données", ["low", "medium", "high"])
    goal_clarity = st.selectbox("Clarté des objectifs business", ["vague", "moyenne", "claire"])
    volume = st.number_input("Nombre de lignes de données", min_value=0)
    budget = st.number_input("Budget prévu (€)", min_value=0)

    # Section 2: Informations sur le projet
    model_complexity = st.selectbox("Complexité du modèle envisagé", ["simple", "intermédiaire", "complexe"])
    internal_expertise = st.selectbox("Niveau d'expertise data interne", ["faible", "moyen", "élevé"])
    estimated_business_value = st.selectbox("Valeur potentielle business", ["faible", "moyenne", "élevée"])
    data_structure = st.selectbox("Structuration des données", ["désordonnée", "semi-structurée", "bien structurée"])

    # Bouton de soumission du formulaire
    submitted = st.form_submit_button("Évaluer le projet")

# Traitement des données après soumission du formulaire
if submitted:
    # Création du dictionnaire des entrées
    inputs = {
        "data_quality": data_quality,
        "goal_clarity": goal_clarity,
        "volume": volume,
        "budget": budget,
        "model_complexity": model_complexity,
        "internal_expertise": internal_expertise,
        "estimated_business_value": estimated_business_value,
        "data_structure": data_structure,
    }

    # Évaluation du projet et génération des résultats
    score = evaluate_project(inputs)
    recommendation = get_recommendation(score)
    explanation = explain_score(inputs)

    # Affichage des résultats
    st.subheader("🧮 Score du projet : {}".format(score))
    st.success("✅ " + recommendation)
    st.markdown("### 📋 Analyse détaillée :")
    st.markdown(explanation)
