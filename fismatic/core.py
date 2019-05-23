from .docx_parser import DocxParser
from . import similarity


def run(target_doc):
    parser = DocxParser(target_doc)
    controls = parser.get_controls()

    # Add all implementation narratives to a list for similarity measurement
    all_desc = []
    desc_lkup = []
    for name, control in controls.items():
        for part, txt in control.implementation.items():
            desc_lkup.append(": ".join([name, part]))
            all_desc.append(txt.strip().lower())

    num_controls = len(controls.items())
    print("Parsed {} controls".format(num_controls))
    print(
        "Comparing {} narratives from {} controls".format(len(all_desc), num_controls)
    )
    print("{} identical narratives found".format(len(all_desc) - len(set(all_desc))))

    diffs = similarity.generate_diffs_with_labels(desc_lkup, all_desc)
    similarity.write_matrix(diffs)

    very_similar = similarity.similar_controls(diffs)
    similarity.print_similarity(very_similar)
