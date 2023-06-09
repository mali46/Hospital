import spacy 
import pandas as pd


df= pd.read_csv("4.csv",  encoding='ISO-8859-1')
values = df['Reviews'].values

values = map(str, values)
text = ''.join(values)

nlp = spacy.load("en_core_web_sm")



#process
doc = nlp(text=text)

word_dict = {}

for word in doc:
    word = word.text.lower()

    if word in word_dict:
        word_dict[word] +=1
    else:
        word_dict[word] = 1


def find_cost_rating():
    positive = word_dict["expensive"] 
    negative = word_dict["cheap"]
    average = word_dict["affordable"] 

    total = positive + negative + average
    sum = positive*5 + negative*1 + average*3
    print("Cost Rating:")
    print(sum/total)

def find_customer_sat_Rating():
    positive = word_dict["good"] + word_dict["great"] + word_dict["best"] + word_dict["satisfied"]
    negative = word_dict["bad"] + word_dict["worst"] + word_dict["worse"]  + word_dict["disappointed"]
    average = word_dict["okay"]
    

    total = positive + negative 
    sum = positive*5 + negative*1 
    print("Customer Rating:")
    print(sum/total)

find_cost_rating()
find_customer_sat_Rating()


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



