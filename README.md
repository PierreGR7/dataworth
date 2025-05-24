# 📊 DataWorth

Un mini-SaaS en Python qui aide à **évaluer la pertinence d’un projet data** avant d’y investir temps et budget.

---

## Fonctionnalités

- Interface Streamlit simple et intuitive
- Évaluation basée sur :
  - Qualité des données
  - Clarté des objectifs business
  - Complexité du modèle
  - Expertise interne
  - Structuration des données
  - Volume de données
  - Budget
  - Valeur business potentielle
- Score global + recommandations
- Analyse détaillée des forces et faiblesses du projet

---

## Lancer l'application en local

```bash
git clone https://github.com/ton-repo/dataworth.git
cd dataworth
pip install -r requirements.txt
python3 train_model.py
streamlit run app.py
