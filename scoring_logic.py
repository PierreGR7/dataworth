def evaluate_project(inputs):
    score = 0

    mapping = {
        "data_quality": {"low": 0, "medium": 1, "high": 2},
        "goal_clarity": {"vague": -1, "moyenne": 1, "claire": 2},
        "model_complexity": {"simple": 2, "intermédiaire": 1, "complexe": -1},
        "internal_expertise": {"faible": -1, "moyen": 1, "élevé": 2},
        "estimated_business_value": {"faible": 0, "moyenne": 2, "élevée": 4},
        "data_structure": {"désordonnée": -1, "semi-structurée": 1, "bien structurée": 2},
    }

    score += mapping["data_quality"][inputs["data_quality"]]
    score += mapping["goal_clarity"][inputs["goal_clarity"]]
    score += mapping["model_complexity"][inputs["model_complexity"]]
    score += mapping["internal_expertise"][inputs["internal_expertise"]]
    score += mapping["estimated_business_value"][inputs["estimated_business_value"]]
    score += mapping["data_structure"][inputs["data_structure"]]

    # Bonus/Malus selon le volume
    if inputs["volume"] >= 100000:
        score += 2
    elif inputs["volume"] < 1000:
        score -= 2

    # Bonus selon budget
    if inputs["budget"] >= 10000:
        score += 1

    return score
