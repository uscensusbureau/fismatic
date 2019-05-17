# Prototype SSP parsing

Rough script exploring approaches to extract control details from a FedRAMP SSP Word document template and analyzing them for similarity of implementation narratives.

### Installation

Install dependencies using [Pipenv](https://docs.pipenv.org/en/latest/):

```
pipenv install
```

### Running

1. Download an SSP as a `.docx` based on the [FedRAMP template](https://www.fedramp.gov/templates/).
1. Execute the script from within the virtual environment.

   ```sh
   pipenv run python ssp-parse.py <path_to.docx>
   ```

Outputs a matrix of difference measures between all control implementation narratives as `matrix.csv`.
