from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import pandas as pd

tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")


df= pd.read_csv("reviews.csv",  encoding='ISO-8859-1')
values = df['Review'].values

values = map(str, values)
text = ''.join(values)

tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")

summary = model.generate(**tokens)
print(tokenizer.decode(summary[0]))