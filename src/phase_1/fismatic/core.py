import glob
import os.path
import sys
from .docx_parser import DocxParser


def get_files(input_path):
    """`input_path` can be a specific file, or a directory."""
    if os.path.isdir(input_path):
        # only process docx
        pattern = os.path.join(input_path, "**", "*.docx")
        files = glob.glob(pattern, recursive=True)
        if not files:
            print("No docx files found.", file=sys.stderr)
        return files
    else:
        return [input_path]


def control_set_for(input_file):
    parser = DocxParser(input_file)
    return parser.get_control_set()


def stats_for(control_set):
    filename = os.path.basename(control_set.source)
    return {
        "Filename": filename,
        "# controls": control_set.num_controls(),
        "# identical implementations": control_set.num_identical_implementations(),
        "# implementations": control_set.num_implementations(),
        "# unique implementations": control_set.num_unique_implementations(),
        "# tokens": control_set.num_tokens(),
    }
