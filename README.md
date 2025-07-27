# URL Parameter Extractor 🕷️

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, efficient command-line tool built with Python to crawl a list of URLs and extract all of their query string parameters. This utility is perfect for web analysis, data gathering, or as a foundational tool in a security reconnaissance workflow. The extracted data is saved into a clean, structured CSV file for easy analysis.

---

## 🌟 Key Features

*   **Simple Command-Line Interface:** Easy-to-use flags for specifying URLs and output files.
*   **Bulk URL Processing:** Accepts and processes multiple URLs in a single command.
*   **Comprehensive Parameter Extraction:** Identifies and extracts all key-value pairs from URL query strings.
*   **Structured CSV Output:** Saves the extracted parameters in a well-formatted CSV for use in spreadsheets or other data analysis tools.
*   **Lightweight & Focused:** Built with minimal dependencies for fast and reliable operation.

---

## 🚀 Demo

![Demo GIF Placeholder](https://user-images.githubusercontent.com/26887593/180222485-3313d4f3-1658-4687-9572-13d6a2f4a4a8.gif)

---

## 🔧 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

*   [Python](https://www.python.org/downloads/) (Version 3.9 or higher)

### Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create and Activate a Virtual Environment** (Recommended)
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate it
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    The project uses a `requirements.txt` file to manage its few dependencies.
    ```bash
    pip install -r requirements.txt
    ```

---

## ⚙️ Usage

Execute the `web_crawler.py` script from your terminal using the `-u` flag for URLs and the optional `-o` flag to name the output file.

**Important:** Enclose each URL in double quotes (`"`).

### Basic Example

```bash
python web_crawler.py -u "https://example.com?param1=value1" "https://another-url.com?product_id=123®ion=us"
```

This command will process the two URLs and save the results to the default extracted_parameters.csv file in your project directory.

### Specifying an Output File Name

```bash
python web_crawler.py -u "https://example.com?param1=value1¶m2=value2" -o my_custom_data.csv
```

This command will save the results to my_custom_data.csv.

---

## 📄 Output Example

The script generates a CSV file with the URL as the first column, followed by columns for each unique parameter found across all provided URLs.

**`extracted_parameters.csv`:**
```csv
URL,param1,param2,product_id,region
https://example.com?param1=value1¶m2=value2,value1,value2,,
https://another-url.com?product_id=123®ion=us,,,123,us
```

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📃 License

Distributed under the MIT License. See `LICENSE.txt` for more information.