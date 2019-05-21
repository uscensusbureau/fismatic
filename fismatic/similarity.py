import csv
import string
import gensim
from nltk.tokenize import word_tokenize


def get_gen_doc(text):
    """Returns an array of tokenized terms."""
    return [w.lower() for w in word_tokenize(text) if w not in string.punctuation]


def get_gen_docs(all_desc):
    """Returns an array of arrays of tokenized terms."""
    return [get_gen_doc(text) for text in all_desc]


def generate_diffs(all_desc):
    gen_docs = get_gen_docs(all_desc)

    dictionary = gensim.corpora.Dictionary(gen_docs)
    # print("Number of words in dictionary:", len(dictionary))
    # for i in range(len(dictionary)):
    #     print(i, dictionary[i])

    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    tf_idf = gensim.models.TfidfModel(corpus)

    sims = gensim.similarities.Similarity(
        "./", tf_idf[corpus], num_features=len(dictionary)
    )

    index = gensim.similarities.MatrixSimilarity(tf_idf[corpus])
    index.save("ssp.index")
    diffs = []

    for i, sims in enumerate(index):
        diffs.append([])
        sims = sorted(enumerate(sims), key=lambda item: item[0])
        for k, d in sims:
            diffs[i].append(d)

    return diffs


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
        for base_narrative, d in enumerate(diffs):
            row = [desc_lkup[base_narrative]] + d
            writer.writerow(row)


def print_similarity(very_similar):
    print("Similar controls:")
    for control, similar_to in very_similar.items():
        print("------- {} -------".format(control))
        keys = list(similar_to.keys())
        print(", ".join(keys))
