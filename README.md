# LangChain + LangGraph Research Agent

Build a practical AI assistant that can both search the web and read PDFs, right from your terminal.

This project combines LangChain, LangGraph, and Groq to create a tool-using chat agent that keeps conversation context, decides when to call tools, and returns clear long-form responses. It also includes a ready-to-use chess reference file, `sample.pdf`, so you can test document Q&A immediately.

> [!TIP]
> If you want a minimal but real example of tool-calling agents with graph-based routing, this repo is a great starting point.

## What You Get

- Web search via DuckDuckGo for fresh facts and current information
- PDF reading and text extraction for document-based Q&A
- LangGraph workflow with automatic tool routing and loop-back execution
- Session-level conversation history in the CLI
- Structured response behavior via system prompt rules
- Minimum final response length policy (100+ words)

## Tech Stack

- Python 3.10+
- LangChain
- LangGraph
- Groq API (`llama-3.1-8b-instant`)
- DuckDuckGo Search (`duckduckgo-search`)
- PyMuPDF (`pymupdf`)
- Python Dotenv

## Quick Start

### 1. Clone

```bash
git clone <your-repo-url>
cd Langchain_Agent
```

### 2. Create a virtual environment

Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Windows (Command Prompt):

```bat
python -m venv venv
venv\Scripts\activate.bat
```

macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run

```bash
python main.py
```

Expected startup message:

```text
Agent ready! Type quit to exit.
```

Exit commands: `quit`, `exit`, `q`

## Included Demo File: Chess Book PDF

The repository includes `sample.pdf` (a chess book) so you can test document-aware prompts out of the box.

Try prompts like:

- "Summarize the key ideas in sample.pdf."
- "What opening principles are covered in the chess book?"
- "Give me five practical tactics from sample.pdf with simple examples."
- "Create a beginner-friendly chess study plan based on sample.pdf."

PDF tool behavior:

- Extracts text page by page
- Adds page separators (`--- Page N ---`)
- Truncates very large output for stability
- Returns clear errors for missing files or non-extractable text

## How It Works

The app is built as a small LangGraph workflow with two nodes:

1. `agent`
   - Builds messages from system prompt + chat history
   - Invokes the LLM with bound tools
2. `tools`
   - Executes selected tool calls
   - Passes tool output back to the agent

Flow:

- Start -> `agent`
- Tool needed -> `tools` -> `agent`
- No tool needed -> End

This keeps tool use controlled and allows the model to produce final answers grounded in retrieved results.

## Project Layout

- `main.py` - CLI loop and message history
- `agent.py` - LLM setup, system prompt, graph wiring
- `tools.py` - `web_search` and `read_pdf` tool implementations
- `requirements.txt` - dependencies
- `sample.pdf` - chess book for PDF Q&A demos

## Troubleshooting

### Groq key/auth issues

- Confirm `.env` exists in the root
- Verify `GROQ_API_KEY` is valid
- Restart terminal session after edits

### Web search returns nothing

- Check internet connectivity
- Try a more specific query
- Confirm DuckDuckGo is reachable from your network

### PDF errors or weak extraction

- Verify file path/filename
- Keep `sample.pdf` in project root or pass absolute path
- For image-only PDFs, run OCR first

## Security Notes

- Never commit real API keys
- Keep secrets in `.env` and ensure `.env` is ignored by Git
- Treat tool output as helpful context, not guaranteed truth

## Roadmap Ideas

- Streaming token output in CLI
- Page-range support for PDF reading
- Source citations with URL/page references
- Tests for tools and graph behavior
- Optional web UI (Streamlit or FastAPI frontend)

## License

Add your preferred license (for example, MIT) before publishing.
