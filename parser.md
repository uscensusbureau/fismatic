# Prototype SSP parsing

Rough script exploring approaches to extract control details from a FedRAMP SSP Word document template and analyzing them for similarity of implementation narratives.

## Setup

1. Install Python 3.
1. Install [Pipenv](https://docs.pipenv.org/en/latest/).
1. Install Python packages.

   ```sh
   pipenv install
   ```

## Running

1. Download an SSP as a `.docx` based on the [FedRAMP template](https://www.fedramp.gov/templates/).
   - The [Azure Blueprint FedRAMP High SSP](https://www.microsoft.com/en-us/trustcenter/compliance/fedramp) is a good one to test with.
1. Execute the script from within the virtual environment.

   ```sh
   pipenv run python run.py <path_to.docx>
   ```

Outputs a matrix of difference measures between all control implementation narratives as `matrix.csv`.

## Development

To run tests:

1. Download the [Azure Blueprint FedRAMP High SSP](https://www.microsoft.com/en-us/trustcenter/compliance/fedramp), and place the file in this directory.
1. From this directory, run:

   ```sh
   pytest
   ```
