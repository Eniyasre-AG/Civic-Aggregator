import spacy
from sklearn.cluster import DBSCAN
import numpy as np

nlp = spacy.load("en_core_web_sm")

def classify_text(text):
    text = text.lower()
    if "garbage" in text:
        return "Garbage"
    elif "pothole" in text:
        return "Pothole"
    elif "light" in text or "lamp" in text:
        return "Streetlight"
    elif "leak" in text or "clog" in text or "block" in text:
        return "Water Clog"
    else:
        return "Other"


def cluster_issues(issues):
    coords = [(i.latitude, i.longitude) for i in issues if i.latitude and i.longitude]
    if not coords:
        return issues

    model = DBSCAN(eps=0.01, min_samples=2)
    labels = model.fit_predict(np.array(coords))

    for i, issue in enumerate(issues):
        if issue.latitude and issue.longitude:
            issue.cluster_id = int(labels[i])
    return issues
