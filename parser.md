# Prototype SSP parsing

Rough script exploring approaches to extract control details from a FedRAMP SSP Word document template and analyzing them for similarity of implementation narratives.

## Setup

1. [Install Conda.](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
1. Set up Conda environment.

   ```sh
   conda env create -f environment.yml
   conda activate fismatic
   ```

1. Download the language model.

   ```sh
   python -m spacy download en_core_web_lg
   ```

## Running

1. Download an SSP as a `.docx` based on the [FedRAMP template](https://www.fedramp.gov/templates/).
   - The [Azure Blueprint FedRAMP High SSP](https://www.microsoft.com/en-us/trustcenter/compliance/fedramp) is a good one to test with.
1. Execute the script from within the virtual environment.

   ```sh
   python run.py <path>
   ```

The `path` can be a specific file, or a directory. Outputs one matrix of difference measures between all control implementation narratives per input file under `out/`.

## Notebook

To start the Jupyter Notebook:

```sh
jupyter notebook --config=jupyter_notebook_config.py
```

then open [`analysis.ipynb`](http://localhost:8888/notebooks/analysis.ipynb).

## Development

To run tests:

1. Download the [Azure Blueprint FedRAMP High SSP](https://www.microsoft.com/en-us/trustcenter/compliance/fedramp), and place the file in this directory.
1. From this directory, run:

   ```sh
   pytest
   ```
