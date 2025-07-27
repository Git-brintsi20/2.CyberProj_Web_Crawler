# Web Crawler Project

## Description
This project is a command-line-based web crawler that takes URLs and extracts all parameters from the provided URLs.

## How to Run
1. Clone this repository or download the ZIP.
2. Navigate to the project folder.
3. Activate the virtual environment using:

    ```bash
    .\venv\Scripts\activate
    ```

4. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the crawler with the following command:

    ```bash
    python web_crawler.py -u "https://example.com?param1=value1" "https://another-url.com?key=123" -o output.csv
    ```

6. The results will be saved in the `output.csv` file.

## Requirements
- Python 3.x
- BeautifulSoup
- Requests

## Output
The output file `output.csv` will contain a list of all URL parameters extracted from the provided URLs.
