from transformers import pipeline 

classifier = pipeline("sentiment-analysis")

out = classifier("I am happy to work on bit powerful machine")
print(out)

