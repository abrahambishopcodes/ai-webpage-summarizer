from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url="https://api.groq.com/openai/v1")

def summarize(title, text):
    """
    Uses OpenAI's model to read, understand and summarize the article based on the provided title and text.
    
    :param title: receives the title of the article to be summarized
    :param text: receives the text of the article to be summarized
    :return: returns the summary of the article
    """

    print(f"Summarizing article titled: {title}")

    prompt = f"Summarize the following article titled '{title}':\n\n{text}\n\nSummary:"
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes articles."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content