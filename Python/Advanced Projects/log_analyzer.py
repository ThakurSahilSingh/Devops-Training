import spacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")
with open("/var/log/syslog", "r") as file:
 logs = file.readlines()
log_text = " ".join(logs)
doc = nlp(log_text)
error_counts = Counter(token.text for token in doc if token.text.lower() in
["error", "failed", "critical"])
print("Frequent Log Errors:", error_counts)
