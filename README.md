# 🤖 LangChain + LangGraph Research Agent

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Workflow-FF6B6B?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM_API-F55036?style=for-the-badge&logo=groq&logoColor=white)
![DuckDuckGo](https://img.shields.io/badge/DuckDuckGo-Web_Search-DE5833?style=for-the-badge&logo=duckduckgo&logoColor=white)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-PDF_Parsing-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> A practical AI assistant that searches the web and reads PDFs — right from your terminal.

This project combines **LangChain**, **LangGraph**, and **Groq** to build a tool-using conversational agent that maintains session history, intelligently routes tool calls, and delivers clear, long-form responses. A ready-to-use chess reference (`sample.pdf`) is included so you can test document Q&A out of the box.

---

## ✨ Features

- 🔍 **Web search** via DuckDuckGo for fresh, real-time information
- 📄 **PDF reading** with page-by-page text extraction for document Q&A
- 🔄 **LangGraph workflow** with automatic tool routing and loop-back execution
- 🗂️ **Session-level conversation history** maintained throughout the CLI session
- 📏 **Minimum response length** enforced at 100+ words via system prompt rules

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Agent Framework | LangChain + LangGraph |
| LLM Provider | Groq API (`llama-3.1-8b-instant`) |
| Web Search | DuckDuckGo (`duckduckgo-search`) |
| PDF Parsing | PyMuPDF (`pymupdf`) |
| Config | Python Dotenv |

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Langchain_Agent
```

### 2. Create a virtual environment

**Windows (PowerShell)**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**
```bat
python -m venv venv
venv\Scripts\activate.bat
```

**macOS / Linux**
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

### 5. Run the agent

```bash
python main.py
```

You should see:
```
Agent ready! Type quit to exit.
```

> To exit, type `quit`, `exit`, or `q`.

---

## 📄 Demo: Chess Book PDF

The repo includes `sample.pdf` (a chess book) for immediate document-aware testing.

**Try these prompts:**

- `"Summarize the key ideas in sample.pdf."`
- `"What opening principles are covered in the chess book?"`
- `"Give me five practical tactics from sample.pdf with simple examples."`
- `"Create a beginner-friendly chess study plan based on sample.pdf."`

**How PDF extraction works:**
- Extracts text page by page
- Inserts `--- Page N ---` separators between pages
- Truncates very large outputs for stability
- Returns clear error messages for missing or non-extractable files

---

## 🏗️ How It Works

The agent is built as a compact **LangGraph** state machine with two nodes:

| Node | Responsibility |
|---|---|
| `agent` | Builds messages from system prompt + history, invokes LLM with tools |
| `tools` | Executes selected tool calls and returns results to the agent |

**Execution flow:**

```
Start → agent → (tool needed?) → tools → agent → ... → End
```

This keeps tool use controlled and allows the model to ground final answers in retrieved content.

---

## 📁 Project Layout

```
Langchain_Agent/
├── main.py          # CLI loop and message history
├── agent.py         # LLM setup, system prompt, graph wiring
├── tools.py         # web_search and read_pdf tool implementations
├── requirements.txt # Python dependencies
└── sample.pdf       # Chess book for PDF Q&A demos
```

---

## 🛠️ Troubleshooting

**Groq key / auth issues**
- Confirm `.env` exists in the project root
- Verify `GROQ_API_KEY` is valid at [console.groq.com](https://console.groq.com)
- Restart your terminal after editing `.env`

**Web search returns no results**
- Check your internet connection
- Try a more specific or rephrased query
- Verify DuckDuckGo is accessible from your network

**PDF errors or weak text extraction**
- Verify the file path and filename are correct
- Keep `sample.pdf` in the project root, or provide an absolute path
- For image-only / scanned PDFs, run OCR preprocessing first

---

## 🔐 Security Notes

- **Never commit real API keys** to version control
- Store all secrets in `.env` and ensure it is listed in `.gitignore`
- Treat tool output as helpful context — not guaranteed truth

---

## 🗺️ Roadmap

- [ ] Streaming token output in the CLI
- [ ] Page-range support for selective PDF reading
- [ ] Source citations with URL and page references
- [ ] Unit tests for tools and graph behavior
- [ ] Optional web UI (Streamlit or FastAPI frontend)

---

## 📜 License

Add your preferred license (e.g. MIT) before publishing.