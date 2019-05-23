import string
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("punkt")


def get_gen_doc(text):
    """Returns an array of tokenized terms."""
    return [w.lower() for w in word_tokenize(text) if w not in string.punctuation]


TfidfVec = TfidfVectorizer(tokenizer=get_gen_doc)


def generate_diffs(all_desc):
    # Part f of
    # https://sites.temple.edu/tudsc/2017/03/30/measuring-similarity-between-texts-in-python/
    tfidf = TfidfVec.fit_transform(all_desc)
    return (tfidf * tfidf.T).toarray()


def similar_controls(desc_lkup, diffs):
    """Find all control narratives which are identical or very similar (>0.8)."""

    df = pd.DataFrame(diffs, index=desc_lkup, columns=desc_lkup)
    # exclude the controls matching themselves
    np.fill_diagonal(df.values, np.nan)

    return {
        control_name: similarities[similarities > 0.8].to_dict()
        for control_name, similarities in df.iteritems()
    }


def write_matrix(desc_lkup, diffs):
    # https://stackoverflow.com/a/11146434/358804
    df = pd.DataFrame(diffs, index=desc_lkup, columns=desc_lkup)
    df.to_csv("matrix.csv", index=True, header=True)


def print_similarity(very_similar):
    print("Similar controls:")
    for control, similar_to in very_similar.items():
        if similar_to:
            print("------- {} -------".format(control))
            keys = list(similar_to.keys())
            print(", ".join(keys))
