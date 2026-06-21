
import json
import difflib

def load_rome_local(filepath="data/rome/rome_metiers.json"):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def score_metier(keyword, label):
    score = difflib.SequenceMatcher(None, keyword, label).ratio()

    if keyword in label:
        score += 0.5

    return score


def filter_metiers(keyword, metiers):
    keyword = keyword.lower()

    scored = [(score_metier(keyword, m["libelle"].lower()), m) for m in metiers]
    scored.sort(reverse=True, key=lambda x: x[0])

    return [m for score, m in scored if score > 0.2]
