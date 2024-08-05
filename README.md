# GPT Helper Functions - Batch Processing for AI Sentence Filtering

This repository provides a Python script that utilizes OpenAI's GPT model for batch processing of sentences stored in a CSV file. The script determines if each sentence is related to AI and adds this information as a new column in the CSV.

## Features

- Ingest a CSV file with sentences.
- Use GPT-3.5-turbo to determine if each sentence is AI-related.
- Output a new CSV file with an additional column indicating AI relevance.
- Detailed logging and progress tracking.

## Getting Started

### Prerequisites

- Python 3.6+
- An OpenAI API key
- The following Python packages:
  - `openai`
  - `pandas`
  - `python-dotenv`
  - `requests`
  - `beautifulsoup4`
  - `tqdm`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/harvard-hbs-d3/gpt-helper-functions.git
    cd gpt-helper-functions
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your OpenAI API key:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

### Usage

1. Prepare your input CSV file with a column named `sentence`. Place it in the `data` directory and name it `sentences.csv`.

2. Run the script:
    ```bash
    python script.py
    ```

3. The output CSV file with the added `AI Related` column will be saved in the `data` directory as `sentences_with_ai_related.csv`.

### Example

The input CSV (`sentences.csv`):
```plaintext
sentence
"This is a test sentence."
"AI is transforming the world."