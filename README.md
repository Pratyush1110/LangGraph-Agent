# LangChain + LangGraph Research and PDF Agent

A lightweight, terminal-based AI assistant built with LangChain, LangGraph, and Groq. This project combines a tool-using chat agent with two practical capabilities:

- Web search using DuckDuckGo for current facts and public information
- PDF reading for document-based question answering and summarization

The agent keeps conversation history, decides when to call tools, and returns polished long-form answers. In this repository, `sample.pdf` is included as a chess book so you can test document Q&A and summarization workflows immediately.

## Features

- Tool-augmented chat agent built on LangGraph state transitions
- Groq-hosted LLM integration (`llama-3.1-8b-instant`)
- Automatic tool routing with loop-back execution
- Conversation memory across turns in a single session
- Built-in PDF text extraction with page markers
- Detailed response style enforced through system prompt rules
- Minimum response-length policy (100+ words in final answers)

## Project Structure

- `main.py`: CLI entry point with chat loop and message history
- `agent.py`: Agent construction, LLM setup, system prompt, and graph wiring
- `tools.py`: Tool implementations (`web_search`, `read_pdf`)
- `requirements.txt`: Python dependency list
- `sample.pdf`: Chess book used for PDF testing and demo queries

## How It Works

The app uses a LangGraph workflow with two nodes:

1. `agent` node:
   - Builds a message list with a system prompt + chat history
   - Invokes the LLM with bound tools
2. `tools` node:
   - Executes the selected tool call
   - Returns tool output back to the graph

Flow summary:

- Start -> agent
- If the model asks for tools -> tools -> agent
- If no tool is needed -> end

This allows the model to think, call one of the tools when needed, and then generate the final response using retrieved information.

## Requirements

- Python 3.10+
- A Groq API key
- Internet access for web search

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Langchain_Agent
```

### 2. Create and activate a virtual environment

#### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### Windows (Command Prompt)

```bat
python -m venv venv
venv\Scripts\activate.bat
```

#### macOS/Linux

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The application loads environment variables with `python-dotenv`.

## Running the Agent

```bash
python main.py
```

You should see:

```text
Agent ready! Type quit to exit.
```

Type your question and press Enter. Exit anytime using:

- `quit`
- `exit`
- `q`

## Using the Chess PDF (`sample.pdf`)

This repository includes `sample.pdf`, a chess book, so you can immediately test document-aware interactions.

### Example prompts

- "Summarize the main concepts explained in sample.pdf."
- "What does the book say about opening principles?"
- "List 5 practical tactics from sample.pdf with simple examples."
- "Create a beginner study plan from the chess book in sample.pdf."

### Notes on PDF reading behavior

- The `read_pdf` tool extracts text page-by-page
- Output includes page separators (`--- Page N ---`)
- Very large extracted text is truncated to keep responses manageable
- If text is not extractable, the tool reports that clearly

## Web Search Behavior

The `web_search` tool uses DuckDuckGo and returns up to 5 results with:

- Title
- URL
- Short summary

Use cases:

- Current events
- Fresh facts not likely in model training data
- Lightweight verification and references

## Design Choices

- `temperature=0` for deterministic and stable answers
- `max_tokens=1024` to support long, complete responses
- Explicit tool-use constraints in the system prompt to reduce repeated calls
- Message history retained in memory during runtime for context continuity

## Troubleshooting

### Groq authentication error

- Confirm `.env` exists in the project root
- Confirm `GROQ_API_KEY` is valid and active
- Restart the terminal after updating environment variables

### No web results

- Check internet connection
- Retry with a more specific query
- Verify DuckDuckGo access from your network

### PDF not found

- Use the correct path and filename
- Keep `sample.pdf` in the project root or provide absolute path

### Empty or weak PDF output

- Some PDFs are image-only and have little extractable text
- Run OCR externally if needed, then re-test with a text-searchable PDF

## Security and Usage Notes

- Do not commit real secrets to source control
- Keep API keys in `.env` and add `.env` to `.gitignore`
- Review model outputs before using them in critical decisions
- Tool outputs may include inaccuracies and should be verified when important

## Suggested Next Improvements

- Add streaming token output for better chat UX
- Add page-range support for PDF tool calls
- Add citation formatting with source links and page references
- Add tests for tool functions and graph behavior
- Add a small web UI (Streamlit/FastAPI + frontend)

## Tech Stack

- LangChain
- LangGraph
- Groq API (`llama-3.1-8b-instant`)
- DuckDuckGo Search (`duckduckgo-search`)
- PyMuPDF (`pymupdf`)
- Python Dotenv

## License

Add your preferred license in this section (for example, MIT) before publishing.
