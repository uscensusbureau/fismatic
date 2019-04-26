# Prototype SSP parsing - NOT MAINTAINED

Rough script exploring approaches to extract control details from a FedRamp template SSP word document and analyzing them for similarity of implementation narratives.

## Public domain

This project is in the worldwide [public domain](LICENSE.md).

### Installation

Install dependencies using Pipenv:
```
pipenv install
```

### Running

Download an SSP(.docx) based on the [FedRamp template](https://www.fedramp.gov/templates/)
Update `ssp-parse.TARGET_DOC` with the path to the the SSP.

Execute the script from within the virtual environment

```
pipenv run python ssp-parse.py
```

Outputs a matrix(csv) of difference measures between all control implementation narratives as
`matrix.csv`
