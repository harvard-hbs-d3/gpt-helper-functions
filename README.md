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
sentence,author,date,category
"This is a test sentence.",John Doe,2024-01-01,General
"AI is transforming the world.",Jane Smith,2024-02-15,Technology
"The sky is blue.",Alice Johnson,2024-03-10,Nature
"Machine learning can analyze data.",Bob Lee,2024-04-05,Technology
"I love to read books.",Emma Davis,2024-05-20,General
"Deep learning algorithms are complex.",Chris Brown,2024-06-25,Technology
"What's the weather like today?",Diana Green,2024-07-30,General
"Data science is an exciting field.",Evan White,2024-08-15,Technology
"Artificial intelligence is the future.",Fiona Black,2024-09-05,Technology
"Let's go for a walk.",George King,2024-10-10,General
