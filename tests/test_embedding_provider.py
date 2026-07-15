from providers.embeddings.gemini_embedding_provider import (
    GeminiEmbeddingProvider,
)


def main():

    provider = GeminiEmbeddingProvider()

    vector = provider.generate_embedding(
        "Fund transfer using OTP verification."
    )

    print(f"Dimensions : {len(vector)}")

    print(vector[:10])


if __name__ == "__main__":
    main()