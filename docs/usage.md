# FISMAtic prototype

Current state: Jupyter Notebooks that perform linguistic and other analysis of System Security Plans (SSPs) written as Word documents.

## Technical overview

The primary technolgies in use:

- Python - programming language
- [spaCy](https://spacy.io/) - Natural Language Processing (NLP)
- [Jupyter Notebooks](https://jupyter.org/) - display of results
- [Pandas](https://pandas.pydata.org/) - everything quantitative

The meat of the project is in Python files under [`fismatic/`](../fismatic), and is `import`ed into Jupyter Notebooks for display. This code could be leveraged in a web application or as an API instead.

How it works: `.docx` files are read from the filesystem into memory as instances of [`ControlSet`s](../fismatic/control_set.py). These could be populated a different way: from a database connection, or [from OpenControl files on GitHub, as this example does](https://github.com/uscensusbureau/fismatic/pull/42). The processing takes place in spaCy/Pandas, and then the results are formatted and displayed in Jupyter.

## Setup

1. [Install Conda.](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
1. Set up Conda environment.

   ```sh
   conda env create -f environment.yml
   conda activate fismatic
   jupyter nbextension enable --py widgetsnbextension
   ```

1. Download the language model.

   ```sh
   python -m spacy download en_core_web_lg --user
   ```

## Running

1. Download an SSP as a `.docx` based on the [FedRAMP template](https://www.fedramp.gov/templates/).
   - The [Azure Blueprint FedRAMP High SSP](https://www.microsoft.com/en-us/trustcenter/compliance/fedramp) is a good one to test with.
1. Start the Jupyter Notebook.

   ```sh
   jupyter notebook --config=jupyter_notebook_config.py
   ```

1. Play with the following notebooks:
   - [`exploration.ipynb`](http://localhost:8888/notebooks/exploration.ipynb) - single SSPs
   - [`analysis.ipynb`](http://localhost:8888/notebooks/analysis.ipynb) - across SSPs
   - [`demo.ipynb`](http://localhost:8888/notebooks/demo.ipynb) - a proof-of-concept showing relevant control implementations being displayed to the user interactively

## Development

To run tests:

1. Download the [Azure Blueprint FedRAMP High SSP](https://www.microsoft.com/en-us/trustcenter/compliance/fedramp), and place the file in this directory.
1. From this directory, run:

   ```sh
   pytest
   ```
