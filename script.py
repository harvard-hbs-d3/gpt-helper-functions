from dotenv import load_dotenv
import openai
import pandas as pd
import logging
import datetime
import os
from tqdm import tqdm
from openai import OpenAI

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize logging
logging.basicConfig(
    filename=os.path.join(script_dir, 'filter_ai_sentences.log'), 
    filemode='a', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    logging.error("OpenAI API key not found in environment variables.")
    raise ValueError("OpenAI API key not found in environment variables. Please set it in the .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Function to filter out non-AI sentences using OpenAI GPT
def query_gpt(sentence):
    messages = [
        {"role": "system", "content": SYSTEM_MESSGE},
        {"role": "user", "content": f"{QUERY}\n\n{sentence}"}
    ]
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        max_tokens=10,
        temperature=0.1,
        seed=SEED,
        user="test_user"  # Replace with actual user information if needed
    )

    # Log the response
    logging.info(f"Received response from the model: {response}")

    return response.choices[0].message.content.strip()

# Function to process a batch of sentences
def process_batch(batch):
    batch['AI Related'] = batch['sentence'].apply(query_gpt)
    return batch

# Function to process the input CSV and add an AI-related column for all rows
def process_csv(input_csv, output_csv, batch_size=5):
    chunks = []
    for chunk in tqdm(pd.read_csv(input_csv, chunksize=batch_size), desc="Processing batches"):
        processed_chunk = process_batch(chunk)
        chunks.append(processed_chunk)
        # Log the progress
        logging.info(f"Processed batch of {batch_size} rows")

    # Concatenate all processed chunks and save to output CSV
    processed_df = pd.concat(chunks)
    processed_df.to_csv(output_csv, index=False)
    logging.info(f"Processed CSV saved to {output_csv}")

if __name__ == "__main__":

    # Global Consts
    global SEED
    global MODEL_NAME
    global SYSTEM_MESSAGE
    global QUERY

    SEED = 123  # Seed for reproducibility of GPT responses
    MODEL_NAME = 'gpt-3.5-turbo'
    SYSTEM_MESSGE = "The GPT determines if a sentence is related to AI."
    QUERY = "I submit a sentence, and the GPT will answer with 'Yes' if the sentence is related to AI or 'No' if it is not."

    BATCH_SIZE = 3

    # Paths for the input and output CSV files in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(script_dir, 'data/sentences.csv')
    output_csv = os.path.join(script_dir, 'data/sentences_with_ai_related.csv')

    # Process the CSV and save the results to the output CSV
    process_csv(input_csv, output_csv, batch_size = BATCH_SIZE)
    logging.info(f"Processed CSV saved to {output_csv}")

    # Log the completion time
    formatted_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"File running finished at: {formatted_time}")
    logging.info(f"File running finished at: {formatted_time}")