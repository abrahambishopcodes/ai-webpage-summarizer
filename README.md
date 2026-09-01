# AI Web Summarizer

A small command-line tool that takes the URL of an article, scrapes its text, and
returns an AI-generated summary.

## What it does

1. Prompts you for an article URL.
2. Downloads the page and extracts its title and visible text.
3. Sends that text to an LLM and prints back a short summary.

## Flow

```
main.py  ->  scraper.scrape(url)      # fetch + parse HTML -> (title, text)
         ->  summarizer.summarize()   # send to LLM -> summary string
         ->  print summary
```

- **`src/main.py`** – entry point; handles user input and output.
- **`src/scraper.py`** – `scrape(url)` uses `requests` to fetch the page and
  `BeautifulSoup` to pull out the `<title>` and all text. Raises/handles HTTP errors.
- **`src/summarizer.py`** – `summarize(title, text)` builds a prompt and calls the
  chat-completions API, returning the model's summary.

## Libraries used

| Library          | Purpose                                                        |
| ---------------- | ------------------------------------------------------------- |
| `requests`       | HTTP GET to download the article HTML.                        |
| `beautifulsoup4` | Parse the HTML and extract the title and text content.        |
| `openai`         | Client for the chat-completions API (pointed at Groq's endpoint). |
| `python-dotenv`  | Load the API key from a local `.env` file.                    |

The summarizer talks to Groq's OpenAI-compatible API
(`base_url="https://api.groq.com/openai/v1"`) using the `openai/gpt-oss-120b` model.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests beautifulsoup4 openai python-dotenv
```

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_groq_api_key_here
```

## Run

```bash
cd src
python main.py
```

Then paste an article URL when prompted.
