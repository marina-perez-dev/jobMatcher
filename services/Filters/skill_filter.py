def set_compatibility_between_skills(listSkills, personal_skill_codes):

    if not listSkills:
        return 0, []

    offer_codes = {skill["code"] for skill in listSkills}

    common = offer_codes & personal_skill_codes

    # Protection division par zéro
    if len(offer_codes) == 0:
        return 0, []

    percent = (len(common) / len(offer_codes)) * 100
    weight_bonus = len(common) * 2
    final_score = percent + weight_bonus

    return final_score, list(common)