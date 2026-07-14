from providers.llm.gemini_provider import GeminiProvider


def main():
    provider = GeminiProvider()

    response = provider.generate(
        "Respond with exactly one word: Hello"
    )

    print(response)


if __name__ == "__main__":
    main()