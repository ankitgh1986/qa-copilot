from providers.llm.base_provider import BaseLLMProvider


class MockProvider(BaseLLMProvider):

    def generate(self, prompt: str) -> str:
        return """
{
    "summary":"Mock Summary",
    "quality_score":92,
    "ambiguity_score":18
}
"""