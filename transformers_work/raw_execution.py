from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

tokenizer = AutoTokenizer.from_pretrained(model_name)

text = "this is steadily becoming very interesting"

print(tokenizer(text))

pt_batch = tokenizer(
    ["We are very happy to show you the 🤗 Transformers library.", "We hope you don't hate it."],
    padding=True,
    truncation=True,
    max_length=512,
    return_tensors="pt",
)

#print(**pt_batch)

pt_model = AutoModelForSequenceClassification.from_pretrained(model_name)


print(pt_model(**pt_batch))


from torch import nn

pt_pred = nn.functional.softmax(pt_model(**pt_batch).logits,dim =-1)

print(pt_pred)
