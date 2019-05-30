import glob
import os.path
import sys
from .docx_parser import DocxParser
from . import similarity

OUT_DIR = "out"


def report(outfile, control_set):
    implementations_by_id = control_set.get_implementations_by_id()

    num_controls = control_set.num_controls()
    num_implementations = control_set.num_implementations()
    print("Parsed {} controls".format(num_controls))
    print("{} total words in the controls.".format(control_set.num_words()))
    print(
        "Comparing {} narratives from {} controls".format(
            num_implementations, num_controls
        )
    )
    print(
        "{} identical narratives found".format(
            control_set.num_identical_implementations()
        )
    )

    diffs = similarity.generate_diffs_with_labels(implementations_by_id)
    similarity.write_matrix(diffs, filename=outfile)

    very_similar = similarity.similar_controls(diffs)
    similarity.print_similarity(very_similar)


def get_files(input_path):
    if os.path.isdir(input_path):
        # only process docx
        pattern = os.path.join(input_path, "*.docx")
        files = glob.glob(pattern)
        if not files:
            print("No docx files found.", file=sys.stderr)
        return files
    else:
        return [input_path]


def control_set_for(input_file):
    parser = DocxParser(input_file)
    return parser.get_control_set()


def process_file(input_file):
    """Returns the ControlSet."""

    print("---------------\nParsing {} ...".format(input_file))
    control_set = control_set_for(input_file)
    outfile = os.path.join(OUT_DIR, input_file.replace(".docx", ".csv"))

    report(outfile, control_set)


def stats_for(input_file, control_set):
    return {
        "Filename": input_file,
        "# controls": control_set.num_controls(),
        "# identical implementations": control_set.num_identical_implementations(),
        "# implementations": control_set.num_implementations(),
        "# unique implementations": control_set.num_unique_implementations(),
        "# words": control_set.num_words(),
    }


def run(input_path):
    files = get_files(input_path)
    os.makedirs(OUT_DIR, exist_ok=True)

    for input_file in files:
        process_file(input_file)
