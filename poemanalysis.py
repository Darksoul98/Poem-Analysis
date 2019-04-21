import pandas as pd
import poetrytools
import csv


def analysis(x):
    print(len(temp_form))
    print(type(x))
    poem = poetrytools.tokenize(x)
    temp_form.append(poetrytools.guess_form(poem, verbose=False))
    temp_metre.append(poetrytools.guess_metre(poem)[3])
    temp_rhyme.append(poetrytools.guess_rhyme_type(poem)[1])
    temp_stanza_type.append(poetrytools.guess_stanza_type(poem)[1])


temp_form = []
temp_metre = []
temp_rhyme = []
temp_stanza_type = []
df = pd.read_csv("all.csv")
df["content"].apply(lambda x: analysis(x))
df["analysis_form"] = temp_form
df["analysis_metre"] = temp_metre
df["analysis_rhyme"] = temp_rhyme
df["analysis_stanza"] = temp_stanza_type
df.to_csv("all_edit.csv", index=False)

