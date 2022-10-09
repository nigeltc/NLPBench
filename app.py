"""
NLP WorkBench
"""
from flask import Flask
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")


@app.route("/")
def index():
    doc = nlp(
        """Shares of Advanced Micro Devices, Inc. hit new 52-week lows on Friday after the company came out with lower third-quarter guidance Thursday after the market close."""
    )
    s = "<ul>"
    for ent in doc.ents:
        s += f"<li>{ent.text} [{ent.label_}]</li>"
    s += "</ul>"
    return s
