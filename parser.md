# Prototype SSP parsing - NOT MAINTAINED

Rough script exploring approaches to extract control details from a FedRamp template SSP word document and analyzing them for similarity of implementation narratives.

### Installation

Install dependencies using [Pipenv](https://docs.pipenv.org/en/latest/):

```
pipenv install
```

### Running

1. Download an SSP(.docx) based on the [FedRamp template](https://www.fedramp.gov/templates/).
1. Execute the script from within the virtual environment.

   ```sh
   pipenv run python ssp-parse.py <path_to.docx>
   ```

Outputs a matrix(csv) of difference measures between all control implementation narratives as `matrix.csv`
