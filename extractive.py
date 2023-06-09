import spacy 
import pandas as pd


df= pd.read_csv("reviews.csv",  encoding='ISO-8859-1')
values = df['Review'].values

values = map(str, values)

nlp = spacy.load("en_core_web_sm")

text = ''.join(values)

#process
doc = nlp(text=text)

word_dict = {}

for word in doc:
    word = word.text.lower()

    if word in word_dict:
        word_dict[word] +=1
    else:
        word_dict[word] = 1





sentences = []
sentence_score = 0

for i, sentence in enumerate(doc.sents):
    for word in sentence:
        word = word.text.lower()
        sentence_score =+ word_dict[word]

    sentences.append((i,sentence.text.replace("\n",""), sentence_score/len(sentence)))



#sort
sorted_sentences = sorted(sentences, key=lambda x: -x[2])
top_5 = sorted(sorted_sentences[:5], key = lambda x:x[0])

summary_text = ""

for sentence in top_5:
    summary_text += sentence[1] + ""


print(summary_text)
