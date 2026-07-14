from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """Base interface for all LLM providers."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response from the LLM."""
        raise NotImplementedError