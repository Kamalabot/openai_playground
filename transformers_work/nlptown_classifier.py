from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

model = AutoModelForSequenceClassification.from_pretrained(model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name)

pipe_classifier = pipeline("sentiment-analysis",model=model,tokenizer=tokenizer)

out = pipe_classifier("The ways of typing out everything can become very interesting")

print(out)
