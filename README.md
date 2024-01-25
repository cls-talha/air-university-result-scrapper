## Overview

This repository contains a web scraping project aimed at extracting subject grades and GPA information based on roll numbers and names. The project consists of both a Jupyter Notebook (`main.ipynb`) and a Python script (`main.py`). The scraped results are stored in the `scrapped_result` directory, and the source CSV file used for input is located in the `source_csv` directory.

## Project Structure

```
.
├── main.ipynb
├── main.py
├── scrapped_result
│   └── BSAIF22-result.csv
└── source_csv
    └── new_rolls.csv
```

- **main.ipynb:** This Jupyter Notebook contains the code for a simple scraper and a detailed scraper. The simple scraper extracts basic information, while the detailed scraper extracts subject grades and GPA. Both versions require a CSV file with roll numbers and names.

- **main.py:** This Python script contains the same functionality as the Jupyter Notebook but in a standalone script form.

- **scrapped_result:** This directory contains the resulting CSV file (`BSAIF22-result.csv`) where the scraped information is stored.

- **source_csv:** This directory contains the source CSV file (`new_rolls.csv`) with roll numbers and names that the scraper uses as input.

## Usage

1. Ensure you have the necessary libraries installed. You can install them using the following:

    ```bash
    pip install requests beautifulsoup4 pandas
    ```

2. Open and run either `main.ipynb` in a Jupyter environment or `main.py` using a Python interpreter.

3. Provide the input CSV file (`new_rolls.csv`) in the `source_csv` directory with columns 'roll' and 'name'.

4. Run the scraper, and the results will be stored in the `scrapped_result` directory as `BSAIF22-result.csv`.

## Note

- Ensure that the input CSV file contains the necessary columns ('roll' and 'name') for the scraper to function correctly.

- Results will be saved in a CSV file named `BSAIF22-result.csv` in the `scrapped_result` directory.

- Make sure you have the required libraries installed as mentioned in the 'Usage' section.
## License
- IDGAF

Feel free to customize the scraper according to your needs. If you encounter any issues, please report them in the 'Issues' section of this repository.
