import fitz
from langchain_core.tools import tool
from ddgs import DDGS


@tool
def web_search(query: str) -> str:
    """Search the web using DuckDuckGo. Use for current events and facts."""
    try:
        results = DDGS().text(query, max_results=5)
        if not results:
            return "No results found."
        formatted = []
        for r in results:
            formatted.append(
                f"Title: {r['title']}\nURL: {r['href']}\nSummary:\n{r['body']}"
            )
        return "\n---\n".join(formatted)
    except Exception as e:
        return f"Search failed: {str(e)}"


@tool
def read_pdf(file_path: str) -> str:
    """Read and extract text from a PDF file. Use when asked about a document."""
    try:
        doc = fitz.open(file_path)
        text_parts = []
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text()
            if text.strip():
                text_parts.append(f"--- Page {page_num} ---\n{text}")
        doc.close()
        if not text_parts:
            return "PDF has no extractable text."
        full_text = "\n\n".join(text_parts)
        return full_text[:8000] + "\n[truncated]" if len(full_text) > 8000 else full_text
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"Error: {str(e)}"