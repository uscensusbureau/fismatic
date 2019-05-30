import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def test_notebook():
    # https://nbconvert.readthedocs.io/en/latest/execute_api.html#executing-notebooks-using-the-python-api-interface
    with open("./analysis.ipynb") as f:
        nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        ep.preprocess(nb, {})
