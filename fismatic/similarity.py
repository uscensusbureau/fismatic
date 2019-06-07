import numpy as np
import pandas as pd
import spacy

# lazy-load the model
# https://stackoverflow.com/a/7152065/358804
class LazyNLP:
    def __init__(self):
        self.nlp = None

    def __call__(self, *args, **kwargs):
        if not self.nlp:
            self.nlp = spacy.load("en_core_web_lg")
        return self.nlp(*args, **kwargs)


nlp = LazyNLP()


def generate_diffs(docs):
    """Expects an iterable of spaCy Docs. Returns the similarity scores between controls."""
    results = [[doc1.similarity(doc2) for doc2 in docs] for doc1 in docs]
    return np.array(results)


def generate_diffs_with_labels(implementations_by_id):
    """Returns a Pandas DataFrame of the similarity scores between controls."""
    implementations = implementations_by_id.values()
    desc_lkup = implementations_by_id.keys()
    matrix = generate_diffs(implementations)
    return pd.DataFrame(matrix, index=desc_lkup, columns=desc_lkup)


def similar_controls(diffs, threshold=0.9):
    """Find all control narratives which are identical or very similar (greater than the provided number)."""
    # exclude the controls matching themselves
    np.fill_diagonal(diffs.values, np.nan)

    return {
        control_name: similarities[similarities > threshold].to_dict()
        for control_name, similarities in diffs.iteritems()
    }
