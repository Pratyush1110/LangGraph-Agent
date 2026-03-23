from datetime import datetime

from langchain_core.callbacks import BaseCallbackHandler


class AgentLogger(BaseCallbackHandler):
    """Logs LLM calls and tool usage for live tracing."""

    def on_llm_start(self, serialized, prompts, **kwargs):
        prompt_size = len(prompts[0]) if prompts else 0
        print(f"[{self._time()}] [LLM] start | input_chars={prompt_size}", flush=True)

    def on_llm_end(self, response, **kwargs):
        text = ""
        try:
            if response.generations and response.generations[0]:
                gen = response.generations[0][0]
                text = getattr(gen, "text", "") or ""
        except Exception:
            text = ""

        print(f"[{self._time()}] [LLM] end   | output_chars={len(text)}", flush=True)

    def on_tool_start(self, serialized, input_str, **kwargs):
        tool_name = serialized.get("name", "unknown") if serialized else "unknown"
        snippet = (input_str or "")[:120]
        print(f"[{self._time()}] [TOOL] start | name={tool_name}", flush=True)
        print(f"[{self._time()}] [TOOL] input | {snippet}", flush=True)

    def on_tool_end(self, output, **kwargs):
        snippet = str(output)[:120]
        print(f"[{self._time()}] [TOOL] end   | {snippet}", flush=True)

    def on_chain_error(self, error, **kwargs):
        print(f"[{self._time()}] [ERROR] {error}", flush=True)

    def _time(self):
        return datetime.now().strftime("%H:%M:%S")
