import nltk
import os
import re
from nltk.stem import WordNetLemmatizer
import pandas as pd
import datetime

class DataPrep():
    def __init__(self, data=None):
        self.main_path = os.path.dirname(__file__)
        self.data = None

        if data is None:
            self.data_path = os.path.join(self.main_path, "..", "results", "2019-02-27_trustpilot_reviews.csv")
        else:
            self.data = data
        
        self.stopwords = nltk.corpus.stopwords.words('english')
        self.lemmatizer = WordNetLemmatizer()

    def read_data(self):
        if self.data is None:
            self.data = pd.read_csv(self.data_path, sep=',')

        # drop duplicate reviews
        self.data.drop_duplicates(subset=['Id'], inplace=True)

    def parse_document(self):
        self.dict_sentences = {}
        for _, row in self.data.iterrows():
            id = row['Id']
            document = re.sub('\n', ' ', row['Review'])
            if isinstance(document, str):
                document = document
            else:
                raise ValueError('Document is not string or unicode!')
            document = document.strip()
            sentences = nltk.sent_tokenize(document)
            self.dict_sentences[id] = sentences



if __name__ == "__main__":
    data_prep = DataPrep()
    data_prep.read_data()
    data_prep.parse_document()
    print(data_prep.dict_sentences)
