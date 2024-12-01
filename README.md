# 📚 Survey Generator

## Overview

**Survey Generator** is a Python-based project designed to streamline the research process by automating the search and retrieval of academic papers on a specific topic. Using a natural language query, this tool interacts with multiple paper databases to find relevant results and organizes them efficiently. Additionally, with the integration of the **PaperQA** library, users can ask natural language questions about the retrieved papers, further accelerating the process of literature review and exploration.

The primary objective of this project is to save researchers valuable time by automating tedious aspects of academic paper searches, allowing them to focus on analyzing and applying the results.

---

## Features

1. **Automated Paper Search**:
   - Perform searches across multiple academic databases using a natural language query.
   - Filter results based on publication year.
   
2. **Organized Storage**:
   - Download and save all retrieved PDFs in a dedicated folder within the `papers` directory.
   - Automatically generate an Excel database containing:
     - DOI
     - Title
     - Citation count
     - Journal or conference site
     - BibTeX entry
     - Publication year
     - URL
   
3. **Question Answering**:
   - Integrates the **PaperQA** library for querying retrieved papers in natural language.

4. **Command-Line Interface**:
   - Fully customizable through command-line arguments for search query, year range, and more.

---

## Installation

### Prerequisites
- Python 3.11 or higher
- pip or conda

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/survey-generator.git
   cd survey-generator
   ```

2. Install dependencies:
   Using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

   Using `conda`:
   ```bash
   conda create --name survey-generator-env --file requirements.txt
   conda activate survey-generator-env
   ```

---

## Usage

Run the script via the command line with the following options:

```bash
python script.py --folder <folder_name> --query <search_query> --amount <number_of_papers> --start_year <start_year> --end_year <end_year>
```

### Example Command
To search for papers on "multilingual large language models explainability," retrieve 30 papers, and filter results from 2022 to 2024, run:
```bash
python script.py --folder multilingual_intrepretability --query "multilingual large language models explainability" --amount 30 --start_year 2022 --end_year 2024
```

### Arguments
- `--folder`: Name of the folder to save search results. Default is `multilingual_intrepretability`.
- `--query`: The search query in natural language. This argument is required.
- `--amount`: Number of papers to retrieve. Default is `30`.
- `--start_year`: Starting year for filtering papers. Default is `2022`.
- `--end_year`: Ending year for filtering papers. Default is `2024`.

---

## Outputs

1. **Papers Directory**:
   - All PDFs are downloaded and saved in a folder named after the `--folder` argument within the `papers` directory.

2. **Excel Database**:
   - An Excel file is generated containing the following columns:
     - `doi`: Digital Object Identifier of the paper.
     - `title`: Title of the paper.
     - `citationCount`: Number of citations the paper has received.
     - `site`: Journal or conference where the paper was published.
     - `bibtex`: BibTeX entry for easy citation.
     - `year`: Publication year.
     - `url`: URL to the paper.

---

## Todos

1. ✅ **Integration with Paper-Scrapper**:
   - Survey Generator is already integrated with Paper-Scrapper for efficient and accurate paper retrieval.

2. ✅ **Thematic Databases**:
   - Papers are organized into thematic databases for easier categorization and analysis.

3. 🔲 **Integration with PaperQA**:
   - Work is in progress to fully enable natural language querying of papers using the PaperQA library.

Feel free to contribute to the project by submitting issues or pull requests! 🚀