# Polish Alphabet Diacritic Remover
This project provides a simple script to replace Polish letters with their ASCII equivalents. 


## Project Status
[![Python package](https://github.com/pen40t0/pol/actions/workflows/main.yml/badge.svg)](https://github.com/pen40t0/pol/actions/workflows/main.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python version](https://img.shields.io/badge/python-3.5+-brightgreen)](https://www.python.org/downloads/)
[![PyPI version](https://img.shields.io/pypi/v/black.svg)](https://pypi.org/project/black/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/)
[![Discord](https://img.shields.io/discord/1243025843094294591?label=Join%20Discord&logo=discord&color=blue)](https://discord.gg/CbSdGanqvU)

## Features
- Converts Polish characters with diacritics (e.g., `ą`, `ć`, etc.) to plain ASCII characters.
- Lightweight and uses only Python's standard library.


## Installation


### User Installation


#### Prerequisites
- Python 3.5 or later

1. Open
- The Command Prompt (On Windows)
- The Terminal (On macOS/Linux)

2. Clone the repository:
    ```bash
    git clone <https://github.com/pen40t0/polish.git>

3. Navigate to the Project Directory
    ```bash
    cd polish

4. Create a Virtual Environment
    ```bash
    python -m venv venv

venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux

5. Install Dependencies
pip install -r requirements.txt

6. Run the Program
python main.py

7. Run Tests (Optional)
python -m unittest discover -s tests


## Contributors
- Jake
- Ayshan
- Vaishnavi


## Changelog
January 31, 2025         Version 0.1.0
<!-- Possibly make it a link and create a website That simply says this "Changelog January 31,2025 Version 0.1.0
That's all folks XD"
See https://github.com/psf/black/blob/main/README.md for example -->


## License
MIT


## TODOs / Future Work / Known issues
- Always more efficient
- Support tokenizers with overlapping positions (ie synonyms, etc)
- Improve support for phrase slop
- Helper functions (like this start at edismax that help recreate Solr / Elasticsearch lexical queries)
- Fuzzy search
- Efficient way to "slurp" some top N results from retrieval system into a dataframe