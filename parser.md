# Prototype SSP parsing

Rough script exploring approaches to extract control details from a FedRAMP SSP Word document template and analyzing them for similarity of implementation narratives.

## Setup

1. [Install Conda.](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
1. Set up Conda environment.

   ```sh
   conda env create -f environment.yml
   conda activate fismatic
   ```

## Running

1. Download an SSP as a `.docx` based on the [FedRAMP template](https://www.fedramp.gov/templates/).
   - The [Azure Blueprint FedRAMP High SSP](https://www.microsoft.com/en-us/trustcenter/compliance/fedramp) is a good one to test with.
1. Execute the script from within the virtual environment.

   ```sh
   python run.py <path>
   ```

The `path` can be a specific file, or a directory. Outputs one matrix of difference measures between all control implementation narratives per input file under `out/`, as well as per-file stats at `out/all.csv`.

## Notebook

To start the Jupyter Notebook:

```sh
jupyter notebook
```

then open [`analysis.ipynb`](http://localhost:8888/notebooks/analysis.ipynb). Before committing, remove the outputs (and thus any potential sensitive information) using:

```sh
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace *.ipynb
```

## Development

To run tests:

1. Download the [Azure Blueprint FedRAMP High SSP](https://www.microsoft.com/en-us/trustcenter/compliance/fedramp), and place the file in this directory.
1. From this directory, run:

   ```sh
   pytest
   ```
