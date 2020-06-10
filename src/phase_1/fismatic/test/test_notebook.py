import glob
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def test_notebooks():
    notebooks = glob.glob("./*.ipynb")
    # safety check
    assert len(notebooks) > 2

    for notebook in notebooks:
        # https://nbconvert.readthedocs.io/en/latest/execute_api.html#executing-notebooks-using-the-python-api-interface
        with open(notebook) as f:
            nb = nbformat.read(f, as_version=4)
            ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
            ep.preprocess(nb, {})
