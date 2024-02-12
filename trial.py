from ast import dump
import json
import os
#from keybert import KeyBERT


embeddings_model_name = "all-MiniLM-L6-v2"
#kw_model = KeyBERT(model = embeddings_model_name)

text_to_be_ingested = []
list_of_files = os.listdir("BrownBag/data/ingestion/")
print(list_of_files)
id = 1

for file in list_of_files[2:]:
    content = ""
    with open("BrownBag/data/ingestion/"+file, encoding="utf8") as f_in:
        for line in f_in:
            if not line.isspace():
                content += line
    #keywords = kw_model.exteact_keywords(f.read(), keyphrase_ngram_range =(1,2), stop_words = 'english')
    #print(keywords,"\n")

    d = {}
    d["id"] = id
    d["content"] = content.replace('\n','. ')
    d["contentUrls"] = file[:-4]
    d["imageUrls"] = 'image'
    d["type"] = file[-4:]
    d["filePath"] = os.path.abspath(file)
    d["chunckSize"] = 9
    d["tags"] = 'key'

    text_to_be_ingested.append(d)
    id = id + 1

with open("text_to_be_ingested.json","w") as outfile:
    json.dump(text_to_be_ingested, outfile )