# Groq pricing per million tokens (as of 2024; verify latest values in Groq pricing docs)
PRICING = {
    "llama-3.1-8b-instant": {"input": 0.05, "output": 0.08},
    "llama-3.1-70b-versatile": {"input": 0.59, "output": 0.79},
}


class TokenTracker:
    def __init__(self, model: str = "llama-3.1-8b-instant"):
        self.model = model
        self.total_input = 0
        self.total_output = 0
        self.call_count = 0

    def record(self, usage):
        """Record usage from response.usage_metadata."""
        if not usage:
            return

        self.total_input += usage.get("input_tokens", 0)
        self.total_output += usage.get("output_tokens", 0)
        self.call_count += 1

    def cost(self) -> float:
        """Calculate total estimated cost in USD."""
        prices = PRICING.get(self.model, {"input": 0, "output": 0})
        return (
            self.total_input * prices["input"] / 1_000_000
            + self.total_output * prices["output"] / 1_000_000
        )

    def summary(self) -> str:
        return (
            "\n--- Session Summary ---\n"
            f"LLM calls:     {self.call_count}\n"
            f"Input tokens:  {self.total_input:,}\n"
            f"Output tokens: {self.total_output:,}\n"
            f"Est. cost:     ${self.cost():.6f} USD\n"
        )
