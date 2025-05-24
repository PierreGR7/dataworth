import streamlit as st
from scoring_logic import evaluate_project
from recommendations import get_recommendation, explain_score

st.set_page_config(page_title="Data Worth Advisor", page_icon="📊")
st.title("📊 Data Worth Advisor")
st.markdown("Évaluez la **rentabilité** et la **faisabilité** de vos projets data à l’aide de l’IA.")

with st.form("project_form"):
    st.header("🔍 Détaillez votre projet")

    data_quality = st.radio("Qualité des données :", ["low", "medium", "high"])
    goal_clarity = st.radio("Clarté des objectifs business :", ["vague", "moyenne", "claire"])
    model_complexity = st.selectbox("Complexité du modèle :", ["simple", "intermédiaire", "complexe"])
    internal_expertise = st.radio("Expertise data interne :", ["faible", "moyen", "élevé"])
    estimated_business_value = st.selectbox("Valeur business attendue :", ["faible", "moyenne", "élevée"])
    data_structure = st.radio("Structuration des données :", ["désordonnée", "semi-structurée", "bien structurée"])
    volume = st.slider("Volume de données (lignes)", 0, 1000000, step=5000, value=10000)
    budget = st.number_input("Budget disponible (€)", min_value=0, value=10000, step=100)

    submitted = st.form_submit_button("⚙️ Évaluer le projet")

if submitted:
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

    score = evaluate_project(inputs)
    recommendation = get_recommendation(score)
    explanation = explain_score(inputs)

    st.subheader(f"🧮 Score du projet : {score}")
    st.success("✅ " + recommendation)
    st.markdown("### 📋 Analyse détaillée :")
    st.markdown(explanation)
