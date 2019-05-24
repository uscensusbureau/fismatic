from .docx_parser import DocxParser
from . import similarity


def run(target_doc):
    parser = DocxParser(target_doc)
    implementations_by_id = parser.get_implementations_by_id()

    num_controls = parser.num_controls()
    num_implementations = parser.num_implementations()
    print("Parsed {} controls".format(num_controls))
    print("{} total words in the controls.".format(parser.num_words()))
    print(
        "Comparing {} narratives from {} controls".format(
            num_implementations, num_controls
        )
    )
    print(
        "{} identical narratives found".format(parser.num_identical_implementations())
    )

    diffs = similarity.generate_diffs_with_labels(implementations_by_id)
    similarity.write_matrix(diffs)

    very_similar = similarity.similar_controls(diffs)
    similarity.print_similarity(very_similar)
