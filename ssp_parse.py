import csv
import string
import sys

import gensim
import nltk
from docx import Document
from docx.document import Document as _Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table, _Cell
from docx.text.paragraph import Paragraph
from nltk.tokenize import word_tokenize

nltk.download("punkt")


def iter_block_items(parent):
    """
    Parsing table structure from .docx

    Generate a reference to each paragraph and table child within *parent*,
    in document order. Each returned value is an instance of either Table or
    Paragraph. *parent* would most commonly be a reference to a main
    Document object, but also works for a _Cell object, which itself can
    contain paragraphs and tables.
    """
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def get_control_summary(control="AC-1"):
    """TODO"""
    pass


def _is_control_summary(block):
    """
    True if table contains control summary information
    2nd cell in first row of table contains "control summary information"
    """
    if not isinstance(block, Table):
        return False
    first_row = block.rows[0]
    try:
        if first_row.cells[1].text.lower() == "control summary information":
            return first_row.cells[0].text
        return False
    except IndexError:
        return False


def parse_control_table(table):
    """
    TODO
    extract data from control summary table
    Not sure how to detect checked boxes
    """
    responsible_role = None
    imp_status = None
    origination = None
    for row in table.rows[1:]:
        for c in row.cells:
            if c.text.strip().lower().startswith("responsible role:"):
                responsible_role = c.text[len("responsible role:") :].split(",")
                responsible_role = [role.strip() for role in responsible_role]
            elif c.text.strip().startswith("Implementation Status"):
                # return which box is checked
                pass
            elif c.text.strip().startswith("Control Origination"):
                # return which box is checked
                pass
            else:
                pass
    raise


def parse_implementation_table(table):
    """Extract implementation narratives"""
    implementations = {}
    for row in table.rows[1:]:
        try:
            implementations.update({row.cells[0].text: row.cells[1].text})
        except IndexError:
            pass
    return implementations


def run(target_doc):
    # Start parsing the doc..
    doc = Document(docx=target_doc)

    tables = []

    for block in iter_block_items(doc):
        """Control details are in tables, skip the rest"""
        if not isinstance(block, Paragraph):
            tables.append(block)

    # Loop through all tables parsed from docx
    # If its a control summary table, add that control to our list
    # Then grab the implementation narratives from the following table
    check_next = False
    controls = {}
    check_control = None

    for t in tables:
        control = _is_control_summary(t)
        if control:
            c_dict = {
                "control": control,
                "responsible_role": None,
                "imp_status": None,
                "origination": None,
                "implementation": {},
            }
            # print('Found %s...' % control)
            # TODO - parse_control_table(t)

            # Next table in the doc is implementation narratives
            check_next = True
            # Need to keep control reference until we grab implementation
            check_control = control

            controls[control] = c_dict
        elif check_next and check_control:
            controls[check_control].update(
                {"implementation": parse_implementation_table(t)}
            )
            check_next = False
            check_control = None
        else:
            check_next = False
            check_control = None

    # Add all implementation narratives to a list for similarity measurement
    all_desc = []
    desc_lkup = []
    for c, d in controls.items():
        for i, txt in d["implementation"].items():
            desc_lkup.append(": ".join([c, i]))
            all_desc.append(txt.strip().lower())

    print("Parsed %d controls" % len(controls.items()))
    print(
        "Comparing %d narratives from %d controls"
        % (len(all_desc), len(controls.items()))
    )
    print("%d identical narratives found" % (len(all_desc) - len(set(all_desc))))

    gen_docs = [
        [w.lower() for w in word_tokenize(text) if w not in string.punctuation]
        for text in all_desc
    ]

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

    very_similar = {}
    similar_count = 0
    # Find all control narratives which are identical or very similar (>0.8)
    for base_narrative, d in enumerate(diffs):
        base = desc_lkup[base_narrative]
        for compared_narrative, diff in enumerate(d):
            if diff > 0.8:
                compared_to = desc_lkup[compared_narrative]
                if base != compared_to:
                    output_key = very_similar.setdefault(base, {})
                    output_key.update({compared_to: str(diff)})
                    similar_count += 1

    # Matrix/spreadsheet output
    with open("matrix.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([""] + desc_lkup)
        for base_narrative, d in enumerate(diffs):
            row = [desc_lkup[base_narrative]] + d
            writer.writerow(row)


if __name__ == "__main__":
    target_doc = sys.argv[1]
    run(target_doc)
