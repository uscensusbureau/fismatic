import string
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def tokenize(text):
    """Returns an array of tokenized terms."""
    return [w.lower() for w in word_tokenize(text) if w not in string.punctuation]


TfidfVec = TfidfVectorizer(tokenizer=tokenize)


def generate_diffs(all_desc):
    """Returns the similarity scores between controls."""
    # Part f of
    # https://sites.temple.edu/tudsc/2017/03/30/measuring-similarity-between-texts-in-python/
    tfidf = TfidfVec.fit_transform(all_desc)
    return (tfidf * tfidf.T).toarray()


def generate_diffs_with_labels(implementations_by_id):
    """Returns a Pandas DataFrame of the similarity scores between controls."""
    all_desc = implementations_by_id.values()
    desc_lkup = implementations_by_id.keys()
    matrix = generate_diffs(all_desc)
    return pd.DataFrame(matrix, index=desc_lkup, columns=desc_lkup)


def similar_controls(diffs, threshold=0.8):
    """Find all control narratives which are identical or very similar (greater than the provided number)."""
    # exclude the controls matching themselves
    np.fill_diagonal(diffs.values, np.nan)

    return {
        control_name: similarities[similarities > threshold].to_dict()
        for control_name, similarities in diffs.iteritems()
    }


def write_matrix(diffs, filename="matrix.csv"):
    # https://stackoverflow.com/a/11146434/358804
    diffs.to_csv(filename, index=True, header=True)


def print_similarity(very_similar):
    print("Similar controls:")
    for control, similar_to in very_similar.items():
        if similar_to:
            print(control)
            for other_control, value in similar_to.items():
                print("  - {} ({:.0%})".format(other_control, value))
