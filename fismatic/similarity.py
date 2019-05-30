import numpy as np
import pandas as pd
import spacy


nlp = spacy.load("en_core_web_lg")


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
