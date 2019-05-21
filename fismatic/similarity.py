import csv
import string
import nltk
from nltk.tokenize import word_tokenize
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

    very_similar = {}
    similar_count = 0
    for base_narrative, d in enumerate(diffs):
        base = desc_lkup[base_narrative]
        for compared_narrative, diff in enumerate(d):
            if diff > 0.8:
                compared_to = desc_lkup[compared_narrative]
                if base != compared_to:
                    output_key = very_similar.setdefault(base, {})
                    output_key.update({compared_to: str(diff)})
                    # TODO don't double-count for both sides of the similarity matrix
                    similar_count += 1

    return very_similar


def write_matrix(desc_lkup, diffs):
    with open("matrix.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([""] + desc_lkup)
        for base_narrative, row_diffs in enumerate(diffs):
            row = [desc_lkup[base_narrative]] + list(row_diffs)
            writer.writerow(row)


def print_similarity(very_similar):
    print("Similar controls:")
    for control, similar_to in very_similar.items():
        print("------- {} -------".format(control))
        keys = list(similar_to.keys())
        print(", ".join(keys))
