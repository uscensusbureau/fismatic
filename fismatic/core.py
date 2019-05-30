import glob
import itertools
import os.path
import sys
from .docx_parser import DocxParser


def flatten(list_of_lists):
    # https://stackoverflow.com/a/13498063/358804
    return list(itertools.chain(*list_of_lists))


def get_files(input_path):
    """`input_path` can be a specific file, or a directory."""
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


def stats_for(input_file, control_set):
    return {
        "Filename": input_file,
        "# controls": control_set.num_controls(),
        "# identical implementations": control_set.num_identical_implementations(),
        "# implementations": control_set.num_implementations(),
        "# unique implementations": control_set.num_unique_implementations(),
        "# tokens": control_set.num_tokens(),
    }
